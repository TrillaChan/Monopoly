from propriete import Propriete 

class Terrain(Propriete):
    def __init__(self, prix_achat, nom, loyers):
        super().__init__(prix_achat, nom)
        self.__loyers = loyers
        self.__nbMaisons = 0
