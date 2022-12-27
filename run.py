#from controleurs.joueur import JoueurControleur
#from controleurs.tournoi import TournoiControleur
from controleurs.controleur import Controleur
from controleurs.manager import Manager



new_manager = Manager()

new_game = Controleur()
#new_tournoi = TournoiControleur()
new_game.run()
new_manager.afficher_tournoi()
#new_tournoi.run()