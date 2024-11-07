class Propriete:
    def __init__(self, prix_achat, nom):
        self.__prix_achat = prix_achat
        self.__nom = nom
        self.__hypothequer = False

    def prix_hypotheque(self):
        return self.prix_achat/2

    @property
    def nom(self):
        return self.__nom

    @property
    def prix_achat(self):
        return self.__prix_achat
    
    @property
    def hypothequer(self):
        return self.__hypothequer
    
    @hypothequer.setter
    def hypothequer(self, value):
        self.__hypothequer = value

    @property
    def prix_hypotheque(self):
        return self.prix_achat/2
    
    def __str__(self):
        return (f"{self.__nom} :({self.prixAchat}e)")

if __name__ == '__main__':
        ruePaix = Propriete(400,"Rue de la Paix")
        print(ruePaix.prix_achat)
        print(ruePaix.nom)
        ruePaix.nom = "Av des Champs Elysées"




