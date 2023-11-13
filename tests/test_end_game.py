from notre_ferme.game import Game


def test_end_game_function():
    instance = Game()
    instance.end_game()

    expected_commands = [
        "40 CUISINER",
        "41 CUISINER",
        "42 CUISINER",
        "43 CUISINER",
        "44 CUISINER",
        "45 CUISINER",
        "46 CUISINER",
        "47 CUISINER",
        "48 CUISINER",
        "49 CUISINER",
        "50 CUISINER",
        "51 CUISINER",
        "52 CUISINER",
        "53 CUISINER",
        "54 CUISINER",
        "55 CUISINER",
        "56 CUISINER",
        "57 CUISINER",
        "58 CUISINER",
        "59 CUISINER",
    ]

    if instance.commands == expected_commands:
        print("La méthode end_game a réussi le test.")
    else:
        print("La méthode end_game a échoué. Les commandes ne sont pas correctes.")
