# Echoes of Abyssus-9 — Architecture Overview

Echoes of Abyssus-9 is a modular, state-driven Python application designed to
enforce clear separation between game flow, world data, player state, and
narrative events.

- `game.py` orchestrates the main loop and routes user commands
- `player.py` manages player state, inventory, and movement
- `world.py` defines the room graph, navigation rules, and progression item identifiers
- `items.py` manages item placement and item-related world state
- `events.py` centralizes narrative text and progression-based outcomes
- `utils.py` provides input normalization and UI output helpers

Narrative events are treated as first-class systems, allowing progression
logic and story outcomes to evolve independently of the main gameplay loop.

## State & Progression Design

Player progression is governed explicitly by inventory state rather than
implicit sequencing or room order. The endgame condition checks for the
presence of required progression items, preventing premature completion
and sequence breaks.

This approach allows the world layout to remain flexible while enforcing
clear progression rules through state validation rather than control flow.

## Command Flow Overview

The main game loop reads user input, normalizes commands, and routes them
through a centralized command parser. Movement commands are validated against
world-defined exits, while progression and narrative outcomes are handled
by dedicated event handlers.

This structure keeps input handling, state mutation, and narrative logic
decoupled while maintaining a simple, readable control flow.

## Extensibility Notes

- New rooms, connections, and descriptions can be added by extending
  world data without modifying the game loop.
- Additional progression rules or endings can be introduced by expanding
  event handlers and required state checks.
- New command types (e.g., puzzles, interactions) can be added by extending
  the command routing logic without impacting existing systems.
