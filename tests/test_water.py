from notre_ferme.game import Game


def test_water_function():
    instance = Game()
    instance.water(1, 0, 2, 0, 3, 4, "FIELD")

    expected_commands = [
        "4 ARROSER 1",
        "4 ARROSER 3",
        "4 ARROSER 3",
        "4 ARROSER 5",
        "4 ARROSER 5",
        "4 ARROSER 5",
    ]

    if instance.commands == expected_commands:
        print("La méthode water a réussi le test.")
    else:
        print("La méthode water a échoué. Les commandes ne sont pas correctes.")
