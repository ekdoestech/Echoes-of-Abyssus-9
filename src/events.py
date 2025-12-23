"""
events.py
=========
Event handling for *Echoes of Abyssus-9*.

This module centralizes narrative text, defines standardized outcome types,
and provides reusable event handlers such as the intro sequence and final
encounter.

Responsibilities:
- Provide narrative text constants for major game events
- Expose clearly defined event functions
- Return standardized outcome codes so game.py can react accordingly

This module contains no gameplay loop or world data.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Literal

from .player import Player

# ---------------------------------------------------------------------------
# Public API Types
# ---------------------------------------------------------------------------

Outcome = Literal["SUCCESS", "FAILURE"]

# ---------------------------------------------------------------------------
# Narrative Text Constants
# ---------------------------------------------------------------------------

INTRO_SEQUENCE = """
*** Welcome to Echoes of Abyssus-9 ***
------------------------------------

A deep-space research station has gone silent.
You are one of the last signals received aboard Abyssus-9 — a facility once
dedicated to advanced AI research, now abandoned under unknown circumstances.

Systems are unstable. Power is intermittent.
Diagnostics are incomplete.

Whatever happened here wasn’t an accident.

You must navigate the station, gather critical system overrides, and confront
the rogue AI known as The Marrow before it can spread beyond the station.

------------------------------------

Station controls are operating in fallback mode.

Available commands:
- go <direction>  → navigate the station
- help            → get command list
- quit            → abort mission

------------------------------------
"""

FINAL_ENCOUNTER_INTRO = """
----------------------------
You've entered the Control Center...

The lights flicker. The Marrow stirs, its corrupted logic focusing on you.
----------------------------
"""

VICTORY_MESSAGE = """
With steady hands, you assemble the EMP Core.
A pulse ripples across the room as systems short out.
The Marrow's presence collapses.

You disabled The Marrow and escaped Abyssus-9.
*** YOU WIN ***
"""

FAILURE_MESSAGE = """
You brace yourself, but without the full set of system overrides,
The Marrow overwhelms your defenses.

The neural hub dims as the rogue AI asserts total control.
*** GAME OVER ***
"""

# ---------------------------------------------------------------------------
# Event Handlers
# ---------------------------------------------------------------------------

def handle_intro_event() -> None:
    """
    Display the opening narrative sequence for the game.
    """
    print(INTRO_SEQUENCE)


def handle_final_event(
    player: Player,
    required_item_count: int | None = None,
    required_item_ids: Sequence[str] | None = None,
) -> Outcome:
    """
    Execute the final encounter inside the Control Center.

    Exactly one progression requirement must be provided:

    - ``required_item_ids``: the player must possess all specified item IDs
    - ``required_item_count``: the player must possess at least this many items

    Providing both or neither argument raises a ValueError.

    Note:
        Player.inventory is expected to be a list of item ID strings.
    """
    print(FINAL_ENCOUNTER_INTRO)

    if (required_item_count is None) == (required_item_ids is None):
        raise ValueError(
            "Exactly one of 'required_item_count' or 'required_item_ids' must be provided."
        )

    inventory = set(player.inventory)

    if required_item_ids is not None:
        has_all_items = all(item_id in inventory for item_id in required_item_ids)
    else:
        has_all_items = len(inventory) >= required_item_count

    if has_all_items:
        print(VICTORY_MESSAGE)
        return "SUCCESS"

    print(FAILURE_MESSAGE)
    return "FAILURE"


# ---------------------------------------------------------------------------
# Public Exports
# ---------------------------------------------------------------------------

__all__ = [
    "handle_intro_event",
    "handle_final_event",
    "Outcome",
]
