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

from events import handle_final_event
from player import Player
from utils import (
    normalize_direction,
    print_move_success,
    print_move_failure,
    print_room_description,
)
from world import get_room_description, REQUIRED_ITEMS

__all__ = ["main"]

# Room that triggers the final encounter
GAME_OVER_ROOM = "Control Center"


# ---------------------------------------------------------------------------
# Main Game Loop
# ---------------------------------------------------------------------------

def main() -> None:
    """
    Entry point for the Echoes of Abyssus-9 adventure.

    Initializes the player, processes commands, handles room transitions,
    and triggers the endgame event when the final room is reached.
    """
    player = Player(starting_room="Docking Bay")

    print("\n*** Welcome to Echoes of Abyssus-9 ***")
    print("Type 'go <direction>' to move or 'quit' to exit.\n")

    # ----------------------------------------------------------------------
    # Primary Gameplay Loop
    # ----------------------------------------------------------------------
    while player.current_room != GAME_OVER_ROOM:
        print(f"\nYou are in the {player.current_room}.")
        print_room_description(get_room_description(player.current_room))

        command = input("> ").strip().lower()

        # --------------------------------------------------------------
        # Movement Commands
        # --------------------------------------------------------------
        if command.startswith("go "):
            raw_direction = command[3:]
            direction = normalize_direction(raw_direction)

            destination = player.move(direction)
            if destination:
                player.current_room = destination
                print_move_success(direction, destination)

                # Print room description
                print_room_description(get_room_description(player.current_room))

                # Auto-collect items
                item = player.collect_item()
                if item:
                    print(f"You picked up: {item}")

            else:
                print_move_failure(direction)

        # --------------------------------------------------------------
        # Quit Command
        # --------------------------------------------------------------
        elif command == "quit":
            print("\nMission aborted. Exiting Abyssus-9.")
            return

        # --------------------------------------------------------------
        # Invalid Command Handler
        # --------------------------------------------------------------
        else:
            print("Invalid command. Try 'go <direction>' or 'quit'.")

    # ----------------------------------------------------------------------
    # Endgame Sequence
    # ----------------------------------------------------------------------
    outcome = handle_final_event(player, REQUIRED_ITEMS)

    print(
        "\n*** Mission Summary ***\n"
        f"Items Collected: {player.inventory}\n"
        f"Total Items: {len(player.inventory)} / {REQUIRED_ITEMS}\n"
        f"Outcome: {outcome}\n"
        "------------------------\n"
        "Thank you for playing Echoes of Abyssus-9.\n"
    )

# ---------------------------------------------------------------------------
# Module Entrypoint
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    main()
