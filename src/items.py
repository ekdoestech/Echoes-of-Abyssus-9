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

from collections.abc import Mapping

__all__ = [
    "ROOM_ITEMS",
    "ITEM_DISPLAY_NAMES",
    "get_room_item",
    "set_room_item",
]


# ---------------------------------------------------------------------------
# Item Placement
# ---------------------------------------------------------------------------
# Maps rooms to item identifiers (or None if no item remains).
# Item identifiers must align with REQUIRED_ITEM_IDS defined in world.py.
# ---------------------------------------------------------------------------

ROOM_ITEMS: dict[str, str | None] = {
    "Security Office": "override_alpha",
    "Engineering Bay": "override_beta",
    "Observation Deck": "override_gamma",
    "Maintenance Tunnel": "override_delta",
    "Bio Lab": "override_epsilon",
    "Server Room": "override_zeta",
}


# ---------------------------------------------------------------------------
# Item Metadata
# ---------------------------------------------------------------------------
# Human-readable display names for item identifiers.
# ---------------------------------------------------------------------------

ITEM_DISPLAY_NAMES: Mapping[str, str] = {
    "override_alpha": "Circuit Override Key",
    "override_beta": "Engineering Scanner",
    "override_gamma": "Cryo Sample Vial",
    "override_delta": "Plasma Torch",
    "override_epsilon": "Access Card",
    "override_zeta": "EMP Device Core",
}


# ---------------------------------------------------------------------------
# Item Query Functions
# ---------------------------------------------------------------------------

def get_room_item(room: str) -> str | None:
    """
    Return the item identifier located in the given room.

    Args:
        room (str): Name of the room.

    Returns:
        str | None: Item identifier if present, otherwise None.
    """
    return ROOM_ITEMS.get(room)


def set_room_item(room: str, item: str | None) -> None:
    # noinspection GrazieStyle
    """
        Update the item identifier stored in a room.

        Used when collecting or placing items.

        Args:
            room (str): Name of the room.
            item (str | None): New item identifier, or None to clear the room.

        Raises:
            KeyError: If the room does not exist in ROOM_ITEMS.
        """
    if room not in ROOM_ITEMS:
        raise KeyError(f"Room '{room}' does not exist in ROOM_ITEMS.")

    ROOM_ITEMS[room] = item
