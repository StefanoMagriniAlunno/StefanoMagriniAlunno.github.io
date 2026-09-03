import torch
import numpy as np
from typing import Tuple

from .templates import Generator
import torch

class StudentT(Generator):
    
    __n_dim: int
    __tail_weight: float
    __shape_factor_intensity: float
    __mode: bool

    def __init__(
        self,
        n_dim: int = 1,
        beta: float = 1.0,
        tail_weight: float = 1.0,
        shape_factor_intensity: float = 0.1,
        shape_fixed: torch.Tensor = None,
        device: torch.device = torch.device("cpu"),
        precision: torch.dtype = torch.float32):
        """ This method initialize the Mexican Hat generator
        
        Args:
            n_dim (int): dimension of the samples
            tail_weight (float): weight of the tails, it is greater than 1 and n_dim/2
            shape_factor_intensity (float): shape factor for the intensity
        """
        super().__init__(device=device, precision=precision)

        self.__n_dim = n_dim
        self.__tail_weight = tail_weight
        self.__shape_factor_intensity = shape_factor_intensity
        
        if self.__tail_weight <= 1.0 or self.__tail_weight <= self.__n_dim / 2:
            raise ValueError("tail_weight must be greater than 1 and n_dim/2")
        
        if shape_fixed is not None:
            self.__Sd = shape_fixed.to(self.device, dtype=self.precision)
        else:
            while True:
                self.__Sd = torch.eye(self.__n_dim, dtype=self.precision, device=self.device)
                self.__Sd = self.__Sd + self.__shape_factor_intensity * torch.randn(self.__n_dim, self.__n_dim, dtype=self.precision, device=self.device)
                if torch.linalg.norm(self.__Sd, ord=2) > 1e-3:
                    break
        self.__Sd /= torch.linalg.norm(self.__Sd, ord=2)
        
        self.__Sigma = self.__Sd.T @ self.__Sd
        self.__Sv_inv = torch.linalg.inv(self.__Sigma)
        self.__k = self.__tail_weight - self.__n_dim / 2
        
        self.__beta2 = beta**2
        self.__theta = 2.0 / self.__beta2  # scale parameter for the gamma distribution
        self.__rate = 1.0 / self.__theta  # rate parameter for the gamma distribution

    @property
    def shape(self) -> torch.Tensor:
        """ This method returns the shape factor of the generator
        """
        return self.__Sd.clone()

    def __call__(self, n_samples: int) -> torch.Tensor:
        """ This method generates samples from the Student's t distribution
        
        Args:
            n_samples (int): number of samples to generate
        """
        # Generate samples from the Student's t distribution
        # multivariate normal samples with covariance matrix Sigma
        normal_samples = torch.randn(n_samples, self.__n_dim, dtype=self.precision, device=self.device)
        normal_samples = normal_samples @ self.__Sd
        # Generate samples from gamma with theta=2
        gamma_samples = torch.distributions.Gamma(self.__k, self.__rate).sample((n_samples,)).to(self.device, dtype=self.precision)
        # Generate Student's t samples
        student_t_samples = normal_samples / torch.sqrt(gamma_samples).unsqueeze(1)
        return student_t_samples
    
    def log_prob(self, x: torch.Tensor) -> torch.Tensor:
        """ This method computes the log probability of the Student's t distribution
        
        Args:
            x (torch.Tensor): samples to compute the log probability
        """
        x = x.to(self.device, dtype=self.precision)
        log_prob = -self.__tail_weight * torch.log(self.__beta2 + torch.sum(x @ self.__Sv_inv * x, dim=1))
        logZ = ((torch.linalg.slogdet(self.__Sigma)[1]) / 2.0
            + (self.__n_dim / 2 - self.__tail_weight) * torch.log(torch.tensor(self.__beta2, dtype=self.precision, device=self.device))
            + self.__n_dim / 2 * torch.log(torch.tensor(np.pi, dtype=self.precision, device=self.device))
            + torch.lgamma(torch.tensor(self.__tail_weight - self.__n_dim / 2, dtype=self.precision, device=self.device))
            - torch.lgamma(torch.tensor(self.__tail_weight, dtype=self.precision, device=self.device)))
        return log_prob - logZ
    
    def score(self, x: torch.Tensor) -> torch.Tensor:
        """ This method computes the score of the samples
        
        Args:
            x (torch.Tensor): samples to compute the score
        """
        x = x.to(self.device, dtype=self.precision)
        c = -self.__tail_weight / (self.__beta2 + torch.sum(x @ self.__Sv_inv * x, dim=1))
        num = (self.__Sv_inv @ x.T).T
        return c.unsqueeze(1) * num * 2.0
    
    def is_normalized(self) -> bool:
        """ Check if the Student's t distribution is normalized.
        
        Returns:
            bool: True if the distribution is normalized, False otherwise
        """
        return True