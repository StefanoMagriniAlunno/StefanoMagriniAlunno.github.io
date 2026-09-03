from abc import ABC, abstractclassmethod
import torch
from typing import Any

class Generator(ABC):
    """ This class is the base class for all benchmark generators
    """
    
    device: torch.device
    precision: torch.dtype
    
    def __init__(
        self,
        device: torch.device = torch.device("cpu"),
        precision: torch.dtype = torch.float32):
        """ This method initialize the Generator
        """
        self.device = device
        self.precision = precision
        
    
    @abstractclassmethod
    def __call__(
        self,
        n_samples: int,
        reset: bool = False, 
        **kwargs: dict[str, Any]) -> torch.Tensor:
        """ This method generates the samples

        Args:
            n_samples (int): number of samples
            device (torch.device): device to generate samples on
            precision (torch.dtype): precision of the generated samples
            reset (bool): whether to reset the generator
        """
        raise NotImplementedError
    
    @abstractclassmethod
    def log_prob(
        self,
        x: torch.Tensor) -> torch.Tensor:
        """ This method computes the log probability of the samples
        """
        raise NotImplementedError
    
    @abstractclassmethod
    def score(
        self,
        x: torch.Tensor) -> torch.Tensor:
        """ This method computes the score of the samples
        """
        raise NotImplementedError
    
    @property
    def is_normalized(self) -> bool:
        """ This method returns whether the generator is normalized
        """
        return False