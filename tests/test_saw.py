from notre_ferme.game import Game


def test_saw_function():
    fields = [
        {"content": "NONE"},
        {"content": "PATATE"},
        {"content": "NONE"},
        {"content": "TOMATE"},
        {"content": "COURGETTE"},
    ]

    instance = Game()
    instance.saw(fields)

    expected_commands = [
        "26 SEMER PATATE 1",
        "27 SEMER TOMATE 2",
        "28 SEMER OIGNON 3",
        "29 SEMER COURGETTE 4",
        "30 SEMER POIREAU 5",
    ]

    if instance.commands == expected_commands:
        print("La méthode saw a réussi le test.")
    else:
        print("La méthode saw a échoué. Les commandes ne sont pas correctes.")
