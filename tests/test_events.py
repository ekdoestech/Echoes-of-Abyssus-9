import pytest

from events import handle_final_event
from player import Player


# noinspection PyUnusedLocal
def test_final_event_success_with_item_ids(capsys):
    player = Player(starting_room="Control Center")
    player.inventory.extend(["override_alpha", "override_beta"])

    outcome = handle_final_event(
        player,
        required_item_ids=["override_alpha", "override_beta"],
    )

    assert outcome == "SUCCESS"


# noinspection PyUnusedLocal
def test_final_event_failure_missing_items(capsys):
    player = Player(starting_room="Control Center")
    player.inventory.append("override_alpha")

    outcome = handle_final_event(
        player,
        required_item_ids=["override_alpha", "override_beta"],
    )

    assert outcome == "FAILURE"


def test_final_event_invalid_arguments():
    player = Player(starting_room="Control Center")

    with pytest.raises(ValueError):
        handle_final_event(player)
