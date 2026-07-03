import torch
from torch.func import vmap, jacrev, hessian
from torch import nn
from typing import Any, Callable

def compute_jacobian(
    model: Callable[[torch.Tensor], torch.Tensor],
    x: torch.Tensor,
    *model_args: Any,
    **model_kwargs: Any) -> torch.Tensor:
    """
    Compute the per-sample Jacobian of ``model`` with respect to its input.

    ``model`` is assumed to map an input of shape ``(a,)`` to an output of
    shape ``(b,)``, and a batched input of shape ``(N, a)`` to an output of
    shape ``(N, b)``. Given ``x`` with shape ``(N, a)``, the returned tensor
    has shape ``(N, b, a)``.

    :param model: Function evaluated on single samples or batches.
    :type model: Callable[[torch.Tensor], torch.Tensor]
    :param x: Input batch of shape ``(N, a)``.
    :type x: torch.Tensor
    :returns: Per-sample Jacobian tensor of shape ``(N, b, a)``.
    :rtype: torch.Tensor
    """
    def wrapped_model(single_x: torch.Tensor) -> torch.Tensor:
        return model(single_x, *model_args, **model_kwargs)

    J = vmap(jacrev(wrapped_model), randomness='same')(x)
    return J

def compute_hessian(
    model: Callable[[torch.Tensor], torch.Tensor],
    x: torch.Tensor,
    *model_args: Any,
    **model_kwargs: Any) -> torch.Tensor:
    """
    Compute the per-sample Hessian of ``model`` with respect to its input.

    ``model`` is assumed to map an input of shape ``(a,)`` to an output of
    shape ``(b,)``, and a batched input of shape ``(N, a)`` to an output
    of shape ``(N, b)``. Given ``x`` with shape ``(N, a)``, the returned
    tensor has shape ``(N, b, a, a)``: for each batch index ``i``,
    ``H[i]`` is the Hessian of ``model`` evaluated at ``x[i]`` and has shape
    ``(a, a)``.

    :param model: Function evaluated on single samples or batches.
    :type model: Callable[[torch.Tensor], torch.Tensor]
    :param x: Input batch of shape ``(N, a)``.
    :type x: torch.Tensor
    :returns: Per-sample Hessian tensor of shape ``(N, b, a, a)``.
    :rtype: torch.Tensor
    """
    def wrapped_model(single_x: torch.Tensor) -> torch.Tensor:
        return model(single_x, *model_args, **model_kwargs)

    H = vmap(hessian(wrapped_model), randomness='same')(x)
    return H

def compute_laplacian(
    model: Callable[[torch.Tensor], torch.Tensor],
    x: torch.Tensor,
    *model_args: Any,
    **model_kwargs: Any
) -> torch.Tensor:
    """
    Compute the per-sample Laplacian of ``model`` with respect to its input.

    The Laplacian is obtained as the trace of the per-sample Hessian. The
    function first computes the Hessian tensor ``H`` with shape
    ``(N, b, a, a)`` via :func:`compute_hessian`, and then sums the diagonal
    entries along the last two dimensions. Given ``x`` with shape ``(N, a)``,
    the returned tensor has shape ``(N, b)``.
    
    ``model`` is assumed to map an input of shape ``(a,)`` to an output of
    shape ``(b,)``, and a batched input of shape ``(N, a)`` to an output
    of shape ``(N, b)``. Given ``x`` with shape ``(N, a)``, the returned
    tensor has shape ``(N, b)``: for each batch index ``i``,
    ``H[i]`` is the Laplacian of ``model`` evaluated at ``x[i]`` and has
    shape ``(a, a)``.

    :param model: Function evaluated on single samples or batches.
    :type model: Callable[[torch.Tensor], torch.Tensor]
    :param x: Input batch of shape ``(N, a)``.
    :type x: torch.Tensor
    :returns: Per-sample Laplacian tensor of shape ``(N, b)``.
    :rtype: torch.Tensor
    """
    H = compute_hessian(model, x, *model_args, **model_kwargs)
    laplacian = H.diagonal(dim1=-2, dim2=-1).sum(-1)
    return laplacian