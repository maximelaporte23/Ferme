from game import Game


def test_cook_function():
    instance = Game()
    instance.cook()

    expected_commands = ["31 CUISINER", "32 CUISINER", "33 CUISINER", "34 CUISINER"]
    if instance.commands == expected_commands:
        print("La fonction cook a réussi le test.")
    else:
        print("La fonction cook a échoué. Les commandes ne sont pas correctes.")
