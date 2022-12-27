class JoueurVue:

    def __init__(self):
        pass
    
    def get_user_data(self):
        #Joueur 1
        index_1 = input("Index du Joueur : ")
        nom_1 = input("Nom du Joueur : ")
        prenom_1 = input("Prenom du joueur : ")
        date_naissance_1 = input("Date de naissance du joueur : ")
        sexe_1 = input("Sexe : ")
        classement_1 = input("Classement : ")
        
        data_player = {
            "index":index_1,
            "nom":nom_1,
            "prenom":prenom_1,
            "date_naissance":date_naissance_1,
            "sexe":sexe_1,
            "classement":classement_1
        }
        return data_player

        #ecrire un menu pour entrer les joueurs, etc...
        #creer tournoi dans vue, modele, controleur
    
    def get_choix_joueur(self, liste_joueurs):
    
        for i in liste_joueurs:
            classement_joueur = i["classement"]
            nom_joueur = i["nom"]
            print(classement_joueur + " : " + nom_joueur)

        nom_joueur = input("Nom du Joueur : ")
        new_classement = input("Nouveau classement : ")

        return nom_joueur, new_classement