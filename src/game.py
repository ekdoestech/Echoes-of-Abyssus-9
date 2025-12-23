"""
game.py
=======
Main game loop for *Echoes of Abyssus-9*.

Responsibilities:
- Initialize the player and starting state
- Process user commands and route them through the appropriate systems
- Handle movement, room transitions, and automatic item collection
- Trigger the final encounter when reaching the Control Center
- Display mission summary and exit cleanly

This module contains no world data or event definitions. It orchestrates
the game flow using helpers provided by other modules.
"""

from __future__ import annotations

from .events import handle_intro_event, handle_final_event
from .player import Player
from .utils import (
    normalize_direction,
    print_move_failure,
    print_move_success,
    print_room_description,
    describe_exits,
)
from .world import get_room_description, get_exits
from .items import ROOM_ITEMS

__all__ = ["main"]

# ---------------------------------------------------------------------------
# Progression Requirements
# ---------------------------------------------------------------------------

REQUIRED_ITEM_IDS = [item for item in ROOM_ITEMS.values() if item]

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

FINAL_ROOM = "Control Center"

QUIT_COMMAND = "quit"
MOVE_PREFIX = "go "
HELP_COMMAND = "help"

HELP_TEXT = (
    "Commands:\n"
    "- 'go <direction>' to move\n"
    "- 'help' for commands\n"
    "- 'quit' to exit"
)

# ---------------------------------------------------------------------------
# Main Game Loop
# ---------------------------------------------------------------------------

def main() -> None:
    """
    Entry point for the Echoes of Abyssus-9 adventure.
    """
    player = Player(starting_room="Docking Bay")

    # Display opening narrative and instructions
    handle_intro_event()

    while player.current_room != FINAL_ROOM:
        print(f"\nYou are in the {player.current_room}.")
        print_room_description(get_room_description(player.current_room))
        describe_exits(get_exits(player.current_room))

        command = input("> ").strip().lower()

        if command.startswith(MOVE_PREFIX):
            direction = normalize_direction(command[len(MOVE_PREFIX):])
            destination = player.move(direction)

            if destination:
                player.current_room = destination
                print_move_success(direction, destination)

                # Auto-collect items on room entry
                item = player.collect_item()
                if item:
                    print(f"You picked up: {item}")
            else:
                print_move_failure(direction)

        elif command == QUIT_COMMAND:
            print("\nMission aborted. Exiting Abyssus-9.")
            return

        elif command == HELP_COMMAND:
            print(HELP_TEXT)

        else:
            print("Invalid command. Try 'go <direction>' or 'quit'.")

    # ----------------------------------------------------------------------
    # Endgame Sequence
    # ----------------------------------------------------------------------

    outcome = handle_final_event(
        player,
        required_item_ids=REQUIRED_ITEM_IDS,
    )

    print(
        "\n*** Mission Summary ***\n"
        f"Items Collected: {player.inventory}\n"
        f"Total Items: {len(player.inventory)} / {len(REQUIRED_ITEM_IDS)}\n"
        f"Outcome: {outcome}\n"
        "------------------------\n"
        "Thank you for playing Echoes of Abyssus-9.\n"
    )


if __name__ == "__main__":
    main()
