from vues.joueur import JoueurVue
from vues.rapport import RapportVue
from modeles.joueur import Joueur
from controleurs.manager import Manager

class JoueurControleur:

    def __init__(self):
        self.joueur_vue = JoueurVue()
        self.manager = Manager()
        self.rapport_vue = RapportVue()
        pass

    #le controleur execute joueur.vue pour recuperer les données
    def run(self):
        self.create_player()
    
    def create_player(self):
        joueur = self.joueur_vue.get_user_data()
        joueur = Joueur(joueur['index'], 
            joueur['nom'],
            joueur['prenom'],
            joueur['date_naissance'],
            joueur['sexe'],
            joueur['classement']
            )
        #joueur = joueur.serialized()
        #print(joueur)

        joueur.save_joueur()

    def afficher_joueur(self):
        liste_joueurs = self.manager.recuperer_joueur()
        print(liste_joueurs)

    def modifier_classement_joueur(self):
        liste_joueurs = self.manager.recuperer_joueur()
        choix_joueur,classement = self.joueur_vue.get_choix_joueur(liste_joueurs)
        self.manager.update_joueur(choix_joueur,classement)
        #print("Le tournoi " + choix_tournoi + " a été supprimé")

    def rapport_liste_joueur(self, ordre):
        liste_joueurs = self.manager.recuperer_joueur()
        liste_joueurs_sorted = []
        if ordre == "alphabetique":
            liste_joueurs_sorted = sorted(liste_joueurs, key=lambda d: d['nom'], reverse=False)
            self.rapport_vue.get_rapport_data(liste_joueurs_sorted, "Liste des joueurs par ordres alphabétique")
        elif ordre == "classement":
            liste_joueurs_sorted = sorted(liste_joueurs, key=lambda d: d['classement'], reverse=True)
            self.rapport_vue.get_rapport_data(liste_joueurs_sorted, "Liste des joueurs par classement")
        #print(liste_joueurs_sorted)