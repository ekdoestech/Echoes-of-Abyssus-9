from player import Player


def test_player_initial_state():
    player = Player(starting_room="Docking Bay")

    assert player.current_room == "Docking Bay"
    assert player.inventory == []


def test_player_movement_success():
    player = Player(starting_room="Docking Bay")

    destination = player.move("north")

    assert destination is not None
    assert player.current_room == "Docking Bay"  # move() should not mutate state


def test_player_movement_failure():
    player = Player(starting_room="Docking Bay")

    destination = player.move("invalid_direction")

    assert destination is None


def test_player_collect_item():
    player = Player(starting_room="Docking Bay")

    item = player.collect_item()

    if item is not None:
        assert item in player.inventory
