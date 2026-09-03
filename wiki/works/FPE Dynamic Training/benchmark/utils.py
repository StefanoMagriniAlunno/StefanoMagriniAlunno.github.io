from . import Generator
import torch

def compute_normalization_constant(
    objective: Generator,
    samples: torch.Tensor,
    bg_log_probs: torch.Tensor
) -> float:
    """ Compute the normalization constant Z for the objective distribution using importance sampling with the background distribution.
    
    Args:
        objective (Generator): the objective distribution
        samples (torch.Tensor): the samples from the background distribution
        bg_log_probs (torch.Tensor): the log probabilities of the samples with respect to the background distribution
    
    Returns:
        float: the estimated normalization constant Z
    """
    if objective.is_normalized:
        return 1.0
    return torch.mean(torch.exp(objective.log_prob(samples) - bg_log_probs))