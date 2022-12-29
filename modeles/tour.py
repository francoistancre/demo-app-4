# from tinydb import TinyDB, Query, where
from tinydb import TinyDB


class Tour:
    def __init__(self, index, index_tournoi, name, matchs, date_debut, date_fin):
        self.index = index
        self.index_tournoi = index_tournoi
        self.name = name
        self.matchs = matchs
        self.date_debut = date_debut
        self.date_fin = date_fin

    def serialized(self):
        serialized_tours = {
            "index": self.index,
            "index_tournoi": self.index_tournoi,
            "nom": self.name,
            "matchs": self.matchs,
            "date_debut": self.date_debut,
            "date_fin": self.date_fin,
        }
        return serialized_tours

    def save_tours(self):
        tours = self.serialized()
        print("Le tour a été sauvegardé")

        db = TinyDB("mydb.json")
        tours_table = db.table("tours")
        tours_table.insert(tours)
