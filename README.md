# Space Horror Exploration Game

A first-person horror exploration game built with Panda3D, combining elements of Lethal Company's horror mechanics with No Man's Sky's vast exploration.

## Features (Planned)
- First-person exploration in procedurally generated environments
- Horror elements with dynamic enemy AI
- Interactive objects and environment
- Atmospheric lighting and sound design
- Low-poly stylized graphics with horror elements

## Setup
1. Install Python 3.8+ from [python.org](https://www.python.org/downloads/):
   - Download the installer for Windows
   - **Important**: Check "Add Python to PATH" during installation
   - **Important**: Do NOT install from Microsoft Store
2. Create and activate virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate
```
3. Install dependencies:
```bash
python -m pip install -r requirements.txt
```

## Development
- `src/` - Main game source code
- `assets/` - Game assets (models, textures, sounds)
- `config/` - Configuration files
- `tests/` - Test files

## Running the Game
```bash
python src/main.py
