
from .joueur import JoueurControleur #quand c'est dans le meme dossier
from .tournoi import TournoiControleur
from .tour import TourControleur
from vues.base import Vue

class Controleur:

    def __init__(self):
        self.new_joueur = JoueurControleur()
        self.new_tournoi = TournoiControleur()
        self.new_tour = TourControleur()
        #self.continue_tournoi = 
        self.new_vue = Vue()
  
    def run(self):
        
        #menu pour rentrer dans le programme
        choix = self.new_vue.menu_principale()  
        print(choix)
        if choix == 1:
            self.new_tournoi.create_tournoi()
        elif choix == 2:
            self.new_joueur.create_player()
        elif choix == 3:
            self.new_tournoi.continuer_tournoi()
        elif choix == 4:
            self.new_joueur.afficher_joueur()
        elif choix == 5:
            self.new_tour.afficher_tour()
        elif choix == 6:
            self.new_tournoi.supprimer_tournoi()
        elif choix == 7:
            self.new_joueur.modifier_classement_joueur()
        elif choix == 8:
            return self.run_rapports()
        return self.run()

    def run_rapports(self):
        choix = self.new_vue.menu_rapport()
        print(choix)
        if choix == 8:
            return self.run()
        elif choix == 1:
            self.new_joueur.rapport_liste_joueur("alphabetique")
        elif choix == 2:
            self.new_joueur.rapport_liste_joueur("classement")
        elif choix == 3:
            self.new_tournoi.rapport_joueurs_tournoi("alphabetique")
        elif choix == 4:
            self.new_tournoi.rapport_joueurs_tournoi("classement")    
        elif choix == 5:
            self.new_tournoi.rapport_liste_tournoi()
        elif choix == 6:
            self.new_tour.rapport_liste_tours()
        elif choix == 7:
            self.new_tour.rapport_liste_matchs()
        return self.run_rapports()