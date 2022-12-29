class Match:
    def __init__(self, equipe_1, equipe_2):
        self.equipe_1 = equipe_1
        self.equipe_2 = equipe_2
        # self.score = score
        self.equipe_1_len = len(equipe_1)

    def Nouveau_Tour(self):
        for i in range(self.equipe_1_len):
            joueur_1 = self.equipe_1[i]
            joueur_2 = self.equipe_2[i]

            print("Joueur 1", joueur_1["nom"])
            score_joueur_1 = input("Score du joueur " + joueur_1["nom"] + " : ")
            joueur_1["score"] = score_joueur_1
            print(joueur_1)

            print("Joueur 2", joueur_2["nom"])
            score_joueur_2 = input("Score du joueur " + joueur_2["nom"] + " : ")
            joueur_2["score"] = score_joueur_2
            print(joueur_2)
