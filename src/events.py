"""
events.py
=========
Event handling for *Echoes of Abyssus-9*.

This module centralizes narrative text, defines standardized outcome types,
and provides reusable event handlers such as the final encounter sequence.

Responsibilities:
- Provide narrative text constants for major game events
- Expose clearly defined event functions (e.g., final encounter)
- Return standardized outcome codes so game.py can react accordingly

This module contains no gameplay loop or world data.
"""

from __future__ import annotations
from typing import Literal
from player import Player


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

Outcome = Literal["SUCCESS", "FAILURE"]

__all__ = [
    "handle_final_event",
    "Outcome",
]


# ---------------------------------------------------------------------------
# Narrative Text Constants
# These strings keep narrative data separate from event logic for clarity,
# maintainability, and potential future expansion.
# ---------------------------------------------------------------------------

INTRO_MESSAGE = """
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
# Core Event Handlers
# ---------------------------------------------------------------------------

def handle_final_event(player: Player, required_items: int) -> Outcome:
    """
    Execute the final encounter inside the Control Center.

    The player succeeds only if they have collected the required number of
    progression items. Otherwise, The Marrow defeats them.

    Args:
        player (Player): The active player instance.
        required_items (int): Number of items required for success.

    Returns:
        Outcome: "SUCCESS" if the player wins, "FAILURE" otherwise.
    """
    print(INTRO_MESSAGE)

    has_all_items = len(player.inventory) >= required_items

    if has_all_items:
        print(VICTORY_MESSAGE)
        return "SUCCESS"

    print(FAILURE_MESSAGE)
    return "FAILURE"
