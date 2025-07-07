# heat2d

`heat2d` solves the steady‑state temperature distribution on a square plate
using a finite difference approach. The top boundary is held at 100°C, the
bottom at 0°C, and the left and right boundaries are insulated.

## Installation
1. Create a Python virtual environment.
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```
2. Install the requirements.
   ```bash
   pip install -r requirements.txt
   ```

## Running the simulation
From within this directory:
```bash
python -m src.main
```
The resulting heatmap is saved to `outputs/heatmap.png`.
