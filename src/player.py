"""
player.py
=========
Defines the Player class for *Echoes of Abyssus-9*.

Responsibilities:
- Track the player's current room and inventory
- Provide validated movement logic
- Handle item collection in coordination with world/item data

This module does not contain the game loop. It interacts with the world
structure abstractly and leaves UI rendering to higher-level modules.
"""

from __future__ import annotations

from world import get_exits
from utils import normalize_direction
from items import get_room_item, set_room_item

__all__ = ["Player"]


# ---------------------------------------------------------------------------
# Player Class
# ---------------------------------------------------------------------------

class Player:
    """
    Represents the active player navigating the station.

    Tracks:
        - Current room location
        - Inventory contents

    Movement validation is performed using world data. Item collection updates
    world state via helper functions defined in items.py.
    """

    def __init__(self, starting_room: str):
        """
        Initialize a new player at the given starting room.

        Args:
            starting_room (str): Name of the initial room.
        """
        self.current_room: str = starting_room
        self.inventory: list[str] = []

    # ----------------------------------------------------------------------
    # Movement
    # ----------------------------------------------------------------------

    def move(self, direction: str) -> str | None:
        """
        Attempt to move the player in the specified direction.

        Args:
            direction (str): User-entered direction (any case, extra spacing allowed).

        Returns:
            str | None:
                - The destination room name if movement is valid.
                - None if no valid exit exists in that direction.
        """
        normalized = normalize_direction(direction)
        exits = get_exits(self.current_room)
        return exits.get(normalized)

    # ----------------------------------------------------------------------
    # Item Collection
    # ----------------------------------------------------------------------

    def collect_item(self) -> str | None:
        """
        Attempt to collect the item in the player's current room.

        Returns:
            str | None:
                - The name of the collected item, if successful.
                - None if the room contains no item.
        """
        item = get_room_item(self.current_room)

        if item is None:
            return None

        self.inventory.append(item)
        set_room_item(self.current_room, None)  # Item removed from the world
        return item
