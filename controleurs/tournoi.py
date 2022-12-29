from vues.tournoi import TournoiVue
from vues.rapport import RapportVue
from modeles.tournoi import Tournoi
from controleurs.manager import Manager

# from modeles.tour import Tour
from .tour import TourControleur


class TournoiControleur:
    def __init__(self):
        self.tournoi_vue = TournoiVue()
        self.manager = Manager()
        self.tour = TourControleur()
        self.rapport_vue = RapportVue()

    # le controleur execute tournoi.vue pour recuperer les données
    def run(self):
        self.create_tournoi()

    def create_tournoi(self):
        liste_joueurs = self.manager.recuperer_joueur()
        tournoi = self.tournoi_vue.get_tournoi_data(liste_joueurs)
        index_tournoi = tournoi["index_tournoi"]
        index_joueurs = tournoi["index_joueurs"]

        tournoi = Tournoi(
            tournoi["index_tournoi"],
            tournoi["nom_tournoi"],
            tournoi["lieu_tournoi"],
            tournoi["nombre_tours"],
            tournoi["tournee"],
            tournoi["joueurs_tournoi"],
            tournoi["index_joueurs"],
            tournoi["controle_temps"],
            tournoi["description"],
        )

        tournoi.save_tournoi()
        choix_tour = input("Voulez-vous commencer le premier tour ? y/n")
        if choix_tour == "y":
            self.tour.tour_1(index_tournoi, index_joueurs)

    def continuer_tournoi(self):
        liste_tournois = self.manager.afficher_tournoi()
        choix_tournoi = self.tournoi_vue.get_choix_tournoi(liste_tournois)
        # print(choix_tournoi)
        search_tournoi = self.manager.search_tournoi(choix_tournoi)
        # print(search_tournoi)
        index_tournoi = search_tournoi[0]["index"]
        # print(index_tournoi)
        index_joueurs = search_tournoi[0]["index_joueurs"]
        # print(index_joueurs)
        # choix_tour = input("Voulez-vous commencer le premier tour ? y/n")
        # tour_list = self.manager.recuperer_tours(index_tournoi)
        self.tour.continuer_tour(index_tournoi, index_joueurs)

    def supprimer_tournoi(self):
        liste_tournois = self.manager.afficher_tournoi()
        choix_tournoi = self.tournoi_vue.get_choix_tournoi(liste_tournois)
        self.manager.delete_tournoi(choix_tournoi)
        print("Le tournoi " + choix_tournoi + " a été supprimé")

    def ajouter_joueurs_tournoi(self):
        liste_joueurs = self.manager.recuperer_joueur()
        for i in liste_joueurs:
            prenom_joueur = i["prenom"]
            print(prenom_joueur)

    def rapport_joueurs_tournoi(self, ordre):
        liste_tournois = self.manager.afficher_tournoi()
        choix_tournoi = self.tournoi_vue.get_choix_tournoi(liste_tournois)
        search_tournoi = self.manager.search_tournoi(choix_tournoi)
        # print(search_tournoi)
        liste_joueurs_tournoi_index = search_tournoi[0]["index_joueurs"]
        # print(liste_joueurs_tournoi_index)
        liste_joueurs_tournoi = []
        for i in liste_joueurs_tournoi_index:
            joueur = self.manager.recuperer_joueur_tournoi(i)
            liste_joueurs_tournoi.append(joueur[0])
        # print(liste_joueurs_tournoi)
        liste_joueurs_tournoi_sorted = []
        if ordre == "alphabetique":
            liste_joueurs_tournoi_sorted = sorted(
                liste_joueurs_tournoi, key=lambda d: d["nom"], reverse=False
            )
            self.rapport_vue.get_rapport_data(
                liste_joueurs_tournoi_sorted,
                "Liste des joueurs du tournoi par ordre alphabétique",
            )
        elif ordre == "classement":
            liste_joueurs_tournoi_sorted = sorted(
                liste_joueurs_tournoi, key=lambda d: d["classement"], reverse=True
            )
            self.rapport_vue.get_rapport_data(
                liste_joueurs_tournoi_sorted,
                "Liste des joueurs du tournoi par classement",
            )
        # print(liste_joueurs_tournoi_sorted)

    def rapport_liste_tournoi(self):
        liste_tournois = self.manager.afficher_tournoi()
        self.rapport_vue.get_rapport_data(liste_tournois, "Liste des tournois")
        # print(liste_tournois)
