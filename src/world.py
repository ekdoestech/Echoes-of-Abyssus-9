"""
world.py
========
Defines the world layout and room metadata for *Echoes of Abyssus-9*.

This module provides:
- The station's room graph (valid movement directions)
- Narrative descriptions displayed when entering each room
- Helper functions for querying room exits and descriptions

The world is intentionally static and data-driven. Gameplay logic,
event triggers, and player state are handled elsewhere.
"""

from __future__ import annotations

from collections.abc import Mapping

__all__ = [
    "ROOM_CONNECTIONS",
    "ROOM_DESCRIPTIONS",
    "get_exits",
    "get_room_description",
]

# ---------------------------------------------------------------------------
# Room Graph
# ---------------------------------------------------------------------------

ROOM_CONNECTIONS: Mapping[str, Mapping[str, str]] = {
    "Docking Bay": {
        "north": "Main Hall",
    },
    "Main Hall": {
        "south": "Docking Bay",
        "east": "Engineering Bay",
        "west": "Security Office",
        "north": "Observation Deck",
    },
    "Engineering Bay": {
        "west": "Main Hall",
    },
    "Security Office": {
        "east": "Main Hall",
    },
    "Observation Deck": {
        "south": "Main Hall",
        "east": "Bio Lab",
    },
    "Bio Lab": {
        "west": "Observation Deck",
        "north": "Maintenance Tunnel",
    },
    "Maintenance Tunnel": {
        "south": "Bio Lab",
        "north": "Server Room",
    },
    "Server Room": {
        "south": "Maintenance Tunnel",
        "north": "Control Center",
    },
    # Final room: no exits from the Control Center.
    "Control Center": {},
}

# ---------------------------------------------------------------------------
# Room Descriptions
# ---------------------------------------------------------------------------

ROOM_DESCRIPTIONS: Mapping[str, str] = {
    "Docking Bay": "The bay is eerily silent. Emergency lights pulse softly.",
    "Main Hall": "A long corridor with cables hanging from the ceiling.",
    "Engineering Bay": "Tools and consoles spark intermittently. Something burned recently.",
    "Security Office": "Monitors flicker with distorted camera feeds.",
    "Observation Deck": "Glass panels reveal the stars drifting beyond the station.",
    "Bio Lab": "Broken vials litter the floor. Something hissed moments ago.",
    "Maintenance Tunnel": "Dim lights barely illuminate the narrow passage ahead.",
    "Server Room": "Racks of servers hum erratically. The air feels charged.",
    "Control Center": "Screens glow softly. The presence of The Marrow is overwhelming here.",
}

# ---------------------------------------------------------------------------
# Public Helper Functions
# ---------------------------------------------------------------------------

def get_exits(room: str) -> Mapping[str, str]:
    """
    Return the available exits for a given room.

    Args:
        room (str): Name of the room.

    Returns:
        Mapping[str, str]: Direction -> destination room mapping.
    """
    return ROOM_CONNECTIONS.get(room, {})


def get_room_description(room: str) -> str:
    """
    Return the narrative description for a given room.

    Args:
        room (str): Name of the room.

    Returns:
        str: Description text, or an empty string if the room has no description.
    """
    return ROOM_DESCRIPTIONS.get(room, "")
