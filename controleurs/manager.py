#from calendar import c
from logging.config import listen
from tinydb import TinyDB, Query, where

class Manager:

    def __init__(self):
        self.db = TinyDB('mydb.json')

            
    def afficher_tournoi(self):
        db = self.db
        table_tournoi = db.table('tournoi')
        liste_tournois = table_tournoi.all()
        return liste_tournois

    def recuperer_joueur(self):
        db = self.db
        table_joueurs = db.table('joueurs')
        liste_joueurs = table_joueurs.all()
        return liste_joueurs
    
    def recuperer_joueur_tournoi(self, index_joueurs):
        db = self.db
        table_joueurs = db.table('joueurs')
        Joueur = Query()
        liste_joueurs = table_joueurs.search(Joueur.index.any(index_joueurs))
        return liste_joueurs

    def search_tournoi_index(self, index_tournoi):
        db = self.db
        table_tournoi = db.table('tournoi')
        Tournoi = Query()
        result = table_tournoi.search(Tournoi.index == index_tournoi)
        #liste_joueurs_tournoi = result[0]["index_joueurs"]
        #return liste_joueurs_tournoi
        return result

    def search_tournoi(self, nom_tournoi):
        db = self.db
        table_tournoi = db.table('tournoi')
        Tournoi = Query()
        result = table_tournoi.search(Tournoi.nom == nom_tournoi)
        return result
    
    def delete_tournoi(self, nom_tournoi):
        db = self.db
        table_tournoi = db.table('tournoi')
        table_tournoi.remove(where('nom') == nom_tournoi)

    def recuperer_tours(self, index_tournoi):
        db = TinyDB('mydb.json')
        table_tours = db.table('tours')
        Tours = Query()
        result = table_tours.search(Tours.index_tournoi == index_tournoi)
        return result
    
    def update_joueur(self, nom_joueur, classement):
        db = self.db
        table_joueurs = db.table('joueurs')
        joueur_query = Query()
        #result = table_joueurs.search(joueur_query.nom == nom_joueur)
        #print(result)
        table_joueurs.update({'classement': classement}, joueur_query.nom == nom_joueur)
        