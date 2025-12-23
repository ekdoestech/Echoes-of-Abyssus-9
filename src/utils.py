"""
utils.py
========
Utility helpers for *Echoes of Abyssus-9*.

This module provides functions for:
- Normalizing player input
- Displaying movement feedback
- Rendering room descriptions and available exits

These helpers contain no game logic or state manipulation. Their purpose
is to keep UI-related output clean, consistent, and separate from core
game systems.
"""

from __future__ import annotations
from collections.abc import Mapping

__all__ = [
    "normalize_direction",
    "print_move_success",
    "print_move_failure",
    "print_room_description",
    "describe_exits",
]


# ---------------------------------------------------------------------------
# Input Normalization
# ---------------------------------------------------------------------------

def normalize_direction(direction: str) -> str:
    """
    Normalize user-entered movement directions.

    Examples:
        "NORTH" -> "north"
        "East" -> "east"

    Args:
        direction (str): Raw user input for a direction.

    Returns:
        str: Normalized lowercase direction string.
    """
    return direction.strip().lower()


# ---------------------------------------------------------------------------
# Movement Feedback Output
# ---------------------------------------------------------------------------

def print_move_success(direction: str, room: str) -> None:
    """
    Display a message when the player successfully moves into a room.

    Args:
        direction (str): Normalized direction the player moved.
        room (str): Destination room name.
    """
    print(f"You move {direction} into the {room}.")


def print_move_failure(direction: str) -> None:
    """
    Display an error message when movement in a direction is not allowed.

    Args:
        direction (str): Normalized attempted direction.
    """
    print(f"You can't go {direction} from here.")


# ---------------------------------------------------------------------------
# Room Description & Exit Output
# ---------------------------------------------------------------------------

def print_room_description(description: str) -> None:
    """
    Display a room's narrative description, if defined.

    Args:
        description (str): Text describing the room.
    """
    if description:
        print(f"\n{description}\n")


def describe_exits(exits: Mapping[str, str]) -> None:
    """
    Display the available exits from the current room.

    Args:
        exits (dict[str, str]): Mapping of direction -> destination room.
    """
    if not exits:
        return

    directions = sorted(exits)

    if len(directions) == 1:
        print(f"A corridor leads {directions[0]}.")
    else:
        print(f"Corridors lead {', '.join(directions)}.")
