from field import Field
from location import Location


class TestCookMethod:
    def test_cook_with_full_stock(self):
        field = Field(Location.FARM)  # Créer le champ grâce à field fais par le BOSS
        stock = {
            "POTATO": 1,
            "LEEK": 1,
            "TOMATO": 1,
            "ONION": 1,
            "ZUCCHINI": 1,
        }

        # Appeler le cook nul de max avec stock
        field.cook(stock)

        # Voir si les commandes on été ajouté à la liste de commande
        assert len(field.commands) == 5  # La j'attend 5 commandes ajoutés

    def test_cook_with_empty_stock(self):
        field = Field(
            Location.FARM
        )  # Créer un champ correcte au bon endroit grâce à Field
        stock = {
            "POTATO": 0,
            "LEEK": 0,
            "TOMATO": 0,
            "ONION": 0,
            "ZUCCHINI": 0,
        }

        # Appeler le cook nul de max avec stock
        field.cook(stock)

        # On vérifie que rien n'a été ajouté à la liste de commande
        assert len(field.commands) == 0  # La rien n'a été ajouté
