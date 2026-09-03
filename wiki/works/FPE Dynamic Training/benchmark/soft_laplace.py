import torch
import torchsde
import math
import numpy as np
from typing import Tuple
from math import exp, cos, acos, sqrt, gamma

from .templates import Generator
import torch

class SoftLaplace(Generator):
    
    __n_dim: int
    __rate: float
    __beta: float
    __shape_factor_intensity: float
    __advanced: bool

    def __init__(
        self,
        n_dim: int = 1,
        rate: float = 1.0,
        beta: float = 1.0,
        shape_factor_intensity: float = 0.1,
        shape_fixed: torch.Tensor = None,
        device: torch.device = torch.device("cpu"),
        precision: torch.dtype = torch.float32):
        """ This method initialize the Mexican Hat generator
        
        Args:
            n_dim (int): dimension of the samples
            rate (float): rate of the potential
            beta (float): beta value
            shape_factor_intensity (float): shape factor for the intensity
            shape_fixed (torch.Tensor): fixed shape factor, if None it is generated randomly
        """
        super().__init__(device=device, precision=precision)

        self.__n_dim = n_dim
        self.__rate = rate
        self.__beta = beta
        self.__shape_factor_intensity = shape_factor_intensity
        
        if shape_fixed is not None:
            self.__Sd = shape_fixed.to(self.device, dtype=self.precision)
        else:
            while True:
                self.__Sd = torch.eye(self.__n_dim, dtype=self.precision, device=self.device)
                self.__Sd = self.__Sd + self.__shape_factor_intensity * torch.randn(self.__n_dim, self.__n_dim, dtype=self.precision, device=self.device)
                if torch.linalg.norm(self.__Sd, ord=2) > 1e-3:
                    break
        self.__Sd /= torch.linalg.norm(self.__Sd, ord=2)
        
        q: float = self.__beta * self.__rate
        if q >= 2.0:
            self.__advanced = True  # advanced algorithm
            # parameters for the advanced algorithm
            z_star = 27*q**2 - 9*self.__n_dim*q**2 - 9*self.__n_dim*q - 2*self.__n_dim**3
            z_star = z_star / (2*(3*q**2 + 3*q + self.__n_dim**2)**(3/2))
            z_star = cos(acos(-z_star) / 3)
            z_star = z_star * (2*sqrt(3*q**2+3*q+self.__n_dim**2)) / (3*q)
            z_star = z_star - (3*q - self.__n_dim) / (3*q)
            
            # improve the precision of z_star with netwon raphson method
            f = lambda z: self.__n_dim * (z + 1)**2 + z - q * z * (z + 1) * (z + 2)
            f_prime = lambda z: 2 * self.__n_dim * (z + 1) + 1 - q * (3 * z**2 + 6 * z + 2)
            for _ in range(5):
                z_star = z_star - f(z_star) / f_prime(z_star)

            self.__M = z_star ** (self.__n_dim / 2)
            self.__M = self.__M * (z_star + 2)**(self.__n_dim/2 - 1)
            self.__M = self.__M * (z_star + 1)
            self.__M = self.__M * exp(-q*z_star)
            self.__M = self.__M / gamma(self.__n_dim / 2)
            self.__M = self.__M * exp(self.__n_dim / 2)
            self.__M = self.__M / (self.__n_dim / 2)**(self.__n_dim / 2)
            
            self.__u = self.__n_dim / (2*z_star)
            self.__Zg = gamma(self.__n_dim / 2) / self.__u ** (self.__n_dim / 2)
            self.__q = q
        else:
            self.__advanced = False  # basic algorithm
            self.__M = gamma(self.__n_dim) / q ** self.__n_dim
            self.__Zg = gamma(self.__n_dim) / q ** (self.__n_dim)
            self.__q = q

    @property
    def shape(self) -> torch.Tensor:
        """ This method returns the shape factor of the generator
        """
        return self.__Sd

    def advanced_algorithm(self, n_samples: int) -> torch.Tensor:
        """ This method generates samples from the Soft Laplace distribution using the advanced algorithm
        
        Args:
            n_samples (int): number of samples to generate
        """
        g = lambda z: z ** (self.__n_dim / 2 - 1) * torch.exp(-self.__u * z) / self.__Zg
        f = lambda z: (z + 2) ** (self.__n_dim / 2 - 1) * (z + 1) * z ** (self.__n_dim / 2 - 1) * torch.exp(-self.__q * z)
        # get n_samples from the distribution g(z) using torch (it is a gamma distribution)
        Z = torch.empty(n_samples, device=self.device, dtype=self.precision)
        current_dim = 0
        while current_dim < n_samples:
            # sample from the gamma distribution
            Z_temp = torch.distributions.Gamma(self.__n_dim / 2, self.__u).sample((n_samples - current_dim,)).to(self.device, dtype=self.precision)
            # rejection sampling
            U = torch.rand(n_samples - current_dim, device=self.device)
            Z_temp = Z_temp[U < f(Z_temp) / (self.__M * g(Z_temp))]
            Z[current_dim:current_dim + Z_temp.shape[0]] = Z_temp
            current_dim += Z_temp.shape[0]
        Z = self.__beta * ((Z+1)**2-1)**0.5
        return Z
    
    def basic_algorithm(self, n_samples: int) -> torch.Tensor:
        """ This method generates samples from the Soft Laplace distribution using the basic algorithm
        
        Args:
            n_samples (int): number of samples to generate
        """
        g = lambda z: z ** (self.__n_dim - 1) * torch.exp(-self.__q * z) / self.__Zg
        f = lambda z: z ** (self.__n_dim - 1) * torch.exp(-self.__q * (z**2 + 1)**0.5)
        # get n_samples from the distribution g(z) using torch (it is a gamma distribution)
        Z = torch.empty(n_samples, device=self.device, dtype=self.precision)
        current_dim = 0
        while current_dim < n_samples:
            # sample from the gamma distribution
            Z_temp = torch.distributions.Gamma(self.__n_dim, self.__q).sample((n_samples - current_dim,)).to(self.device, dtype=self.precision)
            # rejection sampling
            U = torch.rand(n_samples - current_dim, device=self.device)
            Z_temp = Z_temp[U < f(Z_temp) / (self.__M * g(Z_temp))]
            Z[current_dim:current_dim + Z_temp.shape[0]] = Z_temp
            current_dim += Z_temp.shape[0]
        Z = self.__beta * Z
        return Z

    def __call__(self, n_samples: int) -> torch.Tensor:
        """ This method generates samples from the Soft Laplace distribution
        
        Args:
            n_samples (int): number of samples to generate
        """
        if self.__advanced:
            radius = self.advanced_algorithm(n_samples)
        else:
            radius = self.basic_algorithm(n_samples)
        v = torch.randn(n_samples, self.__n_dim, device=self.device, dtype=self.precision)
        v = v / torch.norm(v, dim=1, keepdim=True)
        Z = radius.unsqueeze(1) * v
        Z = Z @ self.__Sd.T
        return Z

    def score(self, x: torch.Tensor) -> torch.Tensor:
        """ This method computes the score of the samples
        
        Args:
            x (torch.Tensor): samples to compute the score
        """
        x = x.to(self.device, dtype=self.precision)
        r_squared = torch.einsum('bi,ij,bj->b', x, self.__Svinv, x)
        c = (r_squared + self.__beta**2)**0.5 * self.__temperature
        return - (self.__Svinv @ x.T).T / c.unsqueeze(1)

    def log_prob(self, x: torch.Tensor) -> torch.Tensor:
        """ This method computes the log probability of the samples
        
        Args:
            x (torch.Tensor): samples to compute the log probability
        """
        x = x.to(self.device, dtype=self.precision)
        r_squared = torch.einsum('bi,ij,bj->b', x, self.__Svinv, x)
        return (r_squared + self.__beta**2)**0.5/self.__temperature
    
    @property
    def is_normalized(self) -> bool:
        """ Check if the Soft Laplace distribution is normalized.
        
        Returns:
            bool: True if the distribution is normalized, False otherwise
        """
        return False