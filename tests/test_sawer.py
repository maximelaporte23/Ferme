from game import Game


def test_distribute_sawer_function():
    instance = Game()
    instance.distribute_sawer()

    expected_commands = [
        "26 SEMER PATATE 1",
        "27 SEMER PATATE 2",
        "28 SEMER PATATE 3",
        "29 SEMER PATATE 4",
        "30 SEMER PATATE 5",
    ]

    if instance.commands == expected_commands:
        print("La méthode distribute_sawer a réussi le test.")
    else:
        print("Les commandes ne sont pas correctes.")
