from notre_ferme.game import Game


def test_water_with_need_water_1():
    game = Game()
    farmer_id = 5

    game.water(1, 0, 0, 0, 0, farmer_id)
    commands = game.commands

    expected_commands = [f"{farmer_id} ARROSER 1"]

    assert commands == expected_commands, "Le test a échoué avec need_water_1."


def test_water_with_need_water_2():
    game = Game()
    farmer_id = 10

    game.water(0, 1, 0, 0, 0, farmer_id)
    commands = game.commands

    expected_commands = [f"{farmer_id} ARROSER 2"]

    assert commands == expected_commands, "Le test a échoué avec need_water_2."


def test_water_with_no_need_water():
    game = Game()
    farmer_id = 20

    game.water(0, 0, 0, 0, 0, farmer_id)
    commands = game.commands

    expected_commands = []

    assert commands == expected_commands, "Le test a échoué sans besoin d'eau."
