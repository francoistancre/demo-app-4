# from tinydb import TinyDB, Query, where
from tinydb import TinyDB


class Tournoi:
    # Implementer un constructeur
    # On crée toujours les variables d'instance dans le constructeur
    def __init__(
        self,
        index,
        nom,
        lieu,
        nombre_de_tours,
        tournee,
        joueurs_tournoi,
        index_joueurs,
        controle_temps,
        description,
    ):
        self.index = index
        self.nom = nom
        self.lieu = lieu
        self.nombre_de_tours = nombre_de_tours
        self.tournee = tournee
        self.joueurs_tournoi = joueurs_tournoi
        self.index_joueurs = index_joueurs
        self.controle_temps = controle_temps
        self.description = description

    def presenter_tournoi(self):
        print("***** NOUVEAU TOURNOI *****")
        print("Index : ", self.index)
        print("Nom : ", self.nom)
        print("Lieu : ", self.lieu)
        print("Nombre de tours: " + str(self.nombre_de_tours))
        print("Tournées : ", self.tournee)
        print("Joueurs : ", self.index_joueurs)
        print("Contrôle du temps : ", self.controle_temps)
        print("Description : ", self.description)
        print("***************************")

    def serialized(self):
        serialized_tournoi = vars(self)
        # print(serialized_tournoi)
        return serialized_tournoi

    def save_tournoi(self):
        tournoi = self.serialized()
        print("Le tournoi a été sauvegardé")

        db = TinyDB("mydb.json")
        tournoi_table = db.table("tournoi")
        tournoi_table.insert(tournoi)
