import torch
from torch import nn
from typing import Any, Callable, Tuple

def compute_trajectory(
    t_ext: Tuple[float, float],
    n_steps: int,
    x0: torch.Tensor,
    drift: Callable[[torch.Tensor, float], torch.Tensor],
    sigma: Callable[[torch.Tensor, float], torch.Tensor],
    time_sampling: int = 1,
) -> torch.Tensor:
    """
    Compute a trajectory of the SDE using the Euler-Maruyama method.

    :param t_ext: Tuple containing the start and end times of the trajectory.
    :type t_ext: Tuple[float, float]
    :param n_steps: Number of time steps to use in the simulation.
    :type n_steps: int
    :param x0: Initial state of the system. It is a tensor of shape (N, d), where N is the number of samples and d is the dimensionality of the state space.
    :type x0: torch.Tensor
    :param drift: Function that computes the drift term f(X_t, t). It should take a tensor of shape (N, d) and a scalar time t, and return a tensor of the same shape (N, d).
    :type drift: Callable[[torch.Tensor, float], torch.Tensor]
    :param sigma: Function that computes the diffusion term sigma(X_t, t). It should take a tensor of shape (N, d) and a scalar time t, and return a tensor of the same shape (N, d, d).
    :type sigma: Callable[[torch.Tensor, float], torch.Tensor]
    :param time_sampling: Frequency of time point sampling. If 1, all time points are used.
    :type time_sampling: int
    :returns: Tensor containing the trajectory of the SDE at specified time points.
    :rtype: torch.Tensor
    """
    # Implementation of the Euler-Maruyama method goes here
    n_times = (n_steps + time_sampling - 1) // time_sampling
    N, d = x0.shape  # number of samples and dimensionality of the state space
    trajectory = torch.empty((n_times, N, d), dtype=x0.dtype, device=x0.device)
    dt = (t_ext[1] - t_ext[0]) / (n_steps - 1)  # assuming uniform time steps

    x_prev = x0.clone()  # has shape (N, d)
    dW = torch.empty((time_sampling, N, d), dtype=x0.dtype, device=x0.device)  # placeholder for random noise
    for i in range(n_steps):
        t = t_ext[0] + i * dt
        if i % time_sampling == 0:
            # save the current state in the trajectory
            trajectory[i // time_sampling] = x_prev
            dW = torch.randn((time_sampling, N, d), dtype=x0.dtype, device=x0.device) * torch.sqrt(torch.tensor(dt))
        
        # Compute drift and diffusion
        drift_term = drift(x_prev, t)  # has shape (N, d)
        diffusion_term = sigma(x_prev, t)  # has shape (N, d, d)
        
        # Generate random noise
        dW_current = dW[i % time_sampling]  # has shape (N, d)
        
        # Update state using Euler-Maruyama method
        x_next = x_prev.unsqueeze(-1) + drift_term.unsqueeze(-1) * dt + diffusion_term @ dW_current.unsqueeze(-1)  # has shape (N, d, 1)
        x_next = x_next.squeeze(-1)  # has shape (N, d)
        x_prev = x_next  # update for the next iteration
        
    return trajectory

if __name__ == "__main__":
    # Example usage
    N = 1000  # number of samples
    d = 2    # dimensionality of the state space
    x0 = torch.zeros((N, d))  # initial state

    def drift(x, t):
        return -x*0.2  # simple linear drift

    def sigma(x, t):
        return torch.eye(d).expand(N, d, d)*0.2  # identity diffusion

    t_ext = (0.0, 12.0)  # time points from 0 to 12 seconds
    n_steps = 10000  # number of time steps
    fps = 30  # frames per second for time sampling
    time_sampling = int(1/(fps * (t_ext[1] - t_ext[0]) / n_steps))  # sample every fps steps
    trajectory = compute_trajectory(t_ext, n_steps, x0, drift, sigma, time_sampling=time_sampling)
    print(trajectory.shape)  # should be (T, N, d)
    
    # creo una gif con l'evoluzione dei punti nel tempo
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib.animation import FuncAnimation, PillowWriter
    
    fig, ax = plt.subplots()
    scat = ax.scatter(trajectory[0, :, 0].numpy(), trajectory[0, :, 1].numpy(), s=1)
    # imposto i limiti dell'asse in base ai dati
    ax.set_xlim(trajectory[:, :, 0].min().item() - 1, trajectory[:, :, 0].max().item() + 1)
    ax.set_ylim(trajectory[:, :, 1].min().item() - 1, trajectory[:, :, 1].max().item() + 1)
    def update(frame):
        scat.set_offsets(trajectory[frame, :, :].numpy())
        return scat,
    ani = FuncAnimation(fig, update, frames=trajectory.shape[0], interval=1000/fps, blit=True)
    # salvo nella stessa cartella del file sde.py
    folder_path = __file__.rsplit('\\', 1)[0]  # get the folder path of the current file
    ani.save(f'{folder_path}\\trajectory.gif', writer=PillowWriter(fps=fps), dpi=200)