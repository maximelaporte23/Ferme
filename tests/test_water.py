from location import Location
from field import Field


#class TestArroserMethod:
#    def test_arroser_unwatered_field(self):
#        field = Field(Location.FIELD1)  # Champ 1 créer pour arroser
#        assert (
#            field.needed_water == 0
#        )  # Normalement le champ à pas besoin d'eau au début
#        assert field.watered is False  # Normalement le champ n'a pas été arrosé

#        field.arroser()  # Arrosez le champ
#        assert field.needed_water == 1  # On a besoin de 1 d'eau pour l'instant
#        assert field.watered is True  # Si le champ arrosé le champ passe en True

#    def test_arroser_already_watered_field(self):
#        field = Field(Location.FIELD1)  # Champ 1 déjà arrosé
#        field.watered = True  # Dire que le champ est déjà arrosé
#        field.needed_water = (
#            2  # Mettre une valeur au hasard pour simuler un besoin d'eau
#        )

#        field.arroser()  # Essayer d'arroser le champ déjà arrosé
#        assert (
#            field.needed_water == 2
#        )  # Normalement need_water ne devrait pas changé vu qu'il est déjà arrosé
#        assert field.watered is True  # Donc water devrait toujours être True
