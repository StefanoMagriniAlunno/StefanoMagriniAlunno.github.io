import torch
import torchsde
import math
import numpy as np
from typing import Tuple

from .templates import Generator
import torch

class MexicanHat(Generator):

    class SDEclass(torch.nn.Module):
        def __init__(self, radius: float, temperature: float, Sd: torch.Tensor, velocity: float):
            """ Initialize the SDE for the Mexican Hat distribution.
            Args:
                radius (float): radius of the Mexican Hat
                temperature (float): intensity of the noise
                Sd (torch.Tensor): transformation matrix for the space
                velocity (float): velocity of the particles in the ergodic term
            """
            super().__init__()
            self.radius = radius
            self.Sd = Sd
            self.Sv = self.Sd.T @ self.Sd  # Transformation matrix for the space
            self.Sv_inv = torch.linalg.inv(self.Sv)  # Inverse of the transformation matrix
            self.ndim = Sd.shape[0]  # Space dimension
            self.velocity = velocity
            self.temperature = temperature
            
            self.M = torch.randn(self.ndim, self.ndim)
            self.M = self.M - self.M.T  # Make it antisymmetric
            
            self.noise_type = "general" 
            self.sde_type = "ito"

        def r_squared(self, x: torch.Tensor) -> torch.Tensor:
            """ Compute the squared Sv_inv-norm.

            Args:
                x (torch.Tensor): Input tensor of shape (batch_size, n_dim)

            Returns:
                torch.Tensor: Output tensor of shape (batch_size,)
            """
            return torch.einsum('bi,ij,bj->b', x, self.Sv_inv, x)

        def value(self, x: torch.Tensor) -> torch.Tensor:
            """ Compute a useful value for the drift and diffusion terms.

            Args:
                x (torch.Tensor): Input tensor of shape (batch_size, n_dim)

            Returns:
                torch.Tensor: Output tensor of shape (batch_size,)
            """
            r_squared = self.r_squared(x)
            return ((r_squared - self.radius**2)**2 + 
                    self.radius**4/4+4*self.temperature)**0.5
        
        def h(self, s2):
            """ Compute a useful value for the ergodic term.

            Args:
                s2 (torch.Tensor): Input tensor of shape (batch_size,), it is the squared norm of the scored vector s.

            Returns:
                torch.Tensor: Output tensor of shape (batch_size,)
            """
            return self.velocity / (s2 + 1)**0.5
        
        def s(self, x: torch.Tensor) -> torch.Tensor:
            """ Compute the scored vector of the steady state.

            Args:
                x (torch.Tensor): Input tensor of shape (batch_size, n_dim)

            Returns:
                torch.Tensor: Output tensor of shape (batch_size, n_dim)
            """
            r_squared = self.r_squared(x)
            coef = 1 / (2.0 * self.temperature * self.radius**2)
            return - coef * (r_squared - self.radius**2).unsqueeze(-1) * (self.Sv_inv @ x.T).T

        def ergodic_term(self, s: torch.Tensor) -> torch.Tensor:
            """ Compute the ergodic term.

            Args:
                s (torch.Tensor): Input tensor of shape (batch_size, n_dim), it is the scored vector of the steady state.

            Returns:
                torch.Tensor: Output tensor of shape (batch_size, n_dim)
            """
            return (
                0.5 * torch.einsum(
                    'b, ij, bj -> bi',
                    self.h(torch.sum(s**2, dim=1)),
                    self.M,
                    s)
            )
        
        def f(self, t: float, x: torch.Tensor) -> torch.Tensor:
            """ Compute the drift term.

            Args:
                t (float): time
                x (torch.Tensor): Input tensor with shape (batch_size, n_dim)

            Returns:
                torch.Tensor: Output tensor with shape (batch_size, n_dim)
            """
            value = self.value(x)
            r_squared = self.r_squared(x)
            coef = 1 / 4.0
            drift_coeff = (self.temperature + coef * value**2) / (value**3) * (r_squared - self.radius**2)
            return -drift_coeff.unsqueeze(-1) * x + self.ergodic_term(self.s(x))  # Drift term with ergodic component

        def g(self, t: float, x: torch.Tensor) -> torch.Tensor:
            """ Compute the diffusion term

            Args:
                t (float): time
                x (torch.Tensor): Input tensor with shape (batch_size, n_dim)

            Returns:
                torch.Tensor: Output tensor with shape (batch_size, n_dim, n_dim)
            """
            noise_coeff = (self.temperature / self.value(x))**0.5
            return noise_coeff.reshape(-1, 1, 1) * self.Sd.T.reshape(1, self.ndim, self.ndim) 
    
    __batch_size: int
    __n_dim: int
    __radius: float
    __shape_factor_intensity: float
    __Sd: torch.Tensor
    __dt: float
    __ergodic_interval: float
    __velocity: float
    __final_state: torch.Tensor

    def __init__(
        self,
        batch_size: int,
        n_dim: int = 1,
        radius: float = 1.0,
        temperature: float = 1.0,
        shape_factor_intensity: float = 0.1,
        shape_fixed: torch.Tensor = None,
        time: float = 5.0,
        dt: float = 0.001,
        ergodic_interval: float = 0.2,
        velocity: float = 0.0,
        device: torch.device = torch.device("cpu"),
        smooth_coefficient: float = 1.0,
        precision: torch.dtype = torch.float32):
        """ This method initialize the Mexican Hat generator
        
        Args:
            batch_size (int): number of samples for the initialization
            n_dim (int): dimension of the SDE
            radius (float): radius of the ring
            temperature (float): intensity of the noise
            shape_factor_intensity (float): intensity of the shape factor
            shape_fixed (torch.Tensor): fixed shape factor, if None it is generated randomly
            time (float): time to reach the steady state
            dt (float): time step of the scheme
            ergodic_interval (float): time interval for a new sampling
            velocity (float): velocity of the wind
        """
        super().__init__(device=device, precision=precision)

        self.__batch_size = batch_size
        self.__n_dim = n_dim
        self.__radius = radius
        self.__temperature = temperature
        self.__shape_factor_intensity = shape_factor_intensity
        self.__dt = dt
        self.__ergodic_interval = ergodic_interval
        self.__velocity = velocity

        if shape_fixed is not None:
            self.__Sd = shape_fixed.to(self.device, dtype=self.precision)
        else:
            while True:
                self.__Sd = torch.eye(self.__n_dim, dtype=self.precision, device=self.device)
                self.__Sd = self.__Sd + self.__shape_factor_intensity * torch.randn(self.__n_dim, self.__n_dim, dtype=self.precision, device=self.device)
                if torch.norm(self.__Sd) > 1e-3:
                    break
        self.__Sd /= torch.linalg.norm(self.__Sd, ord=2)
        
        # initialize the state of the particles
        initial_state: torch.Tensor = torch.randn(self.__batch_size, self.__n_dim, dtype=self.precision, device=self.device)
        initial_state: torch.Tensor = self.__radius * initial_state / torch.norm(initial_state, dim=1, keepdim=True)
        # change shape of the initial state to match the shape of the SDE
        initial_state: torch.Tensor = initial_state @ self.__Sd.T
        
        # initialize the SDE simulation
        steps: int = int(time / self.__dt) + 1
        true_time: float = steps * self.__dt
        ts: torch.Tensor = torch.Tensor([0.0, true_time])
        
        # start the simulation to reach the steady state
        sde = MexicanHat.SDEclass(self.__radius, self.__temperature, self.__Sd, 0.0)
        self.__final_state = torchsde.sdeint(sde, y0=initial_state, ts=ts, method='euler', dt=self.__dt)[-1]
        self.__sde = MexicanHat.SDEclass(self.__radius, self.__temperature, self.__Sd, self.__velocity)
        
        self.__Svinv = torch.linalg.inv(self.__Sd.T @ self.__Sd)

    @property
    def shape(self) -> torch.Tensor:
        """ This method returns the shape factor of the generator
        """
        return self.__Sd

    def __call__(self, n_samples: int) -> torch.Tensor:
        """ Generate samples

        Args:
            n_samples (int): number of samples

        Returns:
            torch.Tensor: samples
        """
        
        # remove shape from the final state to match the shape of the SDE
        
        self.__final_state = self.__final_state @ torch.linalg.inv(self.__Sd)
        # change angle of the final state
        radii = torch.norm(self.__final_state, dim=-1, keepdim=True)
        directions = torch.randn(self.__batch_size, self.__n_dim, dtype=self.precision, device=self.device)
        directions = directions / torch.norm(directions, dim=-1, keepdim=True)
        self.__final_state = radii * directions
        # insert the shape of the final state to match the shape of the SDE
        self.__final_state = self.__final_state @ self.__Sd
        
        # number of repetitions
        repetitions: int = (n_samples + self.__batch_size - 1) // self.__batch_size 
        time: float = self.__ergodic_interval * repetitions
        ts: torch.Tensor = torch.linspace(0.0, time, repetitions+1)
        
        # simulation
        trajectories = torchsde.sdeint(self.__sde, y0=self.__final_state, ts=ts, method='euler', dt=self.__dt)
        
        trajectories = trajectories.reshape(-1, self.__n_dim)
        trajectories = trajectories[torch.randperm(trajectories.shape[0])]    
        self.__final_state = trajectories[-self.__final_state.shape[0]:]  # NOTE: here the update of the last frame, the idea is improve the ergodicity
        return trajectories[:n_samples]
    
    def log_prob(self, x: torch.Tensor) -> torch.Tensor:
        """ This method computes the log probability of the samples
        
        Args:
            x (torch.Tensor): samples to compute the log probability
        """
        x = x.to(self.device, dtype=self.precision)
        r_squared = torch.einsum('bi,ij,bj->b', x, self.__Svinv, x)
        c = 1.0 / (8.0 * self.__temperature)
        return - c * (r_squared - self.__radius**2)**2
    
    def score(self, x: torch.Tensor) -> torch.Tensor:
        """ This method computes the score of the samples
        
        Args:
            x (torch.Tensor): samples to compute the score
        """
        x = x.to(self.device, dtype=self.precision)
        r_squared = torch.einsum('bi,ij,bj->b', x, self.__Svinv, x)
        c = 1.0 / (4.0 * self.__temperature)
        return - 4.0 * c * (r_squared - self.__radius**2).unsqueeze(-1) * (self.__Svinv @ x.T).T
    
    @property
    def is_normalized(self) -> bool:
        """ This method returns whether the generator is normalized
        """
        return False