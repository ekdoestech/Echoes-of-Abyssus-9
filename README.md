# Echoes of Abyssus-9  
A Modular Python Text Adventure Set in Deep Space

----------------
## Overview

**Echoes of Abyssus-9** is a modular text adventure built to showcase clean Python architecture, reusable modules, and state-driven gameplay. Set aboard a derelict deep-space research station, you navigate interconnected rooms, collect key components, and ultimately confront a rogue AI known as The Marrow.

**Highlights:**
- Modular codebase designed for extensibility
- Clean, maintainable Python code (PEP 8, type hints, docstrings)
- Clear separation of world, player, event, and UI logic
- State tracking for movement, inventory, progression, and endgame conditions
- Narrative-focused exploration gameplay

----------------

## Stack and Entry Point
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

3. (Optional) Create and activate a virtual environment:
   - macOS/Linux:
     ```bash
     python3 -m venv .venv && source .venv/bin/activate
     ```
   - Windows (PowerShell):
     ```powershell
     python -m venv .venv; .\.venv\Scripts\Activate.ps1
     ```

4. Run the game:
   - macOS/Linux:
     ```bash
     python3 src/game.py
     ```
   - Windows (PowerShell):
     ```powershell
     python .\src\game.py
     ```
   - Alternatively (any OS, from project root):
     ```bash
     python -m src.game
     ```

5. Follow on-screen instructions to move, explore, collect items, and survive.

----------------

## Environment Variables
No environment variables are required. The game runs entirely in a standard terminal session with no external configuration.

**Future Expansion:**
If save/load functionality or user-configurable options are added, related environment variables will be documented here.

----------------

## Tests
Automated tests are not included yet, but the project is structured to support testability.
Planned areas for coverage include:

**World validation —** ensuring all rooms, exits, and item placements form a coherent, navigable map.
**Player mechanics —** verifying movement, inventory behavior, and item acquisition.
**Endgame logic —** confirming correct outcomes based on collected items and player state.

Recommended frameworks include pytest or Python’s built-in unittest.

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

## Core Gameplay Loop
The gameplay loop focuses on exploration-driven progression:
1. Navigate the interconnected rooms of Abyssus-9.
2. Collect key items required to advance deeper into the station.
3. Unlock restricted areas as your inventory expands.
4. Reach the Control Center to confront _The Marrow_.
5. Deploy the EMP Device Core to complete the final encounter.
----------------

## Progression Items
The station can be explored freely, including early access to the Control Center. However, defeating _The Marrow_ requires collecting all six progression-critical components:
- Circuit Override Key — Security Office
- Engineering Scanner — Engineering Bay
- Cryo Sample Vial — Observation Deck
- Plasma Torch — Maintenance Tunnel
- Access Card — Bio Lab
- EMP Device Core — Server Room
These items form the core progression gating system and determine the outcome of the final encounter.

----------------

## Architectural Features
* Fully modular design dividing world, player state, events, and UI into separate modules 
* Explicit state management (visited rooms, inventory, progression requirements)
* Clear input/output loop with centralized command routing 
* Defensive progression design preventing sequence breaks 
* Extensible structure supporting new rooms, puzzles, and event types without modifying the core loop

----------------

## Potential enhancements include:
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
This project was created as both a learning exercise and a portfolio artifact, focusing on modular Python programming, state-driven design, and foundational game architecture. It serves as a base for building more advanced interactive fiction systems while demonstrating clean, maintainable code and thoughtful game structure. 

Contributions and suggestions are welcome—feel free to fork the repository and expand the station’s world or narrative.

----------------

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
© 2025 ekdoestech

----------------

## Acknowledgements
Inspired by classic text adventures, atmospheric sci-fi narratives, and modern interactive fiction engines.
Developed for SNHU coursework and personal exploration of game architecture.

----------------

## Contact
For questions or contributions, please reach out via GitHub or email:
- GitHub: **ekdoestech**
- Email: **ek.does.tech@gmail.com**

----------------

# Enjoy the adventure, and may you outwit The Marrow!
