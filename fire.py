class Farmer:
    def __init__(self, id, location):
        self.id = id
        self.location = location
        self.free = True

    def nb_farmers_on_field(farmers, location):
        compteur = 0
        for farmer in farmers:
            if farmer.location == location:
                compteur += 1
        return compteur

    def farmers_state_field(farmers, free):
        compteur = 0
        for farmer in farmers:
            if farmer.state == free:
                compteur += 1
        return compteur
