"""Entry point for running the heat2d simulation."""

from __future__ import annotations

import pathlib

from . import solver, plotter, config


def main() -> None:
    """Run the full simulation and save the resulting heatmap."""
    output_dir = pathlib.Path(__file__).resolve().parents[1] / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "heatmap.png"

    T = solver.solve(config.DEFAULT_GRID_SIZE, config.DEFAULT_TOLERANCE)
    plotter.plot_heatmap(T, str(output_path))

    print("Simulation completed. See heatmap at:", output_path)


if __name__ == "__main__":
    main()
