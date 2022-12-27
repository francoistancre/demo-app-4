class TournoiVue:
    
    def __init__(self):
        pass
    
    def get_tournoi_data(self, liste_joueurs):
        #Joueur 1
        print("*********************************************************")
        print("****** ENTRER LES DONNEES POUR UN NOUVEAU TOURNOI *******")
        print("*********************************************************")
        index_tournoi = input("Index du Tournoi : ")
        nom_tournoi = input("Nom du Tournoi : ")
        lieu_tournoi = input("Lieu du Tournoi : ")
        nombre_tours = 4 # Regler par défaut à 4
        tournee = input("Tournées: ") # nombre de tours int
        joueurs_tournoi = 8 # Taille de la liste de joueurs
        controle_temps = input("Controle du temps : ")
        description = input("Description : ")
        liste_index_joueurs = []
        for i in range(joueurs_tournoi):
            for i in liste_joueurs:
                index_joueur = i["index"]
                nom_joueur = i["nom"]
                print(index_joueur, " : " ,nom_joueur)
            choix_joueur = input("Choisissez l'index du joueur pour l'ajouter au tournoi")
            liste_index_joueurs.append(choix_joueur)
        
        data_tournoi = {
            "index_tournoi":index_tournoi,
            "nom_tournoi":nom_tournoi,
            "lieu_tournoi":lieu_tournoi,
            "nombre_tours":nombre_tours,
            "tournee":tournee,
            "joueurs_tournoi":joueurs_tournoi,
            "index_joueurs":liste_index_joueurs,
            "controle_temps":controle_temps,
            "description":description
        }
        return data_tournoi

    def get_choix_tournoi(self, liste_tournois):

        for i in liste_tournois:
            index_tournoi = i["index"]
            nom_tournoi = i["nom"]
            print(index_tournoi + " : " + nom_tournoi)

        nom_tournoi = input("Nom du Tournoi : ")

        return nom_tournoi
