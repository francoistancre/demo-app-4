# from tinydb import TinyDB, Query, where
from tinydb import TinyDB


class Joueur:
    # Implementer un constructeur
    # On crée toujours les variables d'instance dans le constructeur
    def __init__(
        self,
        index: int = 0,
        nom: str = "",
        prenom: str = "",
        date_naissance: str = "",
        sexe: str = "",
        classement: int = 0,
        score: int = 0,
    ):
        self.index = index
        self.nom = nom  # crée une variable d'instance
        self.prenom = prenom  # crée une variable d'instance
        self.date_naissance = date_naissance  # crée une variable d'instance
        self.sexe = sexe  # crée une variable d'instance
        self.classement = classement  # crée une variable d'instance
        self.score = score

    def presenter_joueur(self):
        print("***** NOUVEAU JOUEUR *****")
        print("Index: ", self.index)
        print("Nom : ", self.nom)
        print("Prénom : ", self.prenom)
        print("Date de naissance : ", self.date_naissance)
        print("Sexe : ", self.sexe)
        print("Classement : ", str(self.classement))

    def serialized(self):
        serialized_joueur = {
            "index": self.index,
            "nom": self.nom,
            "prenom": self.prenom,
            "date_naissance": self.date_naissance,
            "sexe": self.sexe,
            "classement": self.classement,
            "score": self.score,
        }
        return serialized_joueur

    def save_joueur(self):
        joueur = self.serialized()
        print(joueur)

        db = TinyDB("mydb.json")
        joueurs_table = db.table("joueurs")
        joueurs_table.insert(joueur)
