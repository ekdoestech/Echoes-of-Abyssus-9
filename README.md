# Echoes of Abyssus-9  
A modular, narrative-driven Python text adventure set in deep space.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Focus](https://img.shields.io/badge/Focus-Game%20Architecture-purple)
![Gameplay](https://img.shields.io/badge/Gameplay-Narrative%20Driven-indigo)
![State](https://img.shields.io/badge/State-Inventory%20%26%20Progression-teal)
![Status](https://img.shields.io/badge/Status-v1.0%20Released-brightgreen)
![Platform](https://img.shields.io/badge/Platform-CLI%20%7C%20Cross--Platform-lightgrey)

----------------

## Overview

**Echoes of Abyssus-9** is a modular text adventure built to demonstrate clean Python architecture and state-driven gameplay. Set aboard a derelict deep-space research station, you navigate interconnected rooms, collect key components, and ultimately confront a rogue AI known as The Marrow.

**Highlights:**
- Modular codebase designed for extensibility
- Clean, maintainable Python code (PEP 8, type hints, docstrings)
- Clear separation of world, player, event, and UI logic
- State tracking for movement, inventory, progression, and endgame conditions
- Narrative-focused exploration gameplay

----------------

## Tech Stack
- **Language:** Python (3.8+)
- **Frameworks/Libs:** Standard Library only (no external dependencies)
- **Package manager:** None required
- **Platform:** Cross-platform (Windows, macOS, Linux)
- **Code style:** PEP 8

#### Scripts
- Run game:
  - `python src/game.py` (macOS/Linux)
  - `python .\src\game.py` (Windows)
  - `python -m src.game` (any OS, from project root)
- There are currently no additional dev or packaging scripts.

----------------

## Requirements
The project is intentionally lightweight:
- Python 3.8 or newer
- A terminal/console capable of running Python
No packages, virtual environments, or configuration steps are needed.

----------------

## Setup and Run
1. Clone the repository:
    ```bash
    git clone https://github.com/ekdoestech/Echoes-of-Abyssus-9.git
    ```
2. Change into the project directory:
    ```bash
    cd Echoes-of-Abyssus-9
    ```
3. Run the game:
    ```bash
    python src/game.py
    ```
   - Alternatively (any OS, from project root):
    ```bash
    python -m src.game
    ```
4. Follow on-screen instructions to move, explore, collect items, and survive.

----------------

## Planned Testing
- World validation (rooms, exits, item placement)
- Player mechanics (movement, inventory, item acquisition)
- Endgame logic (state-based outcomes)

----------------

## Project Structure
Current repository layout:
```
README.md
src/
  __init__.py
  events.py       # Narrative events (final encounter, etc.)
  game.py         # Main loop and command processing (entry point)
  items.py        # ROOM_ITEMS dictionary and helper functions for item management
  player.py       # Player state, movement, and inventory
  utils.py        # UI/printing helpers for status and instructions
  world.py        # Rooms, exits, items, and world helpers
```

----------------

## Gameplay & Progression

Exploration and progression are driven by player state and inventory.

**Gameplay Flow**
1. Explore the interconnected rooms of Abyssus-9.
2. Collect progression-critical components.
3. Unlock restricted paths and interactions.
4. Reach the Control Center and confront _The Marrow_.

**Progression Items**
Defeating _The Marrow_ requires collecting all six key components:
- Circuit Override Key — Security Office
- Engineering Scanner — Engineering Bay
- Cryo Sample Vial — Observation Deck
- Plasma Torch — Maintenance Tunnel
- Access Card — Bio Lab
- EMP Device Core — Server Room

These items form the core gating system that determines access and the outcome.

----------------

## Architectural Features
* Fully modular design dividing world, player state, events, and UI into separate modules 
* Explicit state management (visited rooms, inventory, progression requirements)
* Clear input/output loop with centralized command routing 
* Defensive progression design preventing sequence breaks 
* Extensible structure supporting new rooms, puzzles, and event types without modifying the core loop

----------------

## Potential enhancements
* ASCII art for rooms and key items
* Enemy encounters and a lightweight combat system
* Puzzle mechanics tied to room progression
* Save/load support via JSON or serialized state
* Branching dialogue and narrative choices
* Ambient audio and soundtrack integration
* Multiple endings based on player actions
These improvements would evolve the game from a linear adventure into a richer interactive fiction engine.
----------------

## Purpose
This project was created as a portfolio project focused on modular Python programming, state-driven design, and game architecture fundamentals. It serves as a foundation for building more advanced interactive fiction systems while demonstrating clean, maintainable code and thoughtful game structure. 

Contributions and suggestions are welcome—feel free to fork the repository and expand the station’s world or narrative.

----------------

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
© 2025 ekdoestech

----------------

## Acknowledgements
Inspired by classic text adventures, atmospheric sci-fi narratives, and modern interactive fiction engines.
Developed in part for SNHU coursework and continued as a personal exploration of game architecture.

----------------

## Contact
For questions, feedback, or collaboration:
- GitHub: **ekdoestech**
- Email: **ek.does.tech@gmail.com**
- LinkedIn: https://www.linkedin.com/in/erica-kinch

----------------

# Enjoy the adventure, and may you outwit The Marrow!
