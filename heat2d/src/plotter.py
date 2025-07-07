"""Utilities for visualizing temperature distributions."""

import matplotlib.pyplot as plt
import numpy as np


def plot_heatmap(T: np.ndarray, output_path: str) -> None:
    """Plot a heatmap of the temperature field and save it."""
    plt.figure(figsize=(6, 5))
    plt.imshow(T, origin="lower", cmap="hot", aspect="auto")
    plt.colorbar(label="Temperature (°C)")
    plt.title("Steady-State Temperature Distribution")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"Heatmap saved to {output_path}")
