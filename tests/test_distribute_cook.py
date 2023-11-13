from notre_ferme.game import Game


def test_distribute_cook_function():
    instance = Game()
    instance.distribute_cook()

    expected_commands = ["31 CUISINER", "32 CUISINER", "33 CUISINER", "34 CUISINER"]
    if instance.commands == expected_commands:
        print("La méthode distribute_cook a réussi le test.")
    else:
        print(
            "La méthode distribute_cook a échoué. Les commandes ne sont pas correctes."
        )
