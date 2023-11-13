class Farmer:

    def __init__(self, id, field):
        self.id = id
        self.field = field
        
    def farmers_in_field_1(self, id, field):
        field.farmers = Farmer(2, 1)


def nb_farmers_on_field(farmers, field):
    compteur = 0
    for farmer in farmers:
        if farmer.field == field:
            compteur += 1
    return compteur
