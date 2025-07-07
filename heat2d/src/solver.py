"""Finite difference solver for 2D steady-state heat conduction."""

from __future__ import annotations

import numpy as np

from . import config


def solve(grid_size: int = config.DEFAULT_GRID_SIZE, tolerance: float = config.DEFAULT_TOLERANCE) -> np.ndarray:
    """Solve the temperature distribution on a square plate.

    Parameters
    ----------
    grid_size:
        Number of grid points in each dimension.
    tolerance:
        Convergence criteria for the maximum temperature change between iterations.

    Returns
    -------
    numpy.ndarray
        2D array of temperature values at steady state.
    """

    # Initialize grid
    T = np.zeros((grid_size, grid_size), dtype=float)

    # Apply Dirichlet boundary conditions on top and bottom
    T[0, :] = config.TOP_TEMPERATURE
    T[-1, :] = config.BOTTOM_TEMPERATURE

    # Left and right boundaries start equal to adjacent interior (Neumann BC)
    T[:, 0] = T[:, 1]
    T[:, -1] = T[:, -2]

    delta = np.inf
    iteration = 0

    while delta > tolerance:
        T_old = T.copy()

        # Update interior points (vectorized computation using slicing)
        T[1:-1, 1:-1] = 0.25 * (
            T_old[2:, 1:-1] + T_old[:-2, 1:-1] + T_old[1:-1, 2:] + T_old[1:-1, :-2]
        )

        # Enforce Neumann BCs on left and right after update
        T[:, 0] = T[:, 1]
        T[:, -1] = T[:, -2]

        delta = np.max(np.abs(T - T_old))
        iteration += 1

    print(f"Converged after {iteration} iterations with max \u0394T = {delta:.2e}")
    return T
