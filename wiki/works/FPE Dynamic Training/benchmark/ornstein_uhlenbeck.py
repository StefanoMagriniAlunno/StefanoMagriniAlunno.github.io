from .templates import Generator
import torch

class OrnsteinUhlenbeck(Generator):
    
    __n_dim: int
    __temperature: float
    __shape_factor_intensity: float
    __Sd: torch.Tensor
    __Sv_inv: torch.Tensor
    
    def __init__(
        self,
        n_dim: int = 1,
        temperature: float = 1.0,
        shape_factor_intensity: float = 0.1,
        shape_fixed: torch.Tensor = None,
        device: torch.device = torch.device("cpu"),
        precision: torch.dtype = torch.float32):
        """ This method initialize the Ornstein-Uhlenbeck generator
        
        Args:
            n_dim (int): dimension of the SDE
            shape_factor_intensity (float): intensity of the shape factor
            shape_fixed (torch.Tensor): fixed shape factor, if None it is generated randomly
            temperature (float): intensity of the noise
        """
        super().__init__(device=device, precision=precision)
        
        self.__n_dim = n_dim
        self.__temperature = temperature
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
        self.__Sd *= self.__temperature**0.5
        self.__Sv_inv = torch.linalg.inv(self.__Sd @ self.__Sd.T)

    @property
    def shape(self) -> torch.Tensor:
        """ This method returns the shape factor of the generator
        """
        return self.__Sd.clone()

    def __call__(
            self,
            n_samples: int,
            reset: bool = False) -> torch.Tensor:
        """ Generate samples from the Ornstein-Uhlenbeck process.

        Args:
            n_samples (int): number of samples to generate
            reset (bool): whether to reset the generator

        The total number of samples generated will be n_samples.

        Returns:
            samples (torch.Tensor): samples from the Ornstein-Uhlenbeck process
        """
        
        # Generate samples from the Ornstein-Uhlenbeck process
        z = torch.randn(n_samples, self.__n_dim, dtype=self.precision, device=self.device)  # Standard normal samples
        samples = torch.einsum('ij,kj->ki', self.__Sd, z)  # Apply the transformation matrix

        return samples
    
    def log_prob(
        self,
        x: torch.Tensor) -> torch.Tensor:
        """ Compute the log probability of the Ornstein-Uhlenbeck process at given points.

        Args:
            x (torch.Tensor): points at which to compute the log probability
        """
        # Compute the log probability of the Ornstein-Uhlenbeck process
        # The log probability is given by the multivariate normal distribution with mean 0 and covariance matrix
        cov_matrix = self.__Sd @ self.__Sd.T
        mean = torch.zeros(self.__n_dim, dtype=self.precision, device=self.device)
        return torch.distributions.MultivariateNormal(mean, cov_matrix).log_prob(x)

    def score(self, x: torch.Tensor) -> torch.Tensor:
        """ This method computes the score of the samples
        
        Args:
            x (torch.Tensor): samples to compute the score
        """
        x = x.to(self.device, dtype=self.precision)
        return - torch.einsum('bi,ij->bj', x, self.__Sv_inv)

    def is_normalized(self) -> bool:
        """ Check if the Ornstein-Uhlenbeck process is normalized.

        Returns:
            bool: True if the process is normalized, False otherwise
        """
        return True