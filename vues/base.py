



class Vue:

    def __init__(self):

        pass

    def menu_principale(self):
        #ajouter 
        choix = int(input("""
            1. Creer un nouveau tournoi
            2. Ajouter un nouveau joueur
            3. Continuer un tournoi existant
            4. Afficher les joueurs
            5. Afficher les tours pour un tournoi
            6. Supprimer un tournoi
            7. Modifier classement Joueur
            8. Rapports

        """))
        return choix

    def menu_rapport(self):
            #ajouter 
        choix = int(input("""
            1. Liste des joueurs par ordre alphabétique
            2. Liste des joueurs par classement
            3. Liste des joueurs d'un tournoi par ordre alphabétique
            4. Liste des joueurs d'un tournoi par classement
            5. Liste de tous les tournois
            6. Liste de tous les tours d'un tournoi
            7. Liste de tous les matchs d'un tournoi
            8. Quitter

        """))
        return choix
    
    #creer focntion afficher qui prend un message en parametre et qui print le message
    