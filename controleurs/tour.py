# from modeles.tournoi import Tournoi
from controleurs.manager import Manager
from modeles.tour import Tour
from vues.tournoi import TournoiVue
from vues.rapport import RapportVue
import datetime


class TourControleur:
    def __init__(self):
        # self.tournoi = Tournoi()
        self.manager = Manager()
        self.tournoi_vue = TournoiVue()
        self.rapport_vue = RapportVue()

    def tour_1(self, index_tournoi, index_joueurs):

        index_tour = 1
        date_debut = str(datetime.datetime.now())
        name_tour = "tour1"

        liste_joueurs = self.manager.recuperer_joueur_tournoi(index_joueurs)

        taille_liste = len(liste_joueurs)
        joueurs_match = []
        liste_matchs = []
        equipe_1 = liste_joueurs[0: taille_liste // 2]
        equipe_2 = liste_joueurs[taille_liste // 2:]

        joueurs_match = [equipe_1, equipe_2]

        for i in range(len(liste_joueurs) // 2):
            match = [joueurs_match[0][i], joueurs_match[1][i], (0, 0)]
            liste_matchs.append(match)

        for index, item in enumerate(liste_matchs):
            print("match ", index)

            joueur_1, joueur_2, score_joueur_1, score_joueur_2 = self.set_score(item)
            # match index : affecter au tuple score le score joueur 1 et joueur 2
            liste_matchs[index][2] = (score_joueur_1, score_joueur_2)
            liste_matchs[index][0] = joueur_1
            liste_matchs[index][1] = joueur_2
            # set_score(item)
            print("*********************" * 5)

        print("La liste des matchs pour le tour 1 : ")
        for index, item in enumerate(liste_matchs):
            print("score du match : ", index, item[2])
            print(item[0])
            print(item[1])
            print("*********************" * 5)

        date_fin = str(datetime.datetime.now())
        # appeler save tour
        tour = Tour(
            index_tour, index_tournoi, name_tour, liste_matchs, date_debut, date_fin
        )
        tour.save_tours()

    def set_score(self, match):
        joueur_1 = match[0]
        joueur_2 = match[1]

        print("Joueur 1", joueur_1["nom"])
        score_joueur_1 = int(input("Score du joueur " + joueur_1["nom"] + " : "))
        joueur_1["score"] = int(joueur_1["score"]) + score_joueur_1
        print(joueur_1)

        print("Joueur 2", joueur_2["nom"])
        score_joueur_2 = int(input("Score du joueur " + joueur_2["nom"] + " : "))
        joueur_2["score"] = int(joueur_2["score"]) + score_joueur_2

        print(joueur_2)

        return joueur_1, joueur_2, score_joueur_1, score_joueur_2

    def test_match(self, liste_matchs, new_match):
        new_joueur_1 = new_match[0]["nom"]
        new_joueur_2 = new_match[1]["nom"]
        compteur = 0
        for match in liste_matchs:
            old_joueur_1 = match[0]["nom"]
            old_joueur_2 = match[1]["nom"]
            if (new_joueur_1 == old_joueur_1 or new_joueur_1 == old_joueur_2) and (
                new_joueur_2 == old_joueur_1 or new_joueur_2 == old_joueur_2
            ):
                compteur += 1
        if compteur != 0:
            return False
        else:
            return True

    def test_joueur(self, liste_matchs, joueur):
        compteur = 0
        joueur = joueur["nom"]
        for match in liste_matchs:
            old_joueur_1 = match[0]["nom"]
            old_joueur_2 = match[1]["nom"]

            if joueur == old_joueur_1 or joueur == old_joueur_2:
                compteur += 1
        if compteur != 0:
            return False
        else:
            return True

    def tour_generate(self, new_liste_joueurs, new_liste_matchs, liste_matchs):

        for index, joueur1 in enumerate(new_liste_joueurs):
            if self.test_joueur(new_liste_matchs, joueur1):
                for joueur2 in new_liste_joueurs[index + 1:]:
                    new_match = [joueur1, joueur2, (0, 0)]

                    if self.test_match(liste_matchs, new_match):

                        new_liste_matchs.append(new_match)

                        print(new_match[0]["nom"])
                        print(new_match[1]["nom"])

                        break

        # Faire jouer les matchs
        for index, item in enumerate(new_liste_matchs):
            print("match ", index)
            joueur_1, joueur_2, score_joueur_1, score_joueur_2 = self.set_score(item)
            # match index : affecter au tuple score le score joueur 1 et joueur 2
            new_liste_matchs[index][2] = (score_joueur_1, score_joueur_2)
            new_liste_matchs[index][0] = joueur_1
            new_liste_matchs[index][1] = joueur_2
            # set_score(item)
            print("*********************" * 5)

        return new_liste_matchs

    def tour(self, index_tournoi, liste_matchs, numero_tour, index_joueurs):

        index_tour = numero_tour
        date_debut = str(datetime.datetime.now())
        name_tour = "tour" + str(numero_tour)

        liste_joueurs = self.manager.recuperer_joueur_tournoi(index_joueurs)
        new_liste_joueurs = sorted(
            liste_joueurs, key=lambda d: d["score"], reverse=True
        )
        new_liste_matchs = []

        new_liste_matchs = self.tour_generate(
            new_liste_joueurs, new_liste_matchs, liste_matchs
        )

        print("********** Match du tour " + str(numero_tour) + "*************")
        for index, item in enumerate(new_liste_matchs):
            print("match ", index)
            print(item[0])
            print(item[1])
            print(item[2])
            print("*********************" * 5)

        date_fin = str(datetime.datetime.now())
        tour = Tour(
            index_tour, index_tournoi, name_tour, new_liste_matchs, date_debut, date_fin
        )
        tour.save_tours()

    def continuer_tour(self, index_tournoi, index_joueurs):
        tour_list = self.manager.recuperer_tours(index_tournoi)
        if len(tour_list) != 0:

            nombre_de_tours = len(tour_list)

            if nombre_de_tours == 1:
                print("Le tour 1 est effectué")

                matchs_list = tour_list[0]["matchs"]

                choix_tour = input("Voulez-vous commencer le tour 2 ? y/n")
                if choix_tour == "y":
                    self.tour(index_tournoi, matchs_list, 2, index_joueurs)

            elif nombre_de_tours == 2:
                print("Le tour 2 est effectué")
                matchs_list = tour_list[0]["matchs"] + tour_list[1]["matchs"]
                choix_tour = input("Voulez-vous commencer le tour 3 ? y/n")
                if choix_tour == "y":
                    self.tour(index_tournoi, matchs_list, 3, index_joueurs)

            elif nombre_de_tours == 3:
                print("Le tour 3 est effectué")
                matchs_list = (
                    tour_list[0]["matchs"]
                    + tour_list[1]["matchs"]
                    + tour_list[2]["matchs"]
                )
                choix_tour = input("Voulez-vous commencer le tour 4 ? y/n")
                if choix_tour == "y":
                    self.tour(index_tournoi, matchs_list, 4, index_joueurs)
                print("Bravo ! Le tournoi est terminé")

            elif nombre_de_tours == 4:
                print("Le tournoi est terminé")
        else:
            print("Il n'y a pas de tours pour ce tournoi")
            choix_tour = input("Voulez-vous commencer le premier tour ? y/n")
            if choix_tour == "y":
                self.tour_1(index_tournoi, index_joueurs)

    def afficher_tour(self):
        liste_tournois = self.manager.afficher_tournoi()
        for i in liste_tournois:
            index_tournoi = i["index"]
            nom_tournoi = i["nom"]
            print(index_tournoi + " : " + nom_tournoi)

        index_tournoi = input("Index du Tournoi : ")
        index_joueurs = self.manager.search_tournoi_index(index_tournoi)[0][
            "index_joueurs"
        ]
        print(index_joueurs)

    def rapport_liste_tours(self):
        liste_tournois = self.manager.afficher_tournoi()
        for i in liste_tournois:
            index_tournoi = i["index"]
            nom_tournoi = i["nom"]
            print(index_tournoi + " : " + nom_tournoi)

        index_tournoi = input("Index du Tournoi : ")
        tour_list = self.manager.recuperer_tours(index_tournoi)

        self.rapport_vue.get_rapport_data(tour_list, "Liste des tours du tournoi")

    def rapport_liste_matchs(self):
        liste_tournois = self.manager.afficher_tournoi()
        for i in liste_tournois:
            index_tournoi = i["index"]
            nom_tournoi = i["nom"]
            print(index_tournoi + " : " + nom_tournoi)

        index_tournoi = input("Index du Tournoi : ")
        tour_list = self.manager.recuperer_tours(index_tournoi)
        liste_matchs = []
        for i in range(len(tour_list)):
            liste_matchs.append(tour_list[i]["matchs"])

        self.rapport_vue.get_rapport_data(liste_matchs, "Liste des matchs du tournoi")

        # si il n'y a pas de tours donc tour_list est vide alors commencer le tour 1 ?
        # Si il y a un tour 1 commencer le tour 2
        # si il y a un tour 2 commencer le tour 3
        # si il y a un tour 3 commencer le tour 4

        # utiliser la variable tour_list pour en extraire les matchs nécessaire pour le tour 2

        # index_tournoi = search_tournoi[0]['index']
        # choix_tour = input("Voulez-vous commencer le premier tour ? y/n")
        # if choix_tour == "y":
        #    self.tour.tour_1(index_tournoi)
