"""
items.py
========
Defines item placement and item-management helpers for *Echoes of Abyssus-9*.

Responsibilities:
- Track which items are located in which rooms
- Provide helper functions for retrieving and updating item state
- Keep item logic separate from player logic and world navigation

This module contains no game loop logic or print statements.
"""

from __future__ import annotations

__all__ = [
    "ROOM_ITEMS",
    "get_room_item",
    "set_room_item",
]


# ---------------------------------------------------------------------------
# Item Placement
# ---------------------------------------------------------------------------
# Maps rooms to the item located there (or None if no item remains).
#
# NOTE:
# These names must match the progression items expected by the game logic.
# ---------------------------------------------------------------------------

ROOM_ITEMS: dict[str, str | None] = {
    "Security Office": "Circuit Override Key",
    "Engineering Bay": "Engineering Scanner",
    "Observation Deck": "Cryo Sample Vial",
    "Maintenance Tunnel": "Plasma Torch",
    "Bio Lab": "Access Card",
    "Server Room": "EMP Device Core",
}


# ---------------------------------------------------------------------------
# Item Query Functions
# ---------------------------------------------------------------------------

def get_room_item(room: str) -> str | None:
    """
    Return the item located in the given room.

    Args:
        room (str): Name of the room.

    Returns:
        str | None: The item in the room, or None if empty.
    """
    return ROOM_ITEMS.get(room)


def set_room_item(room: str, item: str | None) -> None:
    """
    Update the item in a room. Used when collecting or placing items.

    Args:
        room (str): Name of the room.
                                    item (str | None): New item, or None to clear the room.
    Raises:
        KeyError: If the room does not exist in ROOM_ITEMS.
        :param room:
        :param item:
    """
    if room not in ROOM_ITEMS:
        raise KeyError(f"Room '{room}' does not exist in ROOM_ITEMS.")
    ROOM_ITEMS[room] = item
