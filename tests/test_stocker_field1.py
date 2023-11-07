from game import Game


def test_stocker_field1_function():
    instance = Game()

    # Cas où les conditions sont remplies
    result = instance.stocker_field1("PATATE", 0, 35, "FARM", False)
    expected_commands = ["35 STOCKER 1 1"]
    if result and instance.commands == expected_commands:
        print(
            "La méthode stocker_field1 a réussi le test pour les conditions remplies."
        )
    else:
        print("La méthode stocker_field1 a échoué pour les conditions remplies.")

    # Cas où les conditions ne sont pas remplies
    result = instance.stocker_field1("NONE", 1, 35, "SOUP_FACTORY", False)
    if not result and len(instance.commands) == 0:
        print("La méthode stocker_field1 a réussi le test si pas remplie.")
    else:
        print("La méthode stocker_field1 a échoué pour les conditions non remplies.")
