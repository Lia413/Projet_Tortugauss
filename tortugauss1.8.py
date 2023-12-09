from itertools import count
import numpy as np
import tkinter as tk
from tkinter import ttk
import time
from PIL import Image, ImageTk

##################################
# tortugauss1.6.3.py             #
# Par Eytan Benharrous           #
#     Lisa Joly                  #
#     Oriane Puerta              #
#     Violette Fiant             #
# Créé le 2023-10-04 à 22:30:07  #
#                                #
#                  /^\--/^\      #
#                  | O  O |      #
#    Whoo!!        \  \/  /      #
#                  / ¤¤  / \     #
#      Whoo!!     |¤¤¤¤¤|;;;|    #
#                 |¤¤¤¤¤|;;;|    #
#                 | ¤¤¤¤ \;;|    #
#                  \ ¤¤    \|    #
####################(((##(((######

"""
_________ _______  _______ _________          _______  _______           _______  _______ 
\__   __/(  ___  )(  ____ )\__   __/|\     /|(  ____ \(  ___  )|\     /|(  ____ \(  ____ \ 
   ) (   | (   ) || (    )|   ) (   | )   ( || (    \/| (   ) || )   ( || (    \/| (    \/
   | |   | |   | || (____)|   | |   | |   | || |      | (___) || |   | || (_____ | (_____ 
   | |   | |   | ||     __)   | |   | |   | || | ____ |  ___  || |   | |(_____  )(_____  )
   | |   | |   | || (\ (      | |   | |   | || | \_  )| (   ) || |   | |      ) |      ) |
   | |   | (___) || ) \ \__   | |   | (___) || (___) || )   ( || (___) |/\____) |/\____) |
   )_(   (_______)|/   \__/   )_(   (_______)(_______)|/     \|(_______)\_______)\_______)
                                                                                          
"""

ListeA = [
    np.array([[2]], dtype=np.float64),
    np.array([[2]], dtype=np.float64),
    np.array([[2, 0, 0], [0, 3, 0], [0, 0, 4]], dtype=np.float64),
    np.array([[2, 0], [4, 0]], dtype=np.float64),
    np.array([[1, 2], [0, 1]], dtype=np.float64),
    np.array([[2, 0], [4, 0]], dtype=np.float64),  # abscence de solution
    np.array([[1, 1], [1, 1]], dtype=np.float64),  # sol infinin
    np.array([[1, 1], [1, 1]], dtype=np.float64),  # sol infini
    np.array([[2, 2], [0, 4]], dtype=np.float64),
    np.array([[1, 4], [-1, 2]], dtype=np.float64),
    np.array([[0, -2, -4], [5, 5, 5], [1, 1, 0]], dtype=np.float64),  # 11
    np.array([[0, -2, -4], [5, 5, 5], [1, 1, 0]], dtype=np.float64),  # 12
    # il manque systeme matrice triangulaire sup
    np.array([[1, 0], [2, 3]], dtype=np.float64),
    np.array([[1, 0], [1, 1]], dtype=np.float64),  # 14
    np.array([[1, 3], [2, 2]], dtype=np.float64),  # 16
    np.array([[1, 3, 1], [2, 3, 4], [1, 0, -3]], dtype=np.float64),  # 36
    np.array([[4, -2], [1, 3]], dtype=np.float64),  # 17
    np.array([[6, -3], [-3, 2]], dtype=np.float64),  # 18
    np.array([[-6, 2], [1, -2]], dtype=np.float64),  # 19
    np.array([[-4, 6], [1, 6]], dtype=np.float64),  # 20
    np.array([[5, -1], [5, 1]], dtype=np.float64),  # 21
    np.array([[-4, -6], [0, -2]], dtype=np.float64),  # 22
    np.array([[3, -5], [0, -3]], dtype=np.float64),  # 23
    np.array([[-5, -2], [4, 5]], dtype=np.float64),  # 24
    np.array([[5, 0], [-3, 6]], dtype=np.float64),  # 25
    np.array([[1, -5], [3, 2]], dtype=np.float64),  # 26
    np.array([[0, 2], [2, 3]], dtype=np.float64),  # 27
    np.array([[-2, 0], [-2, -2]], dtype=np.float64),  # 28
    np.array([[2, 2], [0, 6]], dtype=np.float64),  # 29
    np.array([[-1, 1], [2, -1]], dtype=np.float64),  # 30
    np.array([[-1, 2], [3, 0]], dtype=np.float64),  # 31
    np.array([[5, 0], [-3, 1]], dtype=np.float64),  # 32
    np.array([[1, 6, -1], [-6, 5, -6], [5, 3, 0]], dtype=np.float64),  # 33
    np.array([[-3, -2, 2], [-1, 1, -5], [-1, 2, -4]], dtype=np.float64),  # 34
    np.array([[-1, 1, -5], [5, -3, 6], [-2, 2, 3]], dtype=np.float64),  # 35
    np.array([[-5, 6, -1], [-4, 3, -2], [-1, 6, -5]], dtype=np.float64),  # 36
    np.array([[1, -3, 1], [-1, -1, 3], [-3, -6, 1]], dtype=np.float64),  # 37
    np.array([[-1, 3, 2], [0, 3, 0], [2, -3, -2]], dtype=np.float64),  # 38
    np.array([[1, 5, 2], [4, -5, 0], [5, 1, 1]], dtype=np.float64),  # 39
    np.array([[3, 2, 4], [-1, 2, 0], [4, 1, 4]], dtype=np.float64),  # 40
]


ListeB = [
    np.array([3], dtype=np.float64),  # 1
    np.array([-3], dtype=np.float64),  # 2
    np.array([5, 5, 5], dtype=np.float64),  # 3
    np.array([3, 6], dtype=np.float64),  # 4
    np.array([6, 2], dtype=np.float64),  # 5
    np.array([5, 5], dtype=np.float64),  # 6
    np.array([4, 4], dtype=np.float64),  # 7
    np.array([4, 4], dtype=np.float64),  # 8 double sol
    np.array([5, 2], dtype=np.float64),  # 9
    np.array([-2, -4], dtype=np.float64),  # 10
    np.array([3.8, 6.5, 2.3], dtype=np.float64),  # 11
    np.array([3.8, 6.5, 2.3], dtype=np.float64),  # 12 triang
    np.array([2, 8], dtype=np.float64),  # 13
    np.array([2, 3.5], dtype=np.float64),  # 14
    np.array([3, 4], dtype=np.float64),  # 16
    np.array([8, 9, 4], dtype=np.float64),  # 36
    np.array([4.8, -5.1], dtype=np.float64),  # 17
    np.array([8.4, -4.6], dtype=np.float64),  # 18
    np.array([4.4, 2.6], dtype=np.float64),  # 19
    np.array([-2.4, 5.1], dtype=np.float64),  # 20
    np.array([5.2, 3.8], dtype=np.float64),  # 21
    np.array([-4.4, -2.4], dtype=np.float64),  # 22
    np.array([-4.4, -3.0], dtype=np.float64),  # 23
    np.array([5.6, -8.9], dtype=np.float64),  # 24
    np.array([-4.5, -3.9], dtype=np.float64),  # 25
    np.array([5.5, -2.2], dtype=np.float64),  # 26
    np.array([3.6, 7.4], dtype=np.float64),  # 27
    np.array([4.2, 4.8], dtype=np.float64),  # 28
    np.array([-5.6, -6.6], dtype=np.float64),  # 29
    np.array([-2.9, 4.1], dtype=np.float64),  # 30
    np.array([-4.4, 6.6], dtype=np.float64),  # 31
    np.array([4.0, -2.6], dtype=np.float64),  # 32
    np.array([8.7, 4.3, 3.1], dtype=np.float64),  # 33
    np.array([3.5, -6.1, -4.3], dtype=np.float64),  # 34
    np.array([-4.7, -2.9, 8.8], dtype=np.float64),  # 35
    np.array([6.6, 5.4, -3.0], dtype=np.float64),  # 36
    np.array([-7.5, -3.3, -8.1], dtype=np.float64),  # 37
    np.array([5.3, 3.0, -5.4], dtype=np.float64),  # 38
    np.array([5.8, -9.0, -3.1], dtype=np.float64),  # 39
    np.array([-8.0, -2.4, -6.7], dtype=np.float64),  # 40
]

listeetoile = [
    (20, 40),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
    (40, 80),
]

"""
 ___________    ____ .___________.    ___      .__   __.          
|   ____\   \  /   / |           |   /   \     |  \ |  |        
|  |__   \   \/   /  `---|  |----`  /  ^  \    |   \|  |        
|   __|   \_    _/       |  |      /  /_\  \   |  . `  |       
|  |____    |  |         |  |     /  _____  \  |  |\   |  
|_______|   |__|         |__|    /__/     \__\ |__| \__|  

 __       __       _______.     ___      
|  |     |  |     /       |    /   \     
|  |     |  |    |   (----`   /  ^  \    
|  |     |  |     \   \      /  /_\  \   
|  `----.|  | .----)   |    /  _____  \  
|_______||__| |_______/    /__/     \__\ 

  ______   .______       __       ___      .__   __.  _______ 
 /  __  \  |   _  \     |  |     /   \     |  \ |  | |   ____|
|  |  |  | |  |_)  |    |  |    /  ^  \    |   \|  | |  |__   
|  |  |  | |      /     |  |   /  /_\  \   |  . `  | |   __|  
|  `--'  | |  |\  \----.|  |  /  _____  \  |  |\   | |  |____ 
 \______/  | _| `._____||__| /__/     \__\ |__| \__| |_______|

____    ____  __    ______    __       _______ .___________.___________. _______ 
\   \  /   / |  |  /  __  \  |  |     |   ____||           |           ||   ____|
 \   \/   /  |  | |  |  |  | |  |     |  |__   `---|  |----`---|  |----`|  |__   
  \      /   |  | |  |  |  | |  |     |   __|      |  |        |  |     |   __|  
   \    /    |  | |  `--'  | |  `----.|  |____     |  |        |  |     |  |____ 
    \__/     |__|  \______/  |_______||_______|    |__|        |__|     |_______|
"""

"Il y a un sens a tout les combats."
"Parfois, certains valent la peine d'être perdu,"
"Mais tout les combats méritent d'être mené jusqu'au bout."


class remarque:
    def __init__(
        self, racine: tk, text, font, height, width, border=0, background="white"
    ) -> None:
        self.canva = tk.Canvas(
            racine,
            height=height * len(text),
            width=width,
            background=background,
            highlightthickness=border,
        )
        textlocal = ""
        for i in text:
            textlocal += i + "\n"
        self.id = self.canva.create_text(
            width / 2, 2, anchor="n", text=textlocal, font=font, fill="red"
        )
        self.text = text
        self.canva.pack()
        self.height = height
        self.width = width

    def pack(self):
        if self.text == "":
            self.canva.configure(height=1)
        else:
            self.canva.configure(height=self.height * len(self.text))

    def config(self, texte):
        self.text = texte
        textlocal = ""
        for i in texte:
            textlocal += i + "\n"

        self.canva.itemconfig(self.id, text=textlocal)


"Ici commence notre art."


class Tortugauss(tk.Tk):
    def __init__(
        self,
        A,
        B,
        star,
        screenName=None,
        baseName=None,
        className: str = "Tk",
        useTk: bool = True,
        sync: bool = False,
        use=None,
    ) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)

        # définition des listes qui contiendront les éléments de l'interfaces
        self.listeetoile = star
        self.listetext = [
            ["Mmh, la tortue s'est régalée."],
            ["Aucune laitue ne vous résiste"],
            [
                "Chacune de ces tortues avance à sa propre",
                "vitesse. Par ailleur, elles avancent ",
                "chacune indépendament des autres.",
            ],
            [
                "Ces deux tortues avance de manière",
                "dépendante tout en avancant à des",
                "vitesses différentes.",
            ],
            [
                "Ces tortues sont encore une fois",
                "dépendante selon le bouton foncé.",
                "Cependant, le bouton clair agit sur",
                "la deuxième indépendament de la première.",
            ],
            ["En effet, il n'y en a pas"],
            ["Bien joué. Essayez de retenir la solution", " de ce niveau"],
            [
                "En effet, ce niveau possède de nombreuses",
                "solutions (en réalité, une infinité)",
            ],
            ["Bravo! Ça ne t'a posé aucun problème"],
            ["Trop fort, tu maitrises parfaitement", "le controle des deux tortues."],
            ["Pas facile, pas vrai? Le niveau suivant", "devrait t'aider."],
            ["ça devait être bien plus facile que le", "précédent!"],
            [
                "Normalement, vous avez du remarquer que",
                "les solutions sont les mêmes, mêmes après",
                "ajout et soustraction de colonnes.",
            ],
            [
                "Les solutions sont en effet les mêmes,",
                "après avoir doublé toutes les colonnes.",
            ],
            [
                "Si vous avez compris la méthode présentée,",
                "essayez de l'appliquer pour résoudre le",
                "niveau suivants",
            ],
            [
                "Bien joué! Vous avez résolu tous les niveaux",
                "éducatifs, nous espérons que cela vous as plu.",
                "Vous pouvez maintenant continuer à résoudre",
                "des niveaux pour débloquer des diamants et",
                "acheter de nouveaux animaux.",
            ],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        ]
        self.listetext2 = [
            ["La tortue a faim!", "Essaye de la déplacer avec le bouton bleu."],
            [
                "Cette fois, la laitue est de l'autre côté.",
                "Il faut faire reculer la tortue.",
            ],
            [
                "Ces trois tortues sont toutes affamées.",
                "chacune possède son propre bouton.",
            ],
            ["Ces deux tortues sont liées.", "elles sont controlées par le même bouton."],
            [
                "Deux tortues, deux boutons",
                "Mais est-ce aussi simple que les niveaux précédents?",
            ],
            ["Ce niveau est vraiment facile"],
            ["Concentrez-vous pour mémoriser comment vous résolvez", "ce niveau"],
            [
                "Ce niveau est le même que le niveau précédent,",
                "mais essayez cette fois de trouver une autre solution,",
            ],
            ["Il n'y a qu'une solution pour ce niveau", "Arriveras-tu à la trouver?"],
            [
                "Les choses commencent à se compliquer, le bouton foncé",
                "fait à la fois avancer la première tortue et reculer la",
                "deuxième",
            ],
            ["voyons voir comment tu te débrouilles avec 3 tortues"],
            [
                "Ce niveau est le même que le précédent.",
                "mais cette fois, le tableau de droite devrait t'aider.",
                "Essaye de résoudre le niveau en utilisant seulement",
                "le tableau de droite",
            ],
            [
                "Faites glisser les petites icônes A et B dans les cercles",
                "du pouvoir tortue et appuyez sur le bouton pour soustraire ou",
                "ajouter deux colonnes",
            ],
            [
                "Les rectangles du deuxième tableau sont deux fois plus",
                "élevés que ceux du premier. Voyons voir si leur solution sont",
                "différentes ou non.",
            ],
            [
                "Essayez de doubler la hauteur de la première colonne",
                "avec le boutons X, puis soustrayez la deuxième colonne",
                "à la première. Vous devriez obtenir un niveau simple.",
            ],
            ["Essayez d'adopter la même méthode que le niveau précédent"],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        ]
        self.listebouton = []
        self.listebouton2 = []
        self.listebouton3 = []
        self.listerectangle = []
        self.listeligne = []
        self.listeboule = []
        self.listeovalgauss = []
        self.gaussemplacement = [0, 0, 0, 0]
        self.couleurs = ["#00868B", "#6CA6CD", "#00CDCD", "#68228B"]
        self.activecouleur = ["turquoise3", "Skyblue2", "cyan2", "darkorchid3"]

        self.hauteur_fenetre = int(self.winfo_screenheight() * 5 / 6)
        self.largeur_fenetre = int(self.hauteur_fenetre * 800 / 500)
        print(self.largeur_fenetre, self.hauteur_fenetre)
        self.resizable(False, False)
        self.title("Tortugauss")
        self.geometry(str(self.largeur_fenetre) + "x" + str(self.hauteur_fenetre))
        self.config(background="papaya whip")
        style = ttk.Style(self)
        style.configure("TCombobox", background="lightskyblue2")
        self.enjeu = False
        self.actifniveau = 0
        self.listeA = A
        self.listeB = B
        self.actifA = A[self.actifniveau]
        if self.actifniveau == 11:
            self.actifA2 = np.array(
                [[1, 1, 1], [0, 2, 4], [0, 0, 4]], dtype=np.float64
            )  # 12
        elif self.actifniveau == 12:
            self.actifA2 = self.listeA[self.actifniveau].copy()
        elif self.actifniveau == 14:
            self.actifA2 = self.listeA[self.actifniveau].copy()
        else:
            self.actifA2 = np.array([[2, 0], [2, 2]], dtype=np.float64)
        self.actifB = B[self.actifniveau]
        if self.actifniveau == 11:
            self.actifB2 = np.array([1.3, -3.8, -4.0], dtype=np.float64)  # 12 triang
        elif self.actifniveau == 12:
            self.actifB2 = self.listeB[self.actifniveau].copy()  # 13
        elif self.actifniveau == 14:
            self.actifB2 = self.listeB[self.actifniveau].copy()
        else:
            self.actifB2 = np.array([4, 7], dtype=np.float64)
        self.actifAi = A[self.actifniveau].copy()
        self.actifBi = B[self.actifniveau].copy()
        self.chargement = tk.Frame(self, background="papaya whip")
        self.chargementtext = tk.Label(
            self.chargement,
            text="chargement...",
            font="Helvetica " + str(int(4 * self.hauteur_fenetre / 100)) + " bold",
            background="papaya whip",
        )
        self.chargementtext.pack(side="right")
        tortue = ImageTk.PhotoImage(
            Image.open("projet tortuga/tortumim.jpg").resize((50, 50))
        )
        self.etoilejaune = ImageTk.PhotoImage(
            Image.open("projet tortuga/etoilejaune.png").resize(
                (
                    int(self.hauteur_fenetre * 6 / 100),
                    int(self.hauteur_fenetre * 6 / 100),
                )
            )
        )
        self.etoilegrise = ImageTk.PhotoImage(
            Image.open("projet tortuga/etoilegris.png").resize(
                (
                    int(self.hauteur_fenetre * 6 / 100),
                    int(self.hauteur_fenetre * 6 / 100),
                )
            )
        )
        self.etoilejaune2 = ImageTk.PhotoImage(
            Image.open("projet tortuga/etoilejaune.png").resize(
                (
                    int(self.hauteur_fenetre * 4 / 100),
                    int(self.hauteur_fenetre * 4 / 100),
                )
            )
        )
        self.etoilegrise2 = ImageTk.PhotoImage(
            Image.open("projet tortuga/etoilegris.png").resize(
                (
                    int(self.hauteur_fenetre * 4 / 100),
                    int(self.hauteur_fenetre * 4 / 100),
                )
            )
        )
        self.chargementim = tk.Label(
            self.chargement, image=tortue, background="papaya whip"
        )
        self.chargementim.pack(side="left")
        self.chargement.pack(side="bottom")
        self.update()
        self.after(1, self.initialisejeu)
        self.mainloop()

    def initialisejeu(self):
        # création des widgets
        self.stop = True
        self.pause = tk.Canvas(
            self,
            width=self.largeur_fenetre,
            height=(self.hauteur_fenetre / 10),
            bg="papaya whip",
            borderwidth=0,
            highlightthickness=0,
        )
        self.itemniveau = self.pause.create_text(
            self.hauteur_fenetre * 5 / 100,
            self.hauteur_fenetre / 20,
            font="Helvetica " + str(int(4 * self.hauteur_fenetre / 100)) + " bold",
            anchor="w",
            text="niveau ",
            fill="black",
        )
        self.pause.create_oval(
            self.largeur_fenetre - self.hauteur_fenetre * 4 / 100,
            self.hauteur_fenetre / 100,
            self.largeur_fenetre - self.hauteur_fenetre * 11 / 100,
            self.hauteur_fenetre * 8 / 100,
            width=2,
            fill="white",
        )
        self.pause.create_oval(
            self.largeur_fenetre
            - self.hauteur_fenetre * 4 / 100
            - self.hauteur_fenetre / 10,
            self.hauteur_fenetre * 1 / 100,
            self.largeur_fenetre
            - self.hauteur_fenetre * 11 / 100
            - self.hauteur_fenetre / 10,
            self.hauteur_fenetre * 8 / 100,
            width=2,
            fill="white",
        )
        self.pause.create_arc(
            self.largeur_fenetre
            - self.hauteur_fenetre * 6 / 100
            - self.hauteur_fenetre / 10,
            self.hauteur_fenetre * 3 / 100,
            self.largeur_fenetre
            - self.hauteur_fenetre * 9 / 100
            - self.hauteur_fenetre / 10,
            self.hauteur_fenetre * 6 / 100,
            start=00,
            extent=120,
            width=3 * self.hauteur_fenetre / 200,
            style="arc",
        )
        self.pause.create_arc(
            self.largeur_fenetre
            - self.hauteur_fenetre * 6 / 100
            - self.hauteur_fenetre / 10,
            self.hauteur_fenetre * 3 / 100,
            self.largeur_fenetre
            - self.hauteur_fenetre * 9 / 100
            - self.hauteur_fenetre / 10,
            self.hauteur_fenetre * 6 / 100,
            start=180,
            extent=120,
            width=3 * self.hauteur_fenetre / 200,
            style="arc",
        )
        self.pause.create_arc(
            self.largeur_fenetre
            - self.hauteur_fenetre * 6 / 100
            - self.hauteur_fenetre / 10,
            self.hauteur_fenetre * 3 / 100,
            self.largeur_fenetre
            - self.hauteur_fenetre * 9 / 100
            - self.hauteur_fenetre / 10,
            self.hauteur_fenetre * 6 / 100,
            start=0,
            extent=120,
            width=self.hauteur_fenetre / 100,
            style="arc",
            outline="light grey",
        )
        self.pause.create_arc(
            self.largeur_fenetre
            - self.hauteur_fenetre * 6 / 100
            - self.hauteur_fenetre / 10,
            self.hauteur_fenetre * 3 / 100,
            self.largeur_fenetre
            - self.hauteur_fenetre * 9 / 100
            - self.hauteur_fenetre / 10,
            self.hauteur_fenetre * 6 / 100,
            start=180,
            extent=120,
            width=self.hauteur_fenetre / 100,
            style="arc",
            outline="light grey",
        )
        self.pause.create_line(
            self.largeur_fenetre
            - self.hauteur_fenetre * 9 / 100
            - self.hauteur_fenetre / 10,
            self.hauteur_fenetre * 3 / 100,
            self.largeur_fenetre
            - self.hauteur_fenetre * 9 / 100
            - self.hauteur_fenetre / 10,
            self.hauteur_fenetre * 5 / 100,
            arrow="first",
            width=3 * self.hauteur_fenetre / 200,
            arrowshape=(
                3 * self.hauteur_fenetre / 200,
                3 * self.hauteur_fenetre / 200,
                self.hauteur_fenetre / 100,
            ),
        )
        self.pause.create_line(
            self.largeur_fenetre
            - self.hauteur_fenetre * 9 / 100
            - self.hauteur_fenetre / 10,
            self.hauteur_fenetre * 6.5 / 200,
            self.largeur_fenetre
            - self.hauteur_fenetre * 9 / 100
            - self.hauteur_fenetre / 10,
            self.hauteur_fenetre * 5 / 100,
            width=self.hauteur_fenetre / 100,
            arrow="first",
            arrowshape=(
                self.hauteur_fenetre / 100,
                self.hauteur_fenetre / 100,
                self.hauteur_fenetre / 200,
            ),
            fill="light grey",
        )
        self.pause.create_line(
            self.largeur_fenetre
            - self.hauteur_fenetre * 6 / 100
            - self.hauteur_fenetre / 10,
            self.hauteur_fenetre * 4 / 100,
            self.largeur_fenetre
            - self.hauteur_fenetre * 6 / 100
            - self.hauteur_fenetre / 10,
            self.hauteur_fenetre * 6 / 100,
            arrow="last",
            width=3 * self.hauteur_fenetre / 200,
            arrowshape=(
                3 * self.hauteur_fenetre / 200,
                3 * self.hauteur_fenetre / 200,
                self.hauteur_fenetre / 100,
            ),
        )
        self.pause.create_line(
            self.largeur_fenetre
            - self.hauteur_fenetre * 6 / 100
            - self.hauteur_fenetre / 10,
            self.hauteur_fenetre * 4 / 100,
            self.largeur_fenetre
            - self.hauteur_fenetre * 6 / 100
            - self.hauteur_fenetre / 10,
            self.hauteur_fenetre * 11.5 / 200,
            width=self.hauteur_fenetre / 100,
            arrow="last",
            arrowshape=(
                self.hauteur_fenetre / 100,
                self.hauteur_fenetre / 100,
                self.hauteur_fenetre / 200,
            ),
            fill="light grey",
        )
        self.pause.create_line(
            self.largeur_fenetre
            - self.hauteur_fenetre * 8.5 / 100
            - self.hauteur_fenetre / 10,
            self.hauteur_fenetre * 5 / 200,
            self.largeur_fenetre
            - self.hauteur_fenetre * 7.75 / 100
            - self.hauteur_fenetre / 10,
            self.hauteur_fenetre * 7.5 / 200,
            width=3,
        )
        self.pause.create_line(
            self.largeur_fenetre
            - self.hauteur_fenetre * 7.25 / 100
            - self.hauteur_fenetre / 10,
            self.hauteur_fenetre * 10.5 / 200,
            self.largeur_fenetre
            - self.hauteur_fenetre * 6.5 / 100
            - self.hauteur_fenetre / 10,
            self.hauteur_fenetre * 13 / 200,
            width=3,
        )
        self.pause.create_rectangle(
            self.largeur_fenetre - self.hauteur_fenetre * 6 / 100,
            self.hauteur_fenetre * 5 / 200,
            self.largeur_fenetre - self.hauteur_fenetre * 7 / 100,
            self.hauteur_fenetre * 13 / 200,
            width=2,
            fill="grey73",
        )
        self.pause.create_rectangle(
            self.largeur_fenetre - self.hauteur_fenetre * 8 / 100,
            self.hauteur_fenetre * 5 / 200,
            self.largeur_fenetre - self.hauteur_fenetre * 9 / 100,
            self.hauteur_fenetre * 13 / 200,
            width=2,
            fill="grey73",
        )
        self.pause.bind("<Button-1>", self.click3)
        self.pauseetoile = [
            self.pause.create_image(
                5 * self.hauteur_fenetre / 100
                + 2 * self.largeur_fenetre / 3
                + 5 * self.hauteur_fenetre / 200,
                self.hauteur_fenetre / 20,
                image=self.etoilejaune,
            ),
            self.pause.create_image(
                11 * self.hauteur_fenetre / 100
                + 2 * self.largeur_fenetre / 3
                + 5 * self.hauteur_fenetre / 200,
                self.hauteur_fenetre / 20,
                image=self.etoilegrise,
            ),
            self.pause.create_image(
                17 * self.hauteur_fenetre / 100
                + 2 * self.largeur_fenetre / 3
                + 5 * self.hauteur_fenetre / 200,
                self.hauteur_fenetre / 20,
                image=self.etoilegrise,
            ),
        ]
        self.niveaucanva = tk.Canvas(
            self,
            width=self.hauteur_fenetre * 8 / 5,
            height=self.hauteur_fenetre * 4 / 5,
            bg="papaya whip",
            borderwidth=0,
            highlightthickness=0,
        )

        self.creditcanva = tk.Canvas(
            self,
            width=self.hauteur_fenetre * 8 / 5,
            height=self.hauteur_fenetre * 4 / 5,
            bg="papaya whip",
            borderwidth=0,
            highlightthickness=0,
        )
        self.creditcanva.create_text(
            self.hauteur_fenetre * 4 / 5,
            self.hauteur_fenetre * 1 / 5,
            anchor="center",
            font="Helvetica " + str(int(5 * self.hauteur_fenetre / 100)) + " bold",
            text="programmeur:\nBenharrous Eytan\nJoly Lisa\nPuerta Oriane\nFiant Violette\n\nEncadrant: Nasr Alexis",
        )
        self.niveaucanva.bind("<ButtonRelease-1>", self.declickniveau)
        self.niveaucanva.bind("<Button-1>", self.clickniveau)
        self.actifniveauselect = None
        self.listeniveau = []
        self.niveauvalidé = []
        fichier = open("projet tortuga/usopp.txt", "r")

        donnée = fichier.readlines()
        self.pouvoirunlock = int(donnée[1])
        niveau = donnée[0]
        self.emojie = int(donnée[2][0])
        self.nourriture = int(donnée[3][0])
        self.skindebloque = donnée[2][1:]
        self.nourrituredebloque = donnée[3][1:]
        self.anciennecombine = donnée[4]
        fichier.close()
        self.niveaucanva.create_text(
            self.hauteur_fenetre * 4 / 5,
            self.hauteur_fenetre / 20,
            font="Helvetica " + str(int(4 * self.hauteur_fenetre / 100)) + " bold",
            anchor="center",
            text="niveau éducatif",
            fill="black",
        )
        self.niveaucanva.create_text(
            self.hauteur_fenetre * 4 / 5,
            self.hauteur_fenetre / 20 + 32 * self.hauteur_fenetre / 100,
            font="Helvetica " + str(int(4 * self.hauteur_fenetre / 100)) + " bold",
            anchor="center",
            text="niveau de divertissement",
            fill="black",
        )
        self.trans = ImageTk.PhotoImage(Image.open("projet tortuga/trans.png"))
        for i in range(2):
            for j in range(8):
                self.listeniveau.append(
                    (
                        self.niveaucanva.create_rectangle(
                            3 * self.hauteur_fenetre / 100
                            + 2 * self.hauteur_fenetre / 10 * j,
                            12 * self.hauteur_fenetre / 100
                            + 12 * self.hauteur_fenetre / 100 * i,
                            17 * self.hauteur_fenetre / 100
                            + 2 * self.hauteur_fenetre / 10 * j,
                            2 * self.hauteur_fenetre / 10
                            + 12 * self.hauteur_fenetre / 100 * i,
                            fill="light grey",
                        ),
                        self.niveaucanva.create_text(
                            10 * self.hauteur_fenetre / 100
                            + 2 * self.hauteur_fenetre / 10 * j,
                            18 * self.hauteur_fenetre / 100
                            + 12 * self.hauteur_fenetre / 100 * i,
                            anchor="center",
                            text=str(i * 8 + j + 1),
                            font=("Helvetica", int(self.hauteur_fenetre / 50), "bold"),
                        ),
                        self.niveaucanva.create_image(
                            3 * self.hauteur_fenetre / 100
                            + 2 * self.hauteur_fenetre / 10 * j
                            + 5 * self.hauteur_fenetre / 200,
                            12 * self.hauteur_fenetre / 100
                            + 12 * self.hauteur_fenetre / 100 * i
                            + self.hauteur_fenetre / 200,
                            image=self.etoilegrise2,
                            anchor="n",
                        ),
                        self.niveaucanva.create_image(
                            10 * self.hauteur_fenetre / 100
                            + 2 * self.hauteur_fenetre / 10 * j,
                            12 * self.hauteur_fenetre / 100
                            + 12 * self.hauteur_fenetre / 100 * i
                            + self.hauteur_fenetre / 200,
                            image=self.etoilegrise2,
                            anchor="n",
                        ),
                        self.niveaucanva.create_image(
                            17 * self.hauteur_fenetre / 100
                            + 2 * self.hauteur_fenetre / 10 * j
                            - 5 * self.hauteur_fenetre / 200,
                            12 * self.hauteur_fenetre / 100
                            + 12 * self.hauteur_fenetre / 100 * i
                            + self.hauteur_fenetre / 200,
                            image=self.etoilegrise2,
                            anchor="n",
                        ),
                    )
                )
                if niveau[i * 8 + j] == "1":
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][0], fill="light green"
                    )
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][2], image=self.etoilejaune2
                    )
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][3], image=self.etoilegrise2
                    )
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][4], image=self.etoilegrise2
                    )
                    self.niveauvalidé.append(True)
                elif niveau[i * 8 + j] == "2":
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][0], fill="light green"
                    )
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][2], image=self.etoilejaune2
                    )
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][3], image=self.etoilejaune2
                    )
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][4], image=self.etoilegrise2
                    )
                    self.niveauvalidé.append(True)
                elif niveau[i * 8 + j] == "3":
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][0], fill="light green"
                    )
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][2], image=self.etoilejaune2
                    )
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][3], image=self.etoilejaune2
                    )
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][4], image=self.etoilejaune2
                    )
                    self.niveauvalidé.append(True)
                elif niveau[i * 8 + j - 1] in ["1", "2", "3"]:
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][0], fill="lightskyblue2"
                    )
                    self.actifniveau = i * 8 + j
                    self.niveauvalidé.append(False)
                else:
                    self.niveauvalidé.append(False)
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][2], image=self.trans
                    )
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][3], image=self.trans
                    )
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][4], image=self.trans
                    )
        for i in range(2, 5):
            for j in range(8):
                self.listeniveau.append(
                    (
                        self.niveaucanva.create_rectangle(
                            3 * self.hauteur_fenetre / 100
                            + 2 * self.hauteur_fenetre / 10 * j,
                            22 * self.hauteur_fenetre / 100
                            + 12 * self.hauteur_fenetre / 100 * i,
                            17 * self.hauteur_fenetre / 100
                            + 2 * self.hauteur_fenetre / 10 * j,
                            3 * self.hauteur_fenetre / 10
                            + 12 * self.hauteur_fenetre / 100 * i,
                            fill="light grey",
                        ),
                        self.niveaucanva.create_text(
                            10 * self.hauteur_fenetre / 100
                            + 2 * self.hauteur_fenetre / 10 * j,
                            28 * self.hauteur_fenetre / 100
                            + 12 * self.hauteur_fenetre / 100 * i,
                            anchor="center",
                            text=str(i * 8 + j + 1),
                            font=("Helvetica", int(self.hauteur_fenetre / 50), "bold"),
                        ),
                        self.niveaucanva.create_image(
                            3 * self.hauteur_fenetre / 100
                            + 2 * self.hauteur_fenetre / 10 * j
                            + 5 * self.hauteur_fenetre / 200,
                            22 * self.hauteur_fenetre / 100
                            + 12 * self.hauteur_fenetre / 100 * i
                            + self.hauteur_fenetre / 200,
                            image=self.etoilegrise2,
                            anchor="n",
                        ),
                        self.niveaucanva.create_image(
                            10 * self.hauteur_fenetre / 100
                            + 2 * self.hauteur_fenetre / 10 * j,
                            22 * self.hauteur_fenetre / 100
                            + 12 * self.hauteur_fenetre / 100 * i
                            + self.hauteur_fenetre / 200,
                            image=self.etoilegrise2,
                            anchor="n",
                        ),
                        self.niveaucanva.create_image(
                            17 * self.hauteur_fenetre / 100
                            + 2 * self.hauteur_fenetre / 10 * j
                            - 5 * self.hauteur_fenetre / 200,
                            22 * self.hauteur_fenetre / 100
                            + 12 * self.hauteur_fenetre / 100 * i
                            + self.hauteur_fenetre / 200,
                            image=self.etoilegrise2,
                            anchor="n",
                        ),
                    )
                )
                if niveau[i * 8 + j] == "1":
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][0], fill="light green"
                    )
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][2], image=self.etoilejaune2
                    )
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][3], image=self.etoilegrise2
                    )
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][4], image=self.etoilegrise2
                    )
                    self.niveauvalidé.append(True)
                elif niveau[i * 8 + j] == "2":
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][0], fill="light green"
                    )
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][2], image=self.etoilejaune2
                    )
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][3], image=self.etoilejaune2
                    )
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][4], image=self.etoilegrise2
                    )
                    self.niveauvalidé.append(True)
                elif niveau[i * 8 + j] == "3":
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][0], fill="light green"
                    )
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][2], image=self.etoilejaune2
                    )
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][3], image=self.etoilejaune2
                    )
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][4], image=self.etoilejaune2
                    )
                    self.niveauvalidé.append(True)
                elif niveau[i * 8 + j - 1] in ["1", "2", "3"]:
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][0], fill="lightskyblue2"
                    )
                    self.actifniveau = i * 8 + j
                    self.niveauvalidé.append(False)
                else:
                    self.niveauvalidé.append(False)
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][2], image=self.trans
                    )
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][3], image=self.trans
                    )
                    self.niveaucanva.itemconfig(
                        self.listeniveau[i * 8 + j][4], image=self.trans
                    )
        if not self.niveauvalidé[0]:
            self.niveaucanva.itemconfig(self.listeniveau[0][0], fill="lightskyblue2")
        self.blanc1 = [
            tk.Canvas(
                self,
                width=self.hauteur_fenetre / 5,
                height=self.hauteur_fenetre / 5,
                bg="papaya whip",
                borderwidth=0,
                highlightthickness=0,
            )
            for i in range(2)
        ]

        self.continuer = tk.Button(
            self,
            text="continuer",
            font="Helvetica " + str(int(4 * self.hauteur_fenetre / 100)) + " bold",
            bg="lightskyblue2",
            activebackground="lightskyblue1",
            command=lambda: [
                self.continuer.pack_forget(),
                self.blanc1[0].pack_forget(),
                self.blanc2[0].pack_forget(),
                self.blanc2[1].pack_forget(),
                self.parametre.pack_forget(),
                self.niveau.pack_forget(),
                self.titre.pack_forget(),
                self.blanc2[2].pack_forget(),
                self.skin.pack_forget(),
                self.menu.pack_forget(),
                self.pack(),
                self.assigne(True),
            ],
        )
        self.menu = tk.Button(
            self,
            text="Menu",
            font="Helvetica " + str(int(4 * self.hauteur_fenetre / 100)) + " bold",
            bg="lightskyblue2",
            activebackground="lightskyblue1",
            command=lambda: [
                self.continuer.pack_forget(),
                self.blanc1[0].pack_forget(),
                self.blanc2[0].pack_forget(),
                self.blanc2[1].pack_forget(),
                self.parametre.pack_forget(),
                self.niveau.pack_forget(),
                self.titre.pack_forget(),
                self.menu.pack_forget(),
                self.niveaucanva.pack_forget(),
                self.creditcanva.pack_forget(),
                self.selectskin.pack_forget(),
                self.diamant.pack(),
                self.titre.pack(),
                self.continuer.pack(),
                self.blanc2[0].pack(),
                self.niveau.pack(),
                self.blanc2[1].pack(),
                self.parametre.pack(),
                self.blanc2[2].pack(),
                self.skin.pack(),
                self.assigne(False),
            ],
        )
        self.blanc2 = [
            tk.Canvas(
                self,
                width=self.hauteur_fenetre / 5,
                height=self.hauteur_fenetre / 20,
                bg="papaya whip",
                borderwidth=0,
                highlightthickness=0,
            )
            for i in range(3)
        ]
        self.variable = tk.StringVar(self, value="y")
        self.frameposition = tk.Frame(self)
        self.positionx = tk.Radiobutton(
            self.frameposition,
            variable=self.variable,
            value="x",
            text="vertical",
            font="Helvetica " + str(int(4 * self.hauteur_fenetre / 100)) + " bold",
            background="papaya whip",
            activebackground="papaya whip",
            highlightthickness=0,
        )
        self.positiony = tk.Radiobutton(
            self.frameposition,
            variable=self.variable,
            value="y",
            text="horizontale",
            font="Helvetica " + str(int(4 * self.hauteur_fenetre / 100)) + " bold",
            background="papaya whip",
            activebackground="papaya whip",
            highlightthickness=0,
        )

        self.orientation = tk.Label(
            self,
            text="orientation",
            font="Helvetica " + str(int(4 * self.hauteur_fenetre / 100)) + " bold",
            background="light grey",
            border=1,
            highlightbackground="black",
            highlightcolor="black",
            highlightthickness=1,
        )
        self.positionx.pack(side="left"),
        self.positiony.pack(side="right"),
        self.reinisialise = tk.Button(
            self,
            text="effacer les données",
            font="Helvetica " + str(int(3 * self.hauteur_fenetre / 100)) + " bold",
            bg="lightskyblue2",
            activebackground="lightskyblue1",
            command=self.reinisialisation,
        )
        self.valider = tk.Button(
            self,
            text="valider",
            font="Helvetica " + str(int(4 * self.hauteur_fenetre / 100)) + " bold",
            bg="lightskyblue2",
            activebackground="lightskyblue1",
            command=lambda: [
                self.reinisialise.pack_forget(),
                self.blanc2[0].pack_forget(),
                self.blanc2[1].pack_forget(),
                self.frameposition.pack_forget(),
                self.blanc1[0].pack_forget(),
                self.valider.pack_forget(),
                self.orientation.pack_forget(),
                self.blanc1[0].pack(),
                self.continuer.pack(),
                self.blanc2[0].pack(),
                self.parametre.pack(),
                self.blanc2[1].pack(),
                self.menu.pack(),
            ]
            if self.enjeu
            else [
                self.reinisialise.pack_forget(),
                self.blanc2[0].pack_forget(),
                self.blanc2[1].pack_forget(),
                self.frameposition.pack_forget(),
                self.blanc1[0].pack_forget(),
                self.valider.pack_forget(),
                self.orientation.pack_forget(),
                self.diamant.pack(),
                self.titre.pack(),
                self.continuer.pack(),
                self.blanc2[0].pack(),
                self.niveau.pack(),
                self.blanc2[1].pack(),
                self.parametre.pack(),
                self.blanc2[2].pack(),
                self.skin.pack(),
            ],
        )
        self.niveau = tk.Button(
            self,
            text="sélection du niveau",
            font="Helvetica " + str(int(4 * self.hauteur_fenetre / 100)) + " bold",
            bg="lightskyblue2",
            activebackground="lightskyblue1",
            command=lambda: [
                self.blanc2[0].pack_forget(),
                self.parametre.pack_forget(),
                self.blanc2[1].pack_forget(),
                self.continuer.pack_forget(),
                self.niveau.pack_forget(),
                self.titre.pack_forget(),
                self.blanc2[2].pack_forget(),
                self.skin.pack_forget(),
                self.niveaucanva.pack(),
                self.menu.pack(),
            ],
        )
        self.parametre = tk.Button(
            self,
            text="parametre",
            font="Helvetica " + str(int(4 * self.hauteur_fenetre / 100)) + " bold",
            bg="lightskyblue2",
            activebackground="lightskyblue1",
            command=lambda: [
                self.continuer.pack_forget(),
                self.blanc1[0].pack_forget(),
                self.blanc2[0].pack_forget(),
                self.parametre.pack_forget(),
                self.blanc2[1].pack_forget(),
                self.niveau.pack_forget(),
                self.titre.pack_forget(),
                self.diamant.pack_forget(),
                self.menu.pack_forget(),
                self.blanc2[2].pack_forget(),
                self.skin.pack_forget(),
                self.blanc1[0].pack(),
                self.orientation.pack(),
                self.frameposition.pack(),
                self.blanc2[0].pack(),
                self.reinisialise.pack(),
                self.blanc2[1].pack(),
                self.valider.pack(),
            ],
        )
        self.skin = tk.Button(
            self,
            text="cosmétique",
            font="Helvetica " + str(int(4 * self.hauteur_fenetre / 100)) + " bold",
            bg="lightskyblue2",
            activebackground="lightskyblue1",
            command=lambda: [
                self.continuer.pack_forget(),
                self.blanc1[0].pack_forget(),
                self.blanc2[0].pack_forget(),
                self.parametre.pack_forget(),
                self.blanc2[1].pack_forget(),
                self.niveau.pack_forget(),
                self.titre.pack_forget(),
                self.menu.pack_forget(),
                self.blanc2[2].pack_forget(),
                self.skin.pack_forget(),
                self.selectskin.pack(),
                [
                    self.droitedebloque.config(
                        bg="firebrick3",
                        activebackground="firebrick2",
                        text="diamants insuffisants",
                    ),
                    self.gauchedebloque.config(
                        bg="firebrick3",
                        activebackground="firebrick2",
                        text="diamants insuffisants",
                    ),
                ]
                if self.comptediamant < 10
                else [
                    self.droitedebloque.config(
                        bg="turquoise3",
                        activebackground="turquoise2",
                        text="débloquer (10 diamants)",
                    ),
                    self.gauchedebloque.config(
                        bg="turquoise3",
                        activebackground="turquoise2",
                        text="débloquer (10 diamants)",
                    ),
                ],
                self.menu.pack(),
            ],
        )
        self.selectskin = tk.Frame(
            self,
            width=self.hauteur_fenetre * 8 / 5,
            height=self.hauteur_fenetre * 4 / 5,
            bg="papaya whip",
            borderwidth=0,
            highlightthickness=0,
        )
        self.prepareskin()
        self.zonejeu = tk.Frame(
            self,
            bg="papaya whip",
            borderwidth=0,
            highlightthickness=0,
        )
        self.canva = tk.Canvas(
            self.zonejeu,
            width=73,
            height=42,
            bg="mint cream",
            borderwidth=0,
            highlightthickness=1,
            highlightbackground="black",
        )
        self.blanc4 = tk.Canvas(
            self.zonejeu,
            width=2 * self.hauteur_fenetre / 100,
            bg="papaya whip",
            borderwidth=0,
            highlightthickness=0,
        )

        self.canva2 = tk.Canvas(
            self.zonejeu,
            width=73,
            height=42,
            bg="mint cream",
            borderwidth=0,
            highlightthickness=1,
            highlightbackground="black",
        )

        self.bouton = tk.Canvas(
            self,
            width=self.hauteur_fenetre * 9 / 10,
            height=3 * self.hauteur_fenetre / 10,
            bg="papaya whip",
            borderwidth=0,
            highlightthickness=0,
        )
        self.bouton.bind("<Button-1>", self.click)
        self.bouton.bind("<ButtonRelease-1>", self.declick)
        self.canva.bind("<Button-1>", self.click2)
        self.canva.bind("<ButtonRelease-1>", self.declick2)
        self.canva.bind("<B1-Motion>", self.motion)
        self.systeme = ttk.Combobox(
            width=22,
            font="Helvetica " + str(int(2 * self.hauteur_fenetre / 100)) + " bold",
            state="readonly",
        )
        self.systeme.bind("<<ComboboxSelected>>", self.changesysteme)
        self.canva.bind(
            "<KeyRelease>",
            lambda event: self.canva.config(
                width=self.largeur,
                height=self.hauteur,
            )
            if self.variable.get() == "x"
            else self.canva.config(
                height=self.largeur,
                width=self.hauteur,
            ),
        )

        screen_width = self.winfo_width()
        self.titre = tk.Frame(self, bg="papaya whip")
        self.diamant = tk.Canvas(
            self,
            height=self.hauteur_fenetre / 20,
            width=self.largeur_fenetre,
            background="papaya whip",
            borderwidth=0,
            highlightthickness=0,
        )
        self.imdiamant = ImageTk.PhotoImage(
            Image.open("projet tortuga/diamant.png").resize(
                (4 * self.hauteur_fenetre // 100, 4 * self.hauteur_fenetre // 100)
            )
        )
        self.diamant.create_image(
            self.largeur_fenetre - self.hauteur_fenetre / 20,
            5 * self.hauteur_fenetre / 200,
            image=self.imdiamant,
        )
        self.comptediamant = 0
        for i in donnée[0][:-1]:
            self.comptediamant += int(i)
        for i in donnée[2][2:-1]:
            self.comptediamant -= 10 * int(i)
        for i in donnée[3][2:-1]:
            self.comptediamant -= 10 * int(i)
        self.nombrediamant = self.diamant.create_text(
            self.largeur_fenetre - self.hauteur_fenetre / 10,
            5 * self.hauteur_fenetre / 200,
            text=str(self.comptediamant),
            font="Helvetica " + str(int(3 * self.hauteur_fenetre / 100)) + " bold",
        )
        self.logoimage = ImageTk.PhotoImage(
            Image.open("projet tortuga/tortuga.png").resize(
                (36 * self.hauteur_fenetre // 100, 36 * self.hauteur_fenetre // 100)
            )
        )
        self.gaussimage = ImageTk.PhotoImage(
            Image.open("projet tortuga/tortugauss.png").resize(
                (85 * self.hauteur_fenetre // 100, 18 * self.hauteur_fenetre // 100)
            )
        )
        self.logo = tk.Label(self.titre, image=self.logoimage, bg="papaya whip")
        self.logo.pack(side="left")
        self.tortugauss = tk.Label(self.titre, image=self.gaussimage, bg="papaya whip")

        # définition des matrices associé au niveau
        self.actifX = np.ones(len(self.actifA))
        self.listemultiplicateur = [1] * len(self.actifA)
        self.gauss1actif = 0
        self.gauss2actif = 0
        frames = []
        self.frames = [[], [], [], [], [], [], []]
        im = Image.open("projet tortuga/mygif.gif")
        try:
            im.seek(1)
            for i in count(1):
                frames.append(im.copy())
                im.seek(i)
        except EOFError:
            pass

        self.frames[0] = frames
        self.frames0 = [0 for i in range(len(self.actifA))]
        self.frames1 = [[], [], [], [], [], [], []]
        self.delay = []
        try:
            self.delay.append(im.info["duration"])
        except:
            self.delay.append(100)

        frames = []
        im = Image.open("projet tortuga/mygif2.gif")
        try:
            im.seek(1)
            for i in count(1):
                frames.append(im.copy())
                im.seek(i)
        except EOFError:
            pass

        self.frames[1] = frames
        try:
            self.delay.append(im.info["duration"])
        except:
            self.delay.append(100)

        frames = []
        im = Image.open("projet tortuga/mygif3.gif")
        try:
            im.seek(1)
            for i in count(1):
                frames.append(im.copy())
                im.seek(i)
        except EOFError:
            pass

        self.frames[2] = frames
        try:
            self.delay.append(im.info["duration"])
        except:
            self.delay.append(100)
        frames = []
        im = Image.open("projet tortuga/mygif4.gif")
        try:
            im.seek(1)
            for i in count(1):
                frames.append(im.copy())
                im.seek(i)
        except EOFError:
            pass

        self.frames[3] = frames
        try:
            self.delay.append(im.info["duration"])
        except:
            self.delay.append(100)
        frames = []
        im = Image.open("projet tortuga/mygif5.gif")
        try:
            im.seek(1)
            for i in count(1):
                frames.append(im.copy())
                im.seek(i)
        except EOFError:
            pass

        self.frames[4] = frames
        try:
            self.delay.append(im.info["duration"])
        except:
            self.delay.append(100)
        frames = []
        im = Image.open("projet tortuga/mygif6.gif")
        try:
            im.seek(1)
            for i in count(1):
                frames.append(im.copy())
                im.seek(i)
        except EOFError:
            pass

        self.frames[5] = frames
        try:
            self.delay.append(im.info["duration"] / 2)
        except:
            self.delay.append(50)
        frames = []
        im = Image.open("projet tortuga/mygif7.gif")
        try:
            im.seek(1)
            for i in count(1):
                frames.append(im.copy())
                im.seek(i)
        except EOFError:
            pass

        self.frames[6] = frames
        try:
            self.delay.append(im.info["duration"] / 2)
        except:
            self.delay.append(50)

        self.coup = 0
        self.gifcheck = [False for k in self.actifA]

        self.codegif = [0 for k in self.actifA]
        self.gifcheck2 = [False for k in self.actifA]

        self.codegif2 = [0 for k in self.actifA]
        self.systeme.set("niveau " + str(self.actifniveau + 1))
        self.itemcoup = self.pause.create_text(
            self.largeur_fenetre / 2,
            self.hauteur_fenetre / 20,
            font="Helvetica " + str(int(4 * self.hauteur_fenetre / 100)) + " bold",
            anchor="center",
            text="nombre de coups: 000/" + str(self.listeetoile[self.actifniveau][0]),
            fill="black",
        )
        self.gagne = tk.Frame(
            self,
            background="white",
            border=1,
            highlightbackground="black",
            highlightcolor="black",
            highlightthickness=1,
        )
        self.etoile = tk.Canvas(
            self.gagne,
            height=30 * self.hauteur_fenetre / 100,
            width=3 * self.hauteur_fenetre / 5,
            background="white",
            border=0,
            highlightthickness=0,
        )
        self.menu2 = tk.Button(
            self.gagne,
            text="Menu",
            font="Helvetica " + str(int(3 * self.hauteur_fenetre / 100)) + " bold",
            bg="lightskyblue2",
            activebackground="lightskyblue1",
            command=lambda: [
                self.gagne.place_forget(),
                self.changesysteme("niveau 0" + str(self.actifniveau + 2)),
                self.unpack(),
                self.diamant.pack(),
                self.titre.pack(),
                self.continuer.pack(),
                self.blanc2[0].pack(),
                self.niveau.pack(),
                self.blanc2[1].pack(),
                self.parametre.pack(),
                self.blanc2[2].pack(),
                self.skin.pack(),
                self.assigne(False),
            ],
        )
        self.blanc3 = [
            tk.Canvas(
                self.gagne,
                width=self.hauteur_fenetre / 5,
                height=self.hauteur_fenetre / 20,
                bg="white",
                borderwidth=0,
                highlightthickness=0,
            )
            for i in range(3)
        ]
        self.continuer2 = tk.Button(
            self.gagne,
            text="niveau suivant",
            font="Helvetica " + str(int(3 * self.hauteur_fenetre / 100)) + " bold",
            bg="lightskyblue2",
            activebackground="lightskyblue1",
            command=lambda: [
                self.unpack(),
                self.gagne.place_forget(),
                self.changesysteme("niveau 0" + str(self.actifniveau + 2)),
                self.pack(),
            ],
        )

        self.réessayer = tk.Button(
            self.gagne,
            text="réessayer",
            font="Helvetica " + str(int(3 * self.hauteur_fenetre / 100)) + " bold",
            bg="lightskyblue2",
            activebackground="lightskyblue1",
            command=lambda: [
                self.gagne.place_forget(),
                self.reesaye(),
            ],
        )

        self.etoile.pack()
        self.remarque = remarque(
            self.gagne,
            ["test"],
            "Helvetica " + str(int(2 * self.hauteur_fenetre / 100)) + " bold",
            4 * self.hauteur_fenetre / 100,
            6 * self.hauteur_fenetre / 10,
        )
        self.continuer2.pack()
        self.blanc3[2].pack()
        self.réessayer.pack()
        self.blanc3[1].pack()
        self.menu2.pack()
        self.blanc3[0].pack()

        self.changesysteme("Lisa est un astronaute")
        self.listeaction = []
        self.tortugauss.pack(side="right")
        self.diamant.pack(),
        self.titre.pack()
        self.continuer.pack()
        self.blanc2[0].pack()
        self.niveau.pack()
        self.blanc2[1].pack()
        self.parametre.pack()
        self.blanc2[2].pack(),
        self.skin.pack(),
        self.chargement.pack_forget()

    def changesysteme(self, event):
        systeme = int(self.systeme.get()[-2] + self.systeme.get()[-1]) - 1
        self.actifniveau = systeme
        self.actifA = self.listeA[systeme]
        if self.actifniveau == 11:
            self.actifA2 = np.array(
                [[1, 1, 1], [0, 2, 4], [0, 0, 4]], dtype=np.float64
            )  # 12
        elif self.actifniveau == 12:
            self.actifA2 = self.listeA[self.actifniveau].copy()
        elif self.actifniveau == 14:
            self.actifA2 = self.listeA[self.actifniveau].copy()
        else:
            self.actifA2 = np.array([[2, 0], [2, 2]], dtype=np.float64)
        self.listeaction = []
        self.gifcheck = [False for k in self.actifA]
        self.codegif = [0 for k in self.actifA]
        self.gifcheck2 = [False for k in self.actifA]
        self.codegif2 = [0 for k in self.actifA]
        self.actifB = self.listeB[systeme]
        if self.actifniveau == 11:
            self.actifB2 = np.array([1.3, -3.8, -4.0], dtype=np.float64)  # 12 triang
        elif self.actifniveau == 12:
            self.actifB2 = self.listeB[self.actifniveau].copy()
        elif self.actifniveau == 14:
            self.actifB2 = self.listeB[self.actifniveau].copy()
        else:
            self.actifB2 = np.array([4, 7], dtype=np.float64)
        self.actifAi = self.listeA[systeme].copy()
        self.actifBi = self.listeB[systeme].copy()
        self.actifX = np.ones(len(self.actifA))
        self.listemultiplicateur = [1] * len(self.actifA)
        self.listeovalgauss = []
        self.coup = 0
        self.pause.itemconfig(
            self.itemcoup,
            text="nombre de coups: 000/" + str(self.listeetoile[systeme][0]),
        )
        self.gaussemplacement = [0, 0, 0, 0]
        self.pause.itemconfig(self.pauseetoile[2], image=self.etoilejaune)
        self.pause.itemconfig(self.pauseetoile[1], image=self.etoilejaune)
        self.preparecanva()
        self.canva2.delete("all")
        self.preparebouton()

    def preparecanva(self):
        self.stop = True
        self.listerectangle = []
        self.listeboule = []
        self.frames0 = [0 for i in range(len(self.actifA))]
        self.frames1 = [[], [], [], [], [], [], []]
        self.listefleche = []
        self.listeovalgauss = []
        self.canva.delete("all")

        self.pause.itemconfig(
            self.itemniveau, text="niveau " + str(self.actifniveau + 1)
        )
        if self.variable.get() == "x":
            self.echelle = 3 * self.hauteur_fenetre / 100

            self.largeur = 6.5 * self.hauteur_fenetre / 10
        else:
            self.echelle = 5 * self.hauteur_fenetre / 100
            self.largeur = 5 * self.hauteur_fenetre / 10
        self.echellex = self.echelle / len(self.actifA)
        self.hauteur = (len(self.actifA)) * (self.echelle + 1) * len(
            self.actifA
        ) + self.echelle * len(self.actifA)
        if self.variable.get() == "x":
            if self.actifniveau == 12:
                self.canva.config(
                    width=self.largeur + 2 * self.hauteur_fenetre / 10,
                    height=self.hauteur + self.hauteur_fenetre / 10,
                )
            elif self.actifniveau == 14 or self.actifniveau == 15:
                self.canva.config(
                    width=self.largeur + 2 * self.hauteur_fenetre / 10,
                    height=self.hauteur + self.hauteur_fenetre / 10,
                )
            else:
                self.canva.config(
                    height=self.hauteur,
                    width=self.largeur,
                )

            increment = 0
            # ligne du quadrillage
            for k in range(len(self.actifA) + 1):
                self.canva.create_line(
                    0,
                    (self.echelle + 1) * k,
                    self.largeur + 1,
                    (self.echelle + 1) * k,
                    width=1,
                    fill="grey73",
                )
            self.canva.create_rectangle(
                0,
                (self.echelle + 1) * k,
                self.largeur,
                (self.echelle + 1) * k + self.echelle + 1,
                width=1,
                fill="grey89",
                outline="red",
            )
            for i in range(len(self.actifA)):
                self.canva.create_line(
                    0,
                    (self.echelle + 1) * (len(self.actifA) + 1) + increment,
                    self.largeur + 1,
                    (self.echelle + 1) * (len(self.actifA) + 1) + increment,
                    width=1,
                    fill="black",
                )

                increment += self.echelle + 1
                for k in range(len(self.actifA)):
                    self.canva.create_line(
                        0,
                        (self.echelle + 1) * (len(self.actifA) + 1) + increment,
                        self.largeur,
                        (self.echelle + 1) * (len(self.actifA) + 1) + increment,
                        width=1,
                        fill="grey73",
                    )
                    increment += self.echelle + 1
                self.canva.create_rectangle(
                    0,
                    (self.echelle + 1) * (len(self.actifA) + 1)
                    + increment
                    - self.echelle
                    - 1,
                    self.largeur,
                    (self.echelle + 1) * (len(self.actifA) + 1) + increment,
                    width=1,
                    fill="grey89",
                    outline="red",
                )
            increment = 0
            # rectangle
            for i in range(len(self.actifA)):
                listelocal = []
                for j in range(len(self.actifA)):
                    rectanglelocal = self.canva.create_rectangle(
                        self.largeur // 2,
                        increment,
                        self.largeur // 2
                        + self.actifA[i][j] * self.actifX[j] * (self.echellex + 1),
                        increment + self.echelle + 1,
                        width=1,
                        fill=self.couleurs[j],
                    )
                    if self.actifniveau == 2:
                        self.canva.create_line(
                        self.largeur // 2
                        + self.actifA[i][j] * self.actifX[j] * (self.echellex + 1),
                        increment,
                        self.largeur // 2
                        + self.actifA[i][j] * self.actifX[j] * (self.echellex + 1),
                        increment + self.echelle + 1,
                        width=3,
                        fill='red',
                        )
                        self.canva.create_line(
                        self.largeur // 2
                        + self.actifA[i][j] * self.actifX[j] * (self.echellex + 1)-2,
                        increment,
                        self.largeur // 2
                        + self.actifA[i][j] * self.actifX[j] * (self.echellex + 1)-2,
                        increment + self.echelle + 1,
                        width=2,
                        fill='black',
                        )
                        self.canva.create_line(
                        self.largeur // 2
                        + self.actifA[i][j] * self.actifX[j] * (self.echellex + 1)+2,
                        increment,
                        self.largeur // 2
                        + self.actifA[i][j] * self.actifX[j] * (self.echellex + 1)+2,
                        increment + self.echelle + 1,
                        width=2,
                        fill='black',
                        )
                        self.canva.create_line(
                        self.largeur // 2
                        + self.actifA[i][j] * self.actifX[j] * (self.echellex + 1)+2,
                        increment + self.echelle + 1,
                        self.largeur // 2
                        + self.actifA[i][j] * self.actifX[j] * (self.echellex + 1)-2,
                        increment + self.echelle + 1,
                        width=2,
                        fill='black',
                        )
                        self.canva.create_line(
                        self.largeur // 2
                        + self.actifA[i][j] * self.actifX[j] * (self.echellex + 1)+2,
                        increment,
                        self.largeur // 2
                        + self.actifA[i][j] * self.actifX[j] * (self.echellex + 1)-2,
                        increment,
                        width=2,
                        fill='black',
                        )
                    increment += self.echelle + 1
                    listelocal.append(rectanglelocal)
                increment += self.echelle + 1
                self.listerectangle.append(listelocal)

            # ligne du 0
            self.canva.create_line(
                self.largeur // 2,
                0,
                self.largeur // 2,
                self.hauteur + 1 + len(self.actifA),
                width=3,
                fill="gold",
            )
            self.canva.create_line(
                self.largeur // 2 - 2,
                0,
                self.largeur // 2 - 2,
                self.hauteur + 1 + len(self.actifA),
                width=1,
                fill="black",
            )
            self.canva.create_line(
                self.largeur // 2 + 2,
                0,
                self.largeur // 2 + 2,
                self.hauteur + 1 + len(self.actifA),
                width=1,
                fill="black",
            )

            # boule et cercle
            if self.nourriture == 0:
                self.salade = ImageTk.PhotoImage(
                    Image.open("projet tortuga/salade.png").resize(
                        (
                            int(
                                (self.echelle + 1)
                                * (len(self.actifA) * (3 / (4 * len(self.actifA))))
                                + 1
                            ),
                            int((self.echellex + 1) * (len(self.actifA) * 3 / 4) + 1),
                        )
                    )
                )
            elif self.nourriture == 1:
                self.salade = ImageTk.PhotoImage(
                    Image.open("projet tortuga/pizza.png").resize(
                        (
                            int(
                                (self.echelle + 1)
                                * (len(self.actifA) * (3 / (4 * len(self.actifA))))
                                + 1
                            ),
                            int((self.echellex + 1) * (len(self.actifA) * 3 / 4) + 1),
                        )
                    )
                )
            elif self.nourriture == 2:
                self.salade = ImageTk.PhotoImage(
                    Image.open("projet tortuga/bonbon.png").resize(
                        (
                            int(
                                (self.echelle + 1)
                                * (len(self.actifA) * (3 / (4 * len(self.actifA))))
                                + 1
                            ),
                            int((self.echellex + 1) * (len(self.actifA) * 3 / 4) + 1),
                        )
                    )
                )
            elif self.nourriture == 3:
                self.salade = ImageTk.PhotoImage(
                    Image.open("projet tortuga/pasteque.png").resize(
                        (
                            int(
                                (self.echelle + 1)
                                * (len(self.actifA) * (3 / (4 * len(self.actifA))))
                                + 1
                            ),
                            int((self.echellex + 1) * (len(self.actifA) * 3 / 4) + 1),
                        )
                    )
                )
            elif self.nourriture == 4:
                self.salade = ImageTk.PhotoImage(
                    Image.open("projet tortuga/viande.png").resize(
                        (
                            int(
                                (self.echelle + 1)
                                * (len(self.actifA) * (3 / (4 * len(self.actifA))))
                                + 1
                            ),
                            int((self.echellex + 1) * (len(self.actifA) * 3 / 4) + 1),
                        )
                    )
                )
            elif self.nourriture == 5:
                self.salade = ImageTk.PhotoImage(
                    Image.open("projet tortuga/sushi.png").resize(
                        (
                            int(
                                (self.echelle + 1)
                                * (len(self.actifA) * (3 / (4 * len(self.actifA))))
                                + 1
                            ),
                            int((self.echellex + 1) * (len(self.actifA) * 3 / 4) + 1),
                        )
                    )
                )
            elif self.nourriture == 6:
                self.salade = ImageTk.PhotoImage(
                    Image.open("projet tortuga/glace.png").resize(
                        (
                            int(
                                (self.echelle + 1)
                                * (len(self.actifA) * (3 / (4 * len(self.actifA))))
                                + 1
                            ),
                            int((self.echellex + 1) * (len(self.actifA) * 3 / 4) + 1),
                        )
                    )
                )
            for k in range(len(self.actifB)):
                imagelocal = self.canva.create_image(
                    self.largeur // 2
                    + (self.echellex + 1)
                    * (-len(self.actifA) * 3 / 8 + self.actifB[k]),
                    (self.echelle + 1)
                    * ((len(self.actifA)) * (k + 1 + 1 / (8 * len(self.actifA))))
                    + (self.echelle + 1) * k,
                    anchor=tk.NW,
                    image=self.salade,
                )
                flechelocal = self.canva.create_line(
                    self.largeur // 2,
                    (self.echelle + 1)
                    * (len(self.actifA) * (k + 1 + 1 / (2 * len(self.actifA))))
                    + (self.echelle + 1) * k,
                    self.largeur // 2,
                    (self.echelle + 1)
                    * (len(self.actifA) * (k + 1 + 1 / (2 * len(self.actifA))))
                    + (self.echelle + 1) * k,
                    width=10,
                    arrow="last",
                    fill="red",
                )
                if self.canva.coords(imagelocal)[0] > self.largeur:
                    self.canva.coords(
                        flechelocal,
                        self.largeur - self.hauteur_fenetre / 10,
                        (self.echelle + 1)
                        * (len(self.actifA) * (k + 1 + 1 / (2 * len(self.actifA))))
                        + (self.echelle + 1) * k,
                        self.largeur - 4 * self.hauteur_fenetre / 100,
                        (self.echelle + 1)
                        * (len(self.actifA) * (k + 1 + 1 / (2 * len(self.actifA))))
                        + (self.echelle + 1) * k,
                    )
                elif self.canva.coords(imagelocal)[0] < 0:
                    self.canva.coords(
                        flechelocal,
                        self.hauteur_fenetre / 10,
                        (self.echelle + 1)
                        * (len(self.actifA) * (k + 1 + 1 / (2 * len(self.actifA))))
                        + (self.echelle + 1) * k,
                        4 * self.hauteur_fenetre / 100,
                        (self.echelle + 1)
                        * (len(self.actifA) * (k + 1 + 1 / (2 * len(self.actifA))))
                        + (self.echelle + 1) * k,
                    )
                self.listeboule.append([imagelocal])
                self.listefleche.append(flechelocal)
                jauge = 0.2
            if self.emojie == 0:
                self.mimtortue = ImageTk.PhotoImage(
                    Image.open("projet tortuga/tortumim.jpg").resize(
                        (
                            int(
                                (self.echelle + 1)
                                * (len(self.actifA) * (3 / (4 * len(self.actifA))))
                                + 1
                            ),
                            int((self.echellex + 1) * (len(self.actifA) * 3 / 4) + 1),
                        )
                    )
                )
            elif self.emojie == 1:
                self.mimtortue = ImageTk.PhotoImage(
                    Image.open("projet tortuga/escargot.png").resize(
                        (
                            int(
                                (self.echelle + 1)
                                * (len(self.actifA) * (3 / (4 * len(self.actifA))))
                                + 1
                            ),
                            int((self.echellex + 1) * (len(self.actifA) * 3 / 4) + 1),
                        )
                    )
                )
            elif self.emojie == 2:
                self.mimtortue = ImageTk.PhotoImage(
                    Image.open("projet tortuga/t-rex.png").resize(
                        (
                            int(
                                (self.echelle + 1)
                                * (len(self.actifA) * (3 / (4 * len(self.actifA))))
                                + 1
                            ),
                            int((self.echellex + 1) * (len(self.actifA) * 3 / 4) + 1),
                        )
                    )
                )
            elif self.emojie == 3:
                self.mimtortue = ImageTk.PhotoImage(
                    Image.open("projet tortuga/crabe.png").resize(
                        (
                            int(
                                (self.echelle + 1)
                                * (len(self.actifA) * (3 / (4 * len(self.actifA))))
                                + 1
                            ),
                            int((self.echellex + 1) * (len(self.actifA) * 3 / 4) + 1),
                        )
                    )
                )
            elif self.emojie == 4:
                self.mimtortue = ImageTk.PhotoImage(
                    Image.open("projet tortuga/chevre.png").resize(
                        (
                            int(
                                (self.echelle + 1)
                                * (len(self.actifA) * (3 / (4 * len(self.actifA))))
                                + 1
                            ),
                            int((self.echellex + 1) * (len(self.actifA) * 3 / 4) + 1),
                        )
                    )
                )
            elif self.emojie == 5:
                self.mimtortue = ImageTk.PhotoImage(
                    Image.open("projet tortuga/poussin.png").resize(
                        (
                            int(
                                (self.echelle + 1)
                                * (len(self.actifA) * (3 / (4 * len(self.actifA))))
                                + 1
                            ),
                            int((self.echellex + 1) * (len(self.actifA) * 3 / 4) + 1),
                        )
                    )
                )
            elif self.emojie == 6:
                self.mimtortue = ImageTk.PhotoImage(
                    Image.open("projet tortuga/fourmi.png").resize(
                        (
                            int(
                                (self.echelle + 1)
                                * (len(self.actifA) * (3 / (4 * len(self.actifA))))
                                + 1
                            ),
                            int((self.echellex + 1) * (len(self.actifA) * 3 / 4) + 1),
                        )
                    )
                )

            for k in range(len(self.actifA)):
                imagelocal = self.canva.create_image(
                    self.largeur // 2
                    + (self.echellex + 1)
                    * (-len(self.actifA) * 3 / 8 + self.actifA.dot(self.actifX)[k]),
                    (self.echelle + 1)
                    * (len(self.actifA) * (k + 1 + 1 / (8 * len(self.actifA))))
                    + (self.echelle + 1) * k,
                    anchor=tk.NW,
                    image=self.mimtortue,
                )
                self.listeboule[k].append(imagelocal)
            self.a = 0

        else:
            if self.actifniveau == 12:
                self.canva.config(
                    height=self.largeur + 0.95 * self.hauteur_fenetre / 10,
                    width=self.hauteur + 2 * self.hauteur_fenetre / 10,
                )
            elif self.actifniveau == 14 or self.actifniveau == 15:
                self.canva.config(
                    height=self.largeur + 1.35 * self.hauteur_fenetre / 10,
                    width=self.hauteur + 2 * self.hauteur_fenetre / 10,
                )
            else:
                self.canva.config(
                    height=self.largeur,
                    width=self.hauteur,
                )
            increment = 0
            # ligne du quadrillage
            for k in range(len(self.actifA) + 1):
                self.canva.create_line(
                    (self.echelle + 1) * k,
                    0,
                    (self.echelle + 1) * k,
                    self.largeur + 1,
                    width=1,
                    fill="grey73",
                )
            self.canva.create_rectangle(
                (self.echelle + 1) * k,
                0,
                (self.echelle + 1) * k + self.echelle + 1,
                self.largeur,
                width=1,
                fill="grey89",
                outline="red",
            )
            for i in range(len(self.actifA) - 1):
                self.canva.create_line(
                    (self.echelle + 1) * (len(self.actifA) + 1) + increment,
                    0,
                    (self.echelle + 1) * (len(self.actifA) + 1) + increment,
                    self.largeur + 1,
                    width=1,
                    fill="black",
                )

                increment += self.echelle + 1
                for k in range(len(self.actifA)):
                    self.canva.create_line(
                        (self.echelle + 1) * (len(self.actifA) + 1) + increment,
                        0,
                        (self.echelle + 1) * (len(self.actifA) + 1) + increment,
                        self.largeur,
                        width=1,
                        fill="grey73",
                    )
                    increment += self.echelle + 1
                self.canva.create_rectangle(
                    (self.echelle + 1) * (len(self.actifA) + 1)
                    + increment
                    - self.echelle
                    - 1,
                    0,
                    (self.echelle + 1) * (len(self.actifA) + 1) + increment,
                    self.largeur,
                    width=1,
                    fill="grey89",
                    outline="red",
                )

            increment = 0
            # rectangle
            for i in range(len(self.actifA)):
                listelocal = []
                
                for j in range(len(self.actifA)):

                    
                    rectanglelocal = self.canva.create_rectangle(
                        increment,
                        self.largeur // 2,
                        increment + self.echelle + 1,
                        self.largeur // 2
                        - self.actifA[i][j] * self.actifX[j] * (self.echellex + 1),
                        width=1,
                        fill=self.couleurs[j],
                    )
                    if self.actifniveau == 2:
                        self.canva.create_line(
                        increment,
                        self.largeur // 2
                        - self.actifA[i][j] * self.actifX[j] * (self.echellex + 1),
                        increment + self.echelle + 1,
                        self.largeur // 2
                        - self.actifA[i][j] * self.actifX[j] * (self.echellex + 1),
                        width=3,
                        fill='red',
                        )
                        self.canva.create_line(
                        increment,
                        self.largeur // 2
                        - self.actifA[i][j] * self.actifX[j] * (self.echellex + 1)+2,
                        increment + self.echelle + 1,
                        self.largeur // 2
                        - self.actifA[i][j] * self.actifX[j] * (self.echellex + 1)+2,
                        width=2,
                        fill='black',
                        )
                        self.canva.create_line(
                        increment,
                        self.largeur // 2
                        - self.actifA[i][j] * self.actifX[j] * (self.echellex + 1)-2,
                        increment + self.echelle + 1,
                        self.largeur // 2
                        - self.actifA[i][j] * self.actifX[j] * (self.echellex + 1)-2,
                        width=2,
                        fill='black',
                        )
                        self.canva.create_line(
                        increment,
                        self.largeur // 2
                        - self.actifA[i][j] * self.actifX[j] * (self.echellex + 1)+2,
                        increment,
                        self.largeur // 2
                        - self.actifA[i][j] * self.actifX[j] * (self.echellex + 1)-2,
                        width=2,
                        fill='black',
                        )
                        self.canva.create_line(
                        increment + self.echelle + 1,
                        self.largeur // 2
                        - self.actifA[i][j] * self.actifX[j] * (self.echellex + 1)+2,
                        increment + self.echelle + 1,
                        self.largeur // 2
                        - self.actifA[i][j] * self.actifX[j] * (self.echellex + 1)-2,
                        width=2,
                        fill='black',
                        )
                    increment += self.echelle + 1
                    
                    listelocal.append(rectanglelocal)
                increment += self.echelle + 1
                self.listerectangle.append(listelocal)

            # ligne du 0
            self.canva.create_line(
                0,
                self.largeur // 2,
                self.hauteur + 1 + len(self.actifA),
                self.largeur // 2,
                width=3,
                fill="gold",
            )
            self.canva.create_line(
                0,
                self.largeur // 2 - 2,
                self.hauteur + 1 + len(self.actifA),
                self.largeur // 2 - 2,
                width=1,
                fill="black",
            )
            self.canva.create_line(
                0,
                self.largeur // 2 + 2,
                self.hauteur + 1 + len(self.actifA),
                self.largeur // 2 + 2,
                width=1,
                fill="black",
            )

            # boule et cercle
            if self.nourriture == 0:
                self.salade = ImageTk.PhotoImage(
                    Image.open("projet tortuga/salade.png").resize(
                        (
                            int(
                                (self.echelle + 1)
                                * (len(self.actifA) * (3 / (4 * len(self.actifA))))
                                + 1
                            ),
                            int((self.echellex + 1) * (len(self.actifA) * 3 / 4) + 1),
                        )
                    )
                )
            elif self.nourriture == 1:
                self.salade = ImageTk.PhotoImage(
                    Image.open("projet tortuga/pizza.png").resize(
                        (
                            int(
                                (self.echelle + 1)
                                * (len(self.actifA) * (3 / (4 * len(self.actifA))))
                                + 1
                            ),
                            int((self.echellex + 1) * (len(self.actifA) * 3 / 4) + 1),
                        )
                    )
                )
            elif self.nourriture == 2:
                self.salade = ImageTk.PhotoImage(
                    Image.open("projet tortuga/bonbon.png").resize(
                        (
                            int(
                                (self.echelle + 1)
                                * (len(self.actifA) * (3 / (4 * len(self.actifA))))
                                + 1
                            ),
                            int((self.echellex + 1) * (len(self.actifA) * 3 / 4) + 1),
                        )
                    )
                )
            elif self.nourriture == 3:
                self.salade = ImageTk.PhotoImage(
                    Image.open("projet tortuga/pasteque.png").resize(
                        (
                            int(
                                (self.echelle + 1)
                                * (len(self.actifA) * (3 / (4 * len(self.actifA))))
                                + 1
                            ),
                            int((self.echellex + 1) * (len(self.actifA) * 3 / 4) + 1),
                        )
                    )
                )
            elif self.nourriture == 4:
                self.salade = ImageTk.PhotoImage(
                    Image.open("projet tortuga/viande.png").resize(
                        (
                            int(
                                (self.echelle + 1)
                                * (len(self.actifA) * (3 / (4 * len(self.actifA))))
                                + 1
                            ),
                            int((self.echellex + 1) * (len(self.actifA) * 3 / 4) + 1),
                        )
                    )
                )
            elif self.nourriture == 5:
                self.salade = ImageTk.PhotoImage(
                    Image.open("projet tortuga/sushi.png").resize(
                        (
                            int(
                                (self.echelle + 1)
                                * (len(self.actifA) * (3 / (4 * len(self.actifA))))
                                + 1
                            ),
                            int((self.echellex + 1) * (len(self.actifA) * 3 / 4) + 1),
                        )
                    )
                )
            elif self.nourriture == 6:
                self.salade = ImageTk.PhotoImage(
                    Image.open("projet tortuga/glace.png").resize(
                        (
                            int(
                                (self.echelle + 1)
                                * (len(self.actifA) * (3 / (4 * len(self.actifA))))
                                + 1
                            ),
                            int((self.echellex + 1) * (len(self.actifA) * 3 / 4) + 1),
                        )
                    )
                )

            for k in range(len(self.actifB)):
                imagelocal = self.canva.create_image(
                    (self.echelle + 1)
                    * ((len(self.actifA)) * (k + 1 + 1 / (8 * len(self.actifA))))
                    + (self.echelle + 1) * k,
                    self.largeur // 2
                    - (self.echellex + 1) * (len(self.actifA) * 3 / 8 + self.actifB[k]),
                    anchor=tk.NW,
                    image=self.salade,
                )
                flechelocal = self.canva.create_line(
                    (self.echelle + 1)
                    * (len(self.actifA) * (k + 1 + 1 / (2 * len(self.actifA))))
                    + (self.echelle + 1) * k,
                    self.largeur // 2,
                    (self.echelle + 1)
                    * (len(self.actifA) * (k + 1 + 1 / (2 * len(self.actifA))))
                    + (self.echelle + 1) * k,
                    self.largeur // 2,
                    width=self.hauteur_fenetre / 100,
                    arrow="last",
                    fill="red",
                )
                if self.canva.coords(imagelocal)[1] > self.largeur:
                    self.canva.coords(
                        flechelocal,
                        (self.echelle + 1)
                        * (len(self.actifA) * (k + 1 + 1 / (2 * len(self.actifA))))
                        + (self.echelle + 1) * k,
                        self.largeur - self.hauteur_fenetre / 10,
                        (self.echelle + 1)
                        * (len(self.actifA) * (k + 1 + 1 / (2 * len(self.actifA))))
                        + (self.echelle + 1) * k,
                        self.largeur - 4 * self.hauteur_fenetre / 100,
                    )
                elif self.canva.coords(imagelocal)[1] < 0:
                    self.canva.coords(
                        flechelocal,
                        (self.echelle + 1)
                        * (len(self.actifA) * (k + 1 + 1 / (2 * len(self.actifA))))
                        + (self.echelle + 1) * k,
                        self.hauteur_fenetre / 10,
                        (self.echelle + 1)
                        * (len(self.actifA) * (k + 1 + 1 / (2 * len(self.actifA))))
                        + (self.echelle + 1) * k,
                        4 * self.hauteur_fenetre / 100,
                    )
                self.listeboule.append([imagelocal])
                self.listefleche.append(flechelocal)
            if self.emojie == 0:
                self.mimtortue = ImageTk.PhotoImage(
                    Image.open("projet tortuga/tortumim.jpg").resize(
                        (
                            int(
                                (self.echelle + 1)
                                * (len(self.actifA) * (3 / (4 * len(self.actifA))))
                                + 1
                            ),
                            int((self.echellex + 1) * (len(self.actifA) * 3 / 4) + 1),
                        )
                    )
                )
            elif self.emojie == 1:
                self.mimtortue = ImageTk.PhotoImage(
                    Image.open("projet tortuga/escargot.png").resize(
                        (
                            int(
                                (self.echelle + 1)
                                * (len(self.actifA) * (3 / (4 * len(self.actifA))))
                                + 1
                            ),
                            int((self.echellex + 1) * (len(self.actifA) * 3 / 4) + 1),
                        )
                    )
                )
            elif self.emojie == 2:
                self.mimtortue = ImageTk.PhotoImage(
                    Image.open("projet tortuga/t-rex.png").resize(
                        (
                            int(
                                (self.echelle + 1)
                                * (len(self.actifA) * (3 / (4 * len(self.actifA))))
                                + 1
                            ),
                            int((self.echellex + 1) * (len(self.actifA) * 3 / 4) + 1),
                        )
                    )
                )
            elif self.emojie == 3:
                self.mimtortue = ImageTk.PhotoImage(
                    Image.open("projet tortuga/crabe.png").resize(
                        (
                            int(
                                (self.echelle + 1)
                                * (len(self.actifA) * (3 / (4 * len(self.actifA))))
                                + 1
                            ),
                            int((self.echellex + 1) * (len(self.actifA) * 3 / 4) + 1),
                        )
                    )
                )
            elif self.emojie == 4:
                self.mimtortue = ImageTk.PhotoImage(
                    Image.open("projet tortuga/chevre.png").resize(
                        (
                            int(
                                (self.echelle + 1)
                                * (len(self.actifA) * (3 / (4 * len(self.actifA))))
                                + 1
                            ),
                            int((self.echellex + 1) * (len(self.actifA) * 3 / 4) + 1),
                        )
                    )
                )
            elif self.emojie == 5:
                self.mimtortue = ImageTk.PhotoImage(
                    Image.open("projet tortuga/poussin.png").resize(
                        (
                            int(
                                (self.echelle + 1)
                                * (len(self.actifA) * (3 / (4 * len(self.actifA))))
                                + 1
                            ),
                            int((self.echellex + 1) * (len(self.actifA) * 3 / 4) + 1),
                        )
                    )
                )
            elif self.emojie == 6:
                self.mimtortue = ImageTk.PhotoImage(
                    Image.open("projet tortuga/fourmi.png").resize(
                        (
                            int(
                                (self.echelle + 1)
                                * (len(self.actifA) * (3 / (4 * len(self.actifA))))
                                + 1
                            ),
                            int((self.echellex + 1) * (len(self.actifA) * 3 / 4) + 1),
                        )
                    )
                )

            for k in range(len(self.actifA)):
                imagelocal = self.canva.create_image(
                    (self.echelle + 1)
                    * (len(self.actifA) * (k + 1 + 1 / (8 * len(self.actifA))))
                    + (self.echelle + 1) * k,
                    self.largeur // 2
                    - (self.echellex + 1)
                    * (len(self.actifA) * 3 / 8 + self.actifA.dot(self.actifX)[k]),
                    anchor=tk.NW,
                    image=self.mimtortue,
                )
                self.listeboule[k].append(imagelocal)
            self.a = 0

    def preparecanva2(self):
        self.gifcheck2 = [False for k in self.actifA]
        self.codegif2 = [0 for k in self.actifA]
        self.stop2 = True
        self.listerectangle2 = []
        self.listeboule2 = []
        self.frames02 = [0 for i in range(len(self.actifA2))]
        self.frames12 = [[], [], [], [], [], [], []]
        self.listefleche2 = []
        self.canva2.delete("all")
        if self.variable.get() == "x":
            if self.pouvoirunlock:
                self.canva2.config(
                    width=self.largeur + 2 * self.hauteur_fenetre / 10,
                    height=self.hauteur + self.hauteur_fenetre / 10,
                )
            else:
                self.canva2.config(
                    height=self.hauteur,
                    width=self.largeur,
                )

            increment = 0
            # ligne du quadrillage
            for k in range(len(self.actifA2) + 1):
                self.canva2.create_line(
                    0,
                    (self.echelle + 1) * k,
                    self.largeur + 1,
                    (self.echelle + 1) * k,
                    width=1,
                    fill="grey73",
                )
            self.canva2.create_rectangle(
                0,
                (self.echelle + 1) * k,
                self.largeur,
                (self.echelle + 1) * k + self.echelle + 1,
                width=1,
                fill="grey89",
                outline="red",
            )
            for i in range(len(self.actifA2)):
                self.canva2.create_line(
                    0,
                    (self.echelle + 1) * (len(self.actifA2) + 1) + increment,
                    self.largeur + 1,
                    (self.echelle + 1) * (len(self.actifA2) + 1) + increment,
                    width=1,
                    fill="black",
                )

                increment += self.echelle + 1
                for k in range(len(self.actifA2)):
                    self.canva2.create_line(
                        0,
                        (self.echelle + 1) * (len(self.actifA2) + 1) + increment,
                        self.largeur,
                        (self.echelle + 1) * (len(self.actifA2) + 1) + increment,
                        width=1,
                        fill="grey73",
                    )
                    increment += self.echelle + 1
                self.canva2.create_rectangle(
                    0,
                    (self.echelle + 1) * (len(self.actifA2) + 1)
                    + increment
                    - self.echelle
                    - 1,
                    self.largeur,
                    (self.echelle + 1) * (len(self.actifA2) + 1) + increment,
                    width=1,
                    fill="grey89",
                    outline="red",
                )
            increment = 0
            # rectangle
            for i in range(len(self.actifA2)):
                listelocal = []
                for j in range(len(self.actifA2)):
                    rectanglelocal = self.canva2.create_rectangle(
                        self.largeur // 2,
                        increment,
                        self.largeur // 2
                        + self.actifA2[i][j] * self.actifX[j] * (self.echellex + 1),
                        increment + self.echelle + 1,
                        width=1,
                        fill=self.couleurs[j],
                    )
                    increment += self.echelle + 1
                    listelocal.append(rectanglelocal)
                increment += self.echelle + 1
                self.listerectangle2.append(listelocal)

            # ligne du 0
            self.canva2.create_line(
                self.largeur // 2,
                0,
                self.largeur // 2,
                self.hauteur + 1 + len(self.actifA2),
                width=3,
                fill="gold",
            )
            self.canva2.create_line(
                self.largeur // 2 - 2,
                0,
                self.largeur // 2 - 2,
                self.hauteur + 1 + len(self.actifA2),
                width=1,
                fill="black",
            )
            self.canva2.create_line(
                self.largeur // 2 + 2,
                0,
                self.largeur // 2 + 2,
                self.hauteur + 1 + len(self.actifA2),
                width=1,
                fill="black",
            )

            # boule et cercle
            for k in range(len(self.actifB2)):
                imagelocal = self.canva2.create_image(
                    self.largeur // 2
                    + (self.echellex + 1)
                    * (-len(self.actifA2) * 3 / 8 + self.actifB2[k]),
                    (self.echelle + 1)
                    * ((len(self.actifA2)) * (k + 1 + 1 / (8 * len(self.actifA2))))
                    + (self.echelle + 1) * k,
                    anchor=tk.NW,
                    image=self.salade,
                )
                flechelocal = self.canva2.create_line(
                    self.largeur // 2,
                    (self.echelle + 1)
                    * (len(self.actifA2) * (k + 1 + 1 / (2 * len(self.actifA2))))
                    + (self.echelle + 1) * k,
                    self.largeur // 2,
                    (self.echelle + 1)
                    * (len(self.actifA2) * (k + 1 + 1 / (2 * len(self.actifA2))))
                    + (self.echelle + 1) * k,
                    width=10,
                    arrow="last",
                    fill="red",
                )
                if self.canva2.coords(imagelocal)[0] > self.largeur:
                    self.canva2.coords(
                        flechelocal,
                        self.largeur - self.hauteur_fenetre / 10,
                        (self.echelle + 1)
                        * (len(self.actifA2) * (k + 1 + 1 / (2 * len(self.actifA2))))
                        + (self.echelle + 1) * k,
                        self.largeur - 4 * self.hauteur_fenetre / 100,
                        (self.echelle + 1)
                        * (len(self.actifA2) * (k + 1 + 1 / (2 * len(self.actifA2))))
                        + (self.echelle + 1) * k,
                    )
                elif self.canva2.coords(imagelocal)[0] < 0:
                    self.canva2.coords(
                        flechelocal,
                        self.hauteur_fenetre / 10,
                        (self.echelle + 1)
                        * (len(self.actifA2) * (k + 1 + 1 / (2 * len(self.actifA2))))
                        + (self.echelle + 1) * k,
                        4 * self.hauteur_fenetre / 100,
                        (self.echelle + 1)
                        * (len(self.actifA2) * (k + 1 + 1 / (2 * len(self.actifA2))))
                        + (self.echelle + 1) * k,
                    )
                self.listeboule2.append([imagelocal])
                self.listefleche2.append(flechelocal)
                jauge = 0.2

            for k in range(len(self.actifA2)):
                imagelocal = self.canva2.create_image(
                    self.largeur // 2
                    + (self.echellex + 1)
                    * (-len(self.actifA2) * 3 / 8 + self.actifA2.dot(self.actifX)[k]),
                    (self.echelle + 1)
                    * (len(self.actifA2) * (k + 1 + 1 / (8 * len(self.actifA2))))
                    + (self.echelle + 1) * k,
                    anchor=tk.NW,
                    image=self.mimtortue,
                )
                self.listeboule2[k].append(imagelocal)
            self.a = 0

        else:
            if self.pouvoirunlock:
                self.canva2.config(
                    height=self.largeur + 2 * self.hauteur_fenetre / 10,
                    width=self.hauteur + 2 * self.hauteur_fenetre / 10,
                )
            else:
                self.canva2.config(
                    height=self.largeur,
                    width=self.hauteur,
                )
            increment = 0
            # ligne du quadrillage
            for k in range(len(self.actifA2) + 1):
                self.canva2.create_line(
                    (self.echelle + 1) * k,
                    0,
                    (self.echelle + 1) * k,
                    self.largeur + 1,
                    width=1,
                    fill="grey73",
                )
            self.canva2.create_rectangle(
                (self.echelle + 1) * k,
                0,
                (self.echelle + 1) * k + self.echelle + 1,
                self.largeur,
                width=1,
                fill="grey89",
                outline="red",
            )
            for i in range(len(self.actifA2) - 1):
                self.canva2.create_line(
                    (self.echelle + 1) * (len(self.actifA2) + 1) + increment,
                    0,
                    (self.echelle + 1) * (len(self.actifA2) + 1) + increment,
                    self.largeur + 1,
                    width=1,
                    fill="black",
                )

                increment += self.echelle + 1
                for k in range(len(self.actifA2)):
                    self.canva2.create_line(
                        (self.echelle + 1) * (len(self.actifA2) + 1) + increment,
                        0,
                        (self.echelle + 1) * (len(self.actifA2) + 1) + increment,
                        self.largeur,
                        width=1,
                        fill="grey73",
                    )
                    increment += self.echelle + 1
                self.canva2.create_rectangle(
                    (self.echelle + 1) * (len(self.actifA2) + 1)
                    + increment
                    - self.echelle
                    - 1,
                    0,
                    (self.echelle + 1) * (len(self.actifA2) + 1) + increment,
                    self.largeur,
                    width=1,
                    fill="grey89",
                    outline="red",
                )

            increment = 0
            # rectangle
            for i in range(len(self.actifA2)):
                listelocal = []
                for j in range(len(self.actifA2)):
                    rectanglelocal = self.canva2.create_rectangle(
                        increment,
                        self.largeur // 2,
                        increment + self.echelle + 1,
                        self.largeur // 2
                        - self.actifA2[i][j] * self.actifX[j] * (self.echellex + 1),
                        width=1,
                        fill=self.couleurs[j],
                    )
                    increment += self.echelle + 1
                    listelocal.append(rectanglelocal)
                increment += self.echelle + 1
                self.listerectangle2.append(listelocal)

            # ligne du 0
            self.canva2.create_line(
                0,
                self.largeur // 2,
                self.hauteur + 1 + len(self.actifA2),
                self.largeur // 2,
                width=3,
                fill="gold",
            )
            self.canva2.create_line(
                0,
                self.largeur // 2 - 2,
                self.hauteur + 1 + len(self.actifA2),
                self.largeur // 2 - 2,
                width=1,
                fill="black",
            )
            self.canva2.create_line(
                0,
                self.largeur // 2 + 2,
                self.hauteur + 1 + len(self.actifA2),
                self.largeur // 2 + 2,
                width=1,
                fill="black",
            )

            # boule et cercle

            for k in range(len(self.actifB2)):
                imagelocal = self.canva2.create_image(
                    (self.echelle + 1)
                    * ((len(self.actifA2)) * (k + 1 + 1 / (8 * len(self.actifA2))))
                    + (self.echelle + 1) * k,
                    self.largeur // 2
                    - (self.echellex + 1)
                    * (len(self.actifA2) * 3 / 8 + self.actifB2[k]),
                    anchor=tk.NW,
                    image=self.salade,
                )
                flechelocal = self.canva2.create_line(
                    (self.echelle + 1)
                    * (len(self.actifA2) * (k + 1 + 1 / (2 * len(self.actifA2))))
                    + (self.echelle + 1) * k,
                    self.largeur // 2,
                    (self.echelle + 1)
                    * (len(self.actifA2) * (k + 1 + 1 / (2 * len(self.actifA2))))
                    + (self.echelle + 1) * k,
                    self.largeur // 2,
                    width=self.hauteur_fenetre / 100,
                    arrow="last",
                    fill="red",
                )
                if self.canva2.coords(imagelocal)[1] > self.largeur:
                    self.canva2.coords(
                        flechelocal,
                        (self.echelle + 1)
                        * (len(self.actifA2) * (k + 1 + 1 / (2 * len(self.actifA2))))
                        + (self.echelle + 1) * k,
                        self.largeur - self.hauteur_fenetre / 10,
                        (self.echelle + 1)
                        * (len(self.actifA2) * (k + 1 + 1 / (2 * len(self.actifA2))))
                        + (self.echelle + 1) * k,
                        self.largeur - 4 * self.hauteur_fenetre / 100,
                    )
                elif self.canva2.coords(imagelocal)[1] < 0:
                    self.canva2.coords(
                        flechelocal,
                        (self.echelle + 1)
                        * (len(self.actifA2) * (k + 1 + 1 / (2 * len(self.actifA2))))
                        + (self.echelle + 1) * k,
                        self.hauteur_fenetre / 10,
                        (self.echelle + 1)
                        * (len(self.actifA2) * (k + 1 + 1 / (2 * len(self.actifA2))))
                        + (self.echelle + 1) * k,
                        4 * self.hauteur_fenetre / 100,
                    )
                self.listeboule2.append([imagelocal])
                self.listefleche2.append(flechelocal)
            for k in range(len(self.actifA2)):
                imagelocal = self.canva2.create_image(
                    (self.echelle + 1)
                    * (len(self.actifA2) * (k + 1 + 1 / (8 * len(self.actifA2))))
                    + (self.echelle + 1) * k,
                    self.largeur // 2
                    - (self.echellex + 1)
                    * (len(self.actifA2) * 3 / 8 + self.actifA2.dot(self.actifX)[k]),
                    anchor=tk.NW,
                    image=self.mimtortue,
                )
                self.listeboule2[k].append(imagelocal)

    def assigne(self, bool):
        self.enjeu = bool

    def reinisialisation(self):
        fichier = open("projet tortuga/usopp.txt", "w")

        fichier.write(
            "0000000000000000000000000000000000000000\n0\n01000000\n01000000\n0000"
        )
        fichier.close()
        self.emojie = 0
        self.comptediamant = 0
        self.actifemoji = 0
        self.actifnourriture = 0
        self.skindebloque = "1000000\n"
        self.nourrituredebloque = "1000000\n"
        self.diamant.itemconfig(self.nombrediamant, text=str(self.comptediamant))
        for i in range(5):
            for j in range(8):
                self.niveaucanva.itemconfig(
                    self.listeniveau[i * 8 + j][0], fill="light grey"
                )
                self.niveaucanva.itemconfig(
                    self.listeniveau[i * 8 + j][2], image=self.trans
                )
                self.niveaucanva.itemconfig(
                    self.listeniveau[i * 8 + j][3], image=self.trans
                )
                self.niveaucanva.itemconfig(
                    self.listeniveau[i * 8 + j][4], image=self.trans
                )
                self.niveauvalidé[i * 8 + j] = False

        self.actifniveau = 0

        self.systeme.set("niveau 0" + str(self.actifniveau + 1))
        self.changesysteme(0)
        self.niveaucanva.itemconfig(self.listeniveau[0][0], fill="lightskyblue2")

    def prepareskin(self):
        self.valideskin = tk.Button(
            self.selectskin,
            text="valider",
            font="Helvetica " + str(int(2 * self.hauteur_fenetre / 100)) + " bold",
            bg="turquoise3",
            activebackground="turquoise2",
            command=self.skinvalide,
        )
        self.droiteskin = tk.Button(
            self.selectskin,
            text="->",
            font="Helvetica " + str(int(4 * self.hauteur_fenetre / 100)) + " bold",
            bg="turquoise3",
            activebackground="turquoise2",
            command=lambda: self.skinsuivant(1),
        )
        self.droitedebloque = tk.Button(
            self.selectskin,
            text="débloquer (10 diamants)",
            font="Helvetica " + str(int(2 * self.hauteur_fenetre / 100)) + " bold",
            bg="turquoise3",
            activebackground="turquoise2",
            command=lambda: self.débloquer(-1),
        )
        self.gauchedebloque = tk.Button(
            self.selectskin,
            text="débloquer (10 diamants)",
            font="Helvetica " + str(int(2 * self.hauteur_fenetre / 100)) + " bold",
            bg="turquoise3",
            activebackground="turquoise2",
            command=self.débloquer,
        )
        self.gaucheskin = tk.Button(
            self.selectskin,
            text="<-",
            font="Helvetica " + str(int(4 * self.hauteur_fenetre / 100)) + " bold",
            bg="turquoise3",
            activebackground="turquoise2",
            command=lambda: self.skinsuivant(-1),
        )
        self.valideskin.place(
            anchor="center",
            x=self.hauteur_fenetre * 4 / 5,
            y=self.hauteur_fenetre * 7 / 10,
        )
        self.droiteskin.place(
            anchor="center",
            x=self.hauteur_fenetre * 14 / 20,
            y=self.hauteur_fenetre * 4 / 10,
        )
        self.gaucheskin.place(
            anchor="center",
            x=self.hauteur_fenetre * 1 / 5,
            y=self.hauteur_fenetre * 4 / 10,
        )

        self.actifemoji = self.emojie
        self.listeskin = [
            ImageTk.PhotoImage(
                Image.open("projet tortuga/tortumim.jpg").resize(
                    (
                        int(36 * self.hauteur_fenetre / 100),
                        int(36 * self.hauteur_fenetre / 100),
                    )
                )
            ),
            ImageTk.PhotoImage(
                Image.open("projet tortuga/escargot.png").resize(
                    (
                        int(36 * self.hauteur_fenetre / 100),
                        int(36 * self.hauteur_fenetre / 100),
                    )
                )
            ),
            ImageTk.PhotoImage(
                Image.open("projet tortuga/t-rex.png").resize(
                    (
                        int(36 * self.hauteur_fenetre / 100),
                        int(36 * self.hauteur_fenetre / 100),
                    )
                )
            ),
            ImageTk.PhotoImage(
                Image.open("projet tortuga/crabe.png").resize(
                    (
                        int(36 * self.hauteur_fenetre / 100),
                        int(36 * self.hauteur_fenetre / 100),
                    )
                )
            ),
            ImageTk.PhotoImage(
                Image.open("projet tortuga/chevre.png").resize(
                    (
                        int(36 * self.hauteur_fenetre / 100),
                        int(36 * self.hauteur_fenetre / 100),
                    )
                )
            ),
            ImageTk.PhotoImage(
                Image.open("projet tortuga/poussin.png").resize(
                    (
                        int(36 * self.hauteur_fenetre / 100),
                        int(36 * self.hauteur_fenetre / 100),
                    )
                )
            ),
            ImageTk.PhotoImage(
                Image.open("projet tortuga/fourmi.png").resize(
                    (
                        int(36 * self.hauteur_fenetre / 100),
                        int(36 * self.hauteur_fenetre / 100),
                    )
                )
            ),
        ]
        self.actifskin = tk.Label(
            self.selectskin,
            image=self.listeskin[self.actifemoji],
            background="papaya whip",
        )
        self.actifskin.place(
            anchor="center",
            x=self.hauteur_fenetre * 9 / 20,
            y=self.hauteur_fenetre * 4 / 10,
        )
        self.actifnourriture = self.nourriture
        self.droitegraille = tk.Button(
            self.selectskin,
            text="->",
            font="Helvetica " + str(int(4 * self.hauteur_fenetre / 100)) + " bold",
            bg="turquoise3",
            activebackground="turquoise2",
            command=lambda: self.graillesuivant(1),
        )
        self.gauchegraille = tk.Button(
            self.selectskin,
            text="<-",
            font="Helvetica " + str(int(4 * self.hauteur_fenetre / 100)) + " bold",
            bg="turquoise3",
            activebackground="turquoise2",
            command=lambda: self.graillesuivant(-1),
        )
        self.gauchegraille.place(
            anchor="center",
            x=self.hauteur_fenetre * 18 / 20,
            y=self.hauteur_fenetre * 4 / 10,
        )
        self.droitegraille.place(
            anchor="center",
            x=self.hauteur_fenetre * 7 / 5,
            y=self.hauteur_fenetre * 4 / 10,
        )
        self.listegraille = [
            ImageTk.PhotoImage(
                Image.open("projet tortuga/salade.png").resize(
                    (
                        int(36 * self.hauteur_fenetre / 100),
                        int(36 * self.hauteur_fenetre / 100),
                    )
                )
            ),
            ImageTk.PhotoImage(
                Image.open("projet tortuga/pizza.png").resize(
                    (
                        int(36 * self.hauteur_fenetre / 100),
                        int(36 * self.hauteur_fenetre / 100),
                    )
                )
            ),
            ImageTk.PhotoImage(
                Image.open("projet tortuga/bonbon.png").resize(
                    (
                        int(36 * self.hauteur_fenetre / 100),
                        int(36 * self.hauteur_fenetre / 100),
                    )
                )
            ),
            ImageTk.PhotoImage(
                Image.open("projet tortuga/pasteque.png").resize(
                    (
                        int(36 * self.hauteur_fenetre / 100),
                        int(36 * self.hauteur_fenetre / 100),
                    )
                )
            ),
            ImageTk.PhotoImage(
                Image.open("projet tortuga/viande.png").resize(
                    (
                        int(36 * self.hauteur_fenetre / 100),
                        int(36 * self.hauteur_fenetre / 100),
                    )
                )
            ),
            ImageTk.PhotoImage(
                Image.open("projet tortuga/sushi.png").resize(
                    (
                        int(36 * self.hauteur_fenetre / 100),
                        int(36 * self.hauteur_fenetre / 100),
                    )
                )
            ),
            ImageTk.PhotoImage(
                Image.open("projet tortuga/glace.png").resize(
                    (
                        int(36 * self.hauteur_fenetre / 100),
                        int(36 * self.hauteur_fenetre / 100),
                    )
                )
            ),
        ]
        self.actifgraille = tk.Label(
            self.selectskin,
            image=self.listegraille[self.actifnourriture],
            background="papaya whip",
        )
        self.actifgraille.place(
            anchor="center",
            x=self.hauteur_fenetre * 23 / 20,
            y=self.hauteur_fenetre * 4 / 10,
        )
        if self.nourrituredebloque[self.actifnourriture] == "0":
            self.droitedebloque.place(
                anchor="center",
                x=self.hauteur_fenetre * 23 / 20,
                y=self.hauteur_fenetre * 6 / 10,
            )
        if self.skindebloque[self.actifemoji] == "0":
            self.gauchedebloque.place(
                anchor="center",
                x=self.hauteur_fenetre * 9 / 20,
                y=self.hauteur_fenetre * 6 / 10,
            )

    def débloquer(self, source=1):
        if self.comptediamant >= 10:
            self.comptediamant -= 10
            self.diamant.itemconfig(self.nombrediamant, text=str(self.comptediamant))
            if source == 1:
                self.skindebloque = (
                    self.skindebloque[: self.actifemoji]
                    + "1"
                    + self.skindebloque[self.actifemoji + 1 :]
                )
                self.gauchedebloque.place_forget()
                if self.nourrituredebloque[self.actifnourriture] == "1":
                    self.valideskin.config(
                        bg="turquoise3", activebackground="turquoise2"
                    )
            else:
                self.nourrituredebloque = (
                    self.nourrituredebloque[: self.actifnourriture]
                    + "1"
                    + self.nourrituredebloque[self.actifnourriture + 1 :]
                )

                self.droitedebloque.place_forget()
                if self.skindebloque[self.actifemoji] == "1":
                    self.valideskin.config(
                        bg="turquoise3", activebackground="turquoise2"
                    )
            fichier = open("projet tortuga/usopp.txt", "r")
            info = fichier.readlines()[0]
            fichier.close()
            fichier = open("projet tortuga/usopp.txt", "w")
            fichier.write(
                info
                + str(self.pouvoirunlock)
                + "\n"
                + str(self.emojie)
                + self.skindebloque
                + str(self.nourriture)
                + self.nourrituredebloque
                + self.anciennecombine
            )
            fichier.close()
            if self.comptediamant < 10:
                self.droitedebloque.config(
                    bg="firebrick3",
                    activebackground="firebrick2",
                    text="diamants insuffisants",
                )
                self.gauchedebloque.config(
                    bg="firebrick3",
                    activebackground="firebrick2",
                    text="diamants insuffisants",
                )

    def skinsuivant(self, increment):
        self.actifemoji = (self.actifemoji + increment) % len(self.listeskin)
        if self.skindebloque[self.actifemoji] == "0":
            self.gauchedebloque.place(
                anchor="center",
                x=self.hauteur_fenetre * 9 / 20,
                y=self.hauteur_fenetre * 6 / 10,
            )
            self.valideskin.config(bg="firebrick3", activebackground="firebrick2")
        else:
            if self.nourrituredebloque[self.actifnourriture] == "1":
                self.valideskin.config(bg="turquoise3", activebackground="turquoise2")
            self.gauchedebloque.place_forget()
        self.actifskin.config(image=self.listeskin[self.actifemoji])

    def graillesuivant(self, increment):
        self.actifnourriture = (self.actifnourriture + increment) % len(
            self.listegraille
        )
        if self.nourrituredebloque[self.actifnourriture] == "0":
            self.droitedebloque.place(
                anchor="center",
                x=self.hauteur_fenetre * 23 / 20,
                y=self.hauteur_fenetre * 6 / 10,
            )
            self.valideskin.config(bg="firebrick3", activebackground="firebrick2")
        else:
            if self.skindebloque[self.actifemoji] == "1":
                self.valideskin.config(bg="turquoise3", activebackground="turquoise2")
            self.droitedebloque.place_forget()
        self.actifgraille.config(image=self.listegraille[self.actifnourriture])

    def skinvalide(self):
        if (
            self.skindebloque[self.actifemoji] == "1"
            and self.nourrituredebloque[self.actifnourriture] == "1"
        ):
            self.emojie = self.actifemoji
            self.nourriture = self.actifnourriture

            fichier = open("projet tortuga/usopp.txt", "r")
            info = fichier.readlines()[0]
            fichier.close()
            fichier = open("projet tortuga/usopp.txt", "w")
            fichier.write(
                info
                + str(self.pouvoirunlock)
                + "\n"
                + str(self.emojie)
                + self.skindebloque
                + str(self.nourriture)
                + self.nourrituredebloque
                + self.anciennecombine
            )
            fichier.close()

    def preparebouton(self):
        self.listebouton = []
        self.nonsolution = None
        self.listebouton2 = []
        self.listebouton3 = []
        self.bouton.delete("all")
        increment = 0
        if self.actifniveau == 5:
            self.lvl5timer1 = time.time()
        self.listejauge = []
        for i in range(len(self.actifA)):
            rectangle1 = self.bouton.create_rectangle(
                self.hauteur_fenetre / 20 + increment,
                3 * self.hauteur_fenetre / 100,
                self.hauteur_fenetre / 10 + increment,
                7 * self.hauteur_fenetre / 100,
                width=1,
                fill=self.couleurs[i],
            )
            rectangle2 = self.bouton.create_rectangle(
                self.hauteur_fenetre / 10 + increment,
                3 * self.hauteur_fenetre / 100,
                3 * self.hauteur_fenetre / 20 + increment,
                7 * self.hauteur_fenetre / 100,
                width=1,
                fill=self.couleurs[i],
            )
            plus1 = self.bouton.create_line(
                5 * self.hauteur_fenetre / 40 + increment,
                7 * self.hauteur_fenetre / 200,
                5 * self.hauteur_fenetre / 40 + increment,
                13 * self.hauteur_fenetre / 200,
                width=3,
                fill="white",
            )
            moins1 = self.bouton.create_line(
                3 * self.hauteur_fenetre / 50 + increment,
                self.hauteur_fenetre / 20,
                9 * self.hauteur_fenetre / 100 + increment,
                self.hauteur_fenetre / 20,
                width=3,
                fill="white",
            )
            plus2 = self.bouton.create_line(
                11 * self.hauteur_fenetre / 100 + increment,
                self.hauteur_fenetre / 20,
                14 * self.hauteur_fenetre / 100 + increment,
                self.hauteur_fenetre / 20,
                width=3,
                fill="white",
            )
            jauge1 = self.bouton.create_rectangle(
                5 * self.hauteur_fenetre / 100 + increment,
                2 * self.hauteur_fenetre / 20 - 2 * self.hauteur_fenetre / 100,
                self.hauteur_fenetre / 5 - 5 * self.hauteur_fenetre / 100 + increment,
                2 * self.hauteur_fenetre / 20 - self.hauteur_fenetre / 200,
                width=2,
                fill="white",
            )
            jauge2 = self.bouton.create_rectangle(
                self.hauteur_fenetre / 10 + increment,
                2 * self.hauteur_fenetre / 20 - 2 * self.hauteur_fenetre / 100,
                self.hauteur_fenetre / 10 + 2 * self.hauteur_fenetre / 100 + increment,
                2 * self.hauteur_fenetre / 20 - self.hauteur_fenetre / 200,
                width=2,
                fill=self.couleurs[i],
            )
            self.listejauge.append(jauge2)
            increment += self.hauteur_fenetre / 5
            self.listebouton.append((rectangle1, rectangle2, plus1, plus2, moins1))
        increment = 0
        self.boutonretour = self.bouton.create_rectangle(
            4 * self.hauteur_fenetre / 5,
            3 * self.hauteur_fenetre / 100,
            3 * self.hauteur_fenetre / 40 + 4 * self.hauteur_fenetre / 5,
            7 * self.hauteur_fenetre / 100,
            width=2,
            fill="white",
        )
        self.bouton.create_line(
            2 * self.hauteur_fenetre / 100 + 4 * self.hauteur_fenetre / 5,
            5 * self.hauteur_fenetre / 100,
            6 * self.hauteur_fenetre / 100 + 4 * self.hauteur_fenetre / 5,
            5 * self.hauteur_fenetre / 100,
            arrow="first",
            arrowshape=(8, 8, 8),
            width=8,
            fill="black",
        )
        texte = ""
        for i in self.listetext2[self.actifniveau]:
            texte += i + "\n"

        self.comment = self.bouton.create_text(
            self.hauteur_fenetre / 2,
            11 * self.hauteur_fenetre / 100,
            anchor="n",
            font="Helvetica " + str(int(4 * self.hauteur_fenetre / 200)) + " bold",
            text=texte,
            fill="black",
        )
        ##########x###########

        if self.variable.get() == "x":
            self.canva.create_rectangle(
                self.largeur,
                0,
                self.largeur + self.hauteur_fenetre / 2,
                self.hauteur + 1 + len(self.actifA),
                width=1,
                fill="white",
            )

            # pivot
            self.canva.create_rectangle(
                0,
                self.hauteur + 1 + len(self.actifA),
                self.largeur + self.hauteur_fenetre / 2,
                self.hauteur + 1 + self.hauteur_fenetre / 10,
                width=1,
                fill="white",
            )
            pivotoval1 = self.canva.create_oval(
                self.hauteur_fenetre / 25,
                7 * self.hauteur_fenetre / 200 + self.hauteur,
                7 * self.hauteur_fenetre / 100,
                13 * self.hauteur_fenetre / 200 + self.hauteur,
                width=1,
                fill="grey73",
            )
            pivotoval2 = self.canva.create_oval(
                14 * self.hauteur_fenetre / 100,
                7 * self.hauteur_fenetre / 200 + self.hauteur,
                17 * self.hauteur_fenetre / 100,
                13 * self.hauteur_fenetre / 200 + self.hauteur,
                width=1,
                fill="grey73",
            )

            pivotplus1 = self.canva.create_line(
                9 * self.hauteur_fenetre / 100,
                self.hauteur_fenetre / 20 + self.hauteur,
                3 * self.hauteur_fenetre / 25,
                self.hauteur_fenetre / 20 + self.hauteur,
                width=4,
                fill="black",
            )
            pivotplus2 = self.canva.create_line(
                21 * self.hauteur_fenetre / 200,
                7 * self.hauteur_fenetre / 200 + self.hauteur,
                21 * self.hauteur_fenetre / 200,
                13 * self.hauteur_fenetre / 200 + self.hauteur,
                width=4,
                fill="black",
            )

            self.gaussrectangle1 = self.canva.create_rectangle(
                22 * self.hauteur_fenetre / 100,
                3 * self.hauteur_fenetre / 100 + self.hauteur,
                3 * self.hauteur_fenetre / 10,
                7 * self.hauteur_fenetre / 100 + self.hauteur,
                width=1,
                fill="grey42",
            )

            gausstext1 = self.canva.create_text(
                26 * self.hauteur_fenetre / 100,
                5 * self.hauteur_fenetre / 100 + self.hauteur,
                anchor="center",
                font="Helvetica " + str(int(3 * self.hauteur_fenetre / 200)) + " bold",
                text="pouvoir\ntortue",
                fill="white",
            )

            pivotoval1 = self.canva.create_oval(
                54 * self.hauteur_fenetre / 100,
                7 * self.hauteur_fenetre / 200 + self.hauteur,
                57 * self.hauteur_fenetre / 100,
                13 * self.hauteur_fenetre / 200 + self.hauteur,
                width=1,
                fill="grey73",
            )
            pivotoval2 = self.canva.create_oval(
                64 * self.hauteur_fenetre / 100,
                7 * self.hauteur_fenetre / 200 + self.hauteur,
                67 * self.hauteur_fenetre / 100,
                13 * self.hauteur_fenetre / 200 + self.hauteur,
                width=1,
                fill="grey73",
            )

            pivotmoins = self.canva.create_line(
                59 * self.hauteur_fenetre / 100,
                self.hauteur_fenetre / 20 + self.hauteur,
                62 * self.hauteur_fenetre / 100,
                self.hauteur_fenetre / 20 + self.hauteur,
                width=4,
                fill="black",
            )
            self.gaussrectangle2 = self.canva.create_rectangle(
                72 * self.hauteur_fenetre / 100,
                3 * self.hauteur_fenetre / 100 + self.hauteur,
                8 * self.hauteur_fenetre / 10,
                7 * self.hauteur_fenetre / 100 + self.hauteur,
                width=1,
                fill="grey42",
            )
            gausstext2 = self.canva.create_text(
                76 * self.hauteur_fenetre / 100,
                self.hauteur_fenetre / 20 + self.hauteur,
                anchor="center",
                font="Helvetica " + str(int(3 * self.hauteur_fenetre / 200)) + " bold",
                text="pouvoir\ntortue",
                fill="white",
            )
            for i in range(len(self.actifA)):
                ovalegauss = self.canva.create_oval(
                    self.largeur + 6 * self.hauteur_fenetre / 100,
                    -3 * self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 9 * self.hauteur_fenetre / 100,
                    3 * self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    width=1,
                    fill="grey73",
                )

                self.listeovalgauss.append(
                    [
                        self.canva.create_oval(
                            self.largeur + 6 * self.hauteur_fenetre / 100,
                            -3 * self.hauteur_fenetre / 200
                            + (len(self.actifA) + 1) * self.echelle // 2
                            + increment,
                            self.largeur + 9 * self.hauteur_fenetre / 100,
                            3 * self.hauteur_fenetre / 200
                            + (len(self.actifA) + 1) * self.echelle // 2
                            + increment,
                            width=1,
                            fill="red4",
                        ),
                        self.canva.create_text(
                            self.largeur + 3 * self.hauteur_fenetre / 40 + 1,
                            (len(self.actifA) + 1) * self.echelle // 2 + increment,
                            anchor="center",
                            text=chr(97 + i).capitalize(),
                            font="Helvetica "
                            + str(int(2 * self.hauteur_fenetre / 100))
                            + " bold",
                            fill="white",
                        ),
                    ]
                )
                rectangle1 = self.canva.create_rectangle(
                    self.largeur + self.hauteur_fenetre / 10,
                    -7 * self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 13 * self.hauteur_fenetre / 100,
                    -self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    width=1,
                    fill="red4",
                )
                self.listebouton2.append(rectangle1)
                rectangle2 = self.canva.create_rectangle(
                    self.largeur + self.hauteur_fenetre / 10,
                    self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 13 * self.hauteur_fenetre / 100,
                    7 * self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    width=1,
                    fill="red4",
                )
                self.listebouton2.append(rectangle2)
                plus1 = self.canva.create_line(
                    self.largeur + 11 * self.hauteur_fenetre / 100,
                    -5 * self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 12 * self.hauteur_fenetre / 100,
                    -3 * self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    width=2,
                    fill="white",
                )
                plus2 = self.canva.create_line(
                    self.largeur + 11 * self.hauteur_fenetre / 100,
                    -3 * self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 12 * self.hauteur_fenetre / 100,
                    -5 * self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    width=2,
                    fill="white",
                )

                moins1 = self.canva.create_line(
                    self.largeur + 45 * self.hauteur_fenetre / 400,
                    self.hauteur_fenetre / 40
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 47 * self.hauteur_fenetre / 400,
                    3 * self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    width=2,
                    fill="white",
                )
                ovale1 = self.canva.create_oval(
                    self.largeur + 21 * self.hauteur_fenetre / 200,
                    -3 * self.hauteur_fenetre / 100
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 5 * self.hauteur_fenetre / 40,
                    -self.hauteur_fenetre / 100
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    width=2,
                    outline="white",
                )
                ovale2 = self.canva.create_oval(
                    self.largeur + 21 * self.hauteur_fenetre / 200,
                    self.hauteur_fenetre / 100
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 5 * self.hauteur_fenetre / 40,
                    3 * self.hauteur_fenetre / 100
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    width=2,
                    outline="white",
                )
                increment += self.echelle * (len(self.actifA) + 1)
            increment = 0
            for i in range(len(self.actifA)):
                rectangle1 = self.canva.create_rectangle(
                    self.largeur + 14 * self.hauteur_fenetre / 100,
                    -7 * self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 17 * self.hauteur_fenetre / 100,
                    -self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    width=1,
                    fill="red4",
                )
                self.listebouton3.append(rectangle1)
                rectangle2 = self.canva.create_rectangle(
                    self.largeur + 14 * self.hauteur_fenetre / 100,
                    self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 17 * self.hauteur_fenetre / 100,
                    7 * self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    width=1,
                    fill="red4",
                )
                self.listebouton3.append(rectangle2)
                droite = self.canva.create_line(
                    self.largeur + 31 * self.hauteur_fenetre / 200,
                    -self.hauteur_fenetre / 40
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 31 * self.hauteur_fenetre / 200,
                    -3 * self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    width=2,
                    fill="white",
                    arrow="first",
                )

                gauche = self.canva.create_line(
                    self.largeur + 31 * self.hauteur_fenetre / 200,
                    3 * self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 31 * self.hauteur_fenetre / 200,
                    self.hauteur_fenetre / 40
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    width=2,
                    fill="white",
                    arrow="last",
                )
                ovale1 = self.canva.create_oval(
                    self.largeur + 29 * self.hauteur_fenetre / 200,
                    -3 * self.hauteur_fenetre / 100
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 33 * self.hauteur_fenetre / 200,
                    -self.hauteur_fenetre / 100
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    width=2,
                    outline="white",
                )
                ovale2 = self.canva.create_oval(
                    self.largeur + 29 * self.hauteur_fenetre / 200,
                    self.hauteur_fenetre / 100
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 33 * self.hauteur_fenetre / 200,
                    3 * self.hauteur_fenetre / 100
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    width=2,
                    outline="white",
                )
                increment += self.echelle * (len(self.actifA) + 1)

        ##########y###########

        else:
            self.canva.create_rectangle(
                0,
                self.largeur,
                self.hauteur + self.largeur_fenetre / 5,
                self.largeur + self.hauteur_fenetre / 2,
                width=1,
                fill="white",
            )
            # pivot
            self.canva.create_rectangle(
                self.hauteur + 1 + len(self.actifA),
                0,
                self.hauteur + self.hauteur_fenetre / 5,
                self.largeur,
                width=1,
                fill="white",
            )

            pivotoval1 = self.canva.create_oval(
                self.hauteur + 1 + len(self.actifA) + self.hauteur_fenetre / 25,
                7 * self.hauteur_fenetre / 200,
                self.hauteur + 1 + len(self.actifA) + 7 * self.hauteur_fenetre / 100,
                13 * self.hauteur_fenetre / 200,
                width=1,
                fill="grey73",
            )
            pivotoval2 = self.canva.create_oval(
                self.hauteur + 1 + len(self.actifA) + 14 * self.hauteur_fenetre / 100,
                7 * self.hauteur_fenetre / 200,
                self.hauteur + 1 + len(self.actifA) + 17 * self.hauteur_fenetre / 100,
                13 * self.hauteur_fenetre / 200,
                width=1,
                fill="grey73",
            )

            pivotplus1 = self.canva.create_line(
                self.hauteur + 1 + len(self.actifA) + 9 * self.hauteur_fenetre / 100,
                self.hauteur_fenetre / 20,
                self.hauteur + 1 + len(self.actifA) + 12 * self.hauteur_fenetre / 100,
                self.hauteur_fenetre / 20,
                width=4,
                fill="black",
            )
            pivotplus2 = self.canva.create_line(
                self.hauteur + 1 + len(self.actifA) + 21 * self.hauteur_fenetre / 200,
                7 * self.hauteur_fenetre / 200,
                self.hauteur + 1 + len(self.actifA) + 21 * self.hauteur_fenetre / 200,
                13 * self.hauteur_fenetre / 200,
                width=4,
                fill="black",
            )

            self.gaussrectangle1 = self.canva.create_rectangle(
                self.hauteur + 1 + len(self.actifA) + 13 * self.hauteur_fenetre / 200,
                2 * self.hauteur_fenetre / 25,
                self.hauteur + 1 + len(self.actifA) + 29 * self.hauteur_fenetre / 200,
                3 * self.hauteur_fenetre / 25,
                width=1,
                fill="grey42",
            )

            gausstext1 = self.canva.create_text(
                len(self.actifA) + 21 * self.hauteur_fenetre / 200 + 1 + self.hauteur,
                self.hauteur_fenetre / 10,
                anchor="center",
                font="Helvetica " + str(int(3 * self.hauteur_fenetre / 200)) + " bold",
                text="pouvoir\ntortue",
                fill="white",
            )

            pivotoval1 = self.canva.create_oval(
                self.hauteur + 1 + len(self.actifA) + self.hauteur_fenetre / 25,
                47 * self.hauteur_fenetre / 200,
                self.hauteur + 1 + len(self.actifA) + 7 * self.hauteur_fenetre / 100,
                53 * self.hauteur_fenetre / 200,
                width=1,
                fill="grey73",
            )
            pivotoval2 = self.canva.create_oval(
                self.hauteur + 1 + len(self.actifA) + 7 * self.hauteur_fenetre / 50,
                47 * self.hauteur_fenetre / 200,
                self.hauteur + 1 + len(self.actifA) + 17 * self.hauteur_fenetre / 100,
                53 * self.hauteur_fenetre / 200,
                width=1,
                fill="grey73",
            )

            pivotmoins1 = self.canva.create_line(
                self.hauteur + 1 + len(self.actifA) + 9 * self.hauteur_fenetre / 100,
                self.hauteur_fenetre / 4,
                self.hauteur + 1 + len(self.actifA) + 12 * self.hauteur_fenetre / 100,
                self.hauteur_fenetre / 4,
                width=4,
                fill="black",
            )

            self.gaussrectangle2 = self.canva.create_rectangle(
                self.hauteur + 1 + len(self.actifA) + 13 * self.hauteur_fenetre / 200,
                28 * self.hauteur_fenetre / 100,
                self.hauteur + 1 + len(self.actifA) + 29 * self.hauteur_fenetre / 200,
                32 * self.hauteur_fenetre / 100,
                width=1,
                fill="grey42",
            )

            gausstext2 = self.canva.create_text(
                len(self.actifA) + 21 * self.hauteur_fenetre / 200 + 1 + self.hauteur,
                3 * self.hauteur_fenetre / 10,
                anchor="center",
                font="Helvetica " + str(int(3 * self.hauteur_fenetre / 200)) + " bold",
                text="pouvoir\ntortue",
                fill="white",
            )

            for i in range(len(self.actifA)):
                ovalegauss = self.canva.create_oval(
                    (len(self.actifA) + 1) * self.echelle // 2
                    - 3 * self.hauteur_fenetre / 200
                    + increment,
                    self.largeur + 6 * self.hauteur_fenetre / 100,
                    3 * self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 9 * self.hauteur_fenetre / 100,
                    width=1,
                    fill="grey73",
                )

                self.listeovalgauss.append(
                    [
                        self.canva.create_oval(
                            -3 * self.hauteur_fenetre / 200
                            + (len(self.actifA) + 1) * self.echelle // 2
                            + increment,
                            self.largeur + 6 * self.hauteur_fenetre / 100,
                            3 * self.hauteur_fenetre / 200
                            + (len(self.actifA) + 1) * self.echelle // 2
                            + increment,
                            self.largeur + 9 * self.hauteur_fenetre / 100,
                            width=1,
                            fill="red4",
                        ),
                        self.canva.create_text(
                            (len(self.actifA) + 1) * self.echelle // 2 + increment + 1,
                            self.largeur + 3 * self.hauteur_fenetre / 40,
                            anchor="center",
                            text=chr(97 + i).capitalize(),
                            font="Helvetica "
                            + str(int(self.hauteur_fenetre / 50))
                            + " bold",
                            fill="white",
                        ),
                    ]
                )
                rectangle1 = self.canva.create_rectangle(
                    -7 * self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + self.hauteur_fenetre / 10,
                    -self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 13 * self.hauteur_fenetre / 100,
                    width=1,
                    fill="red4",
                )
                self.listebouton2.append(rectangle1)
                rectangle2 = self.canva.create_rectangle(
                    self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + self.hauteur_fenetre / 10,
                    7 * self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 13 * self.hauteur_fenetre / 100,
                    width=1,
                    fill="red4",
                )
                self.listebouton2.append(rectangle2)
                plus1 = self.canva.create_line(
                    -5 * self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 11 * self.hauteur_fenetre / 100,
                    -3 * self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 12 * self.hauteur_fenetre / 100,
                    width=2,
                    fill="white",
                )
                plus2 = self.canva.create_line(
                    -3 * self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 11 * self.hauteur_fenetre / 100,
                    -5 * self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 12 * self.hauteur_fenetre / 100,
                    width=2,
                    fill="white",
                )

                moins1 = self.canva.create_line(
                    9 * self.hauteur_fenetre / 400
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 11 * self.hauteur_fenetre / 100,
                    7 * self.hauteur_fenetre / 400
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 12 * self.hauteur_fenetre / 100,
                    width=2,
                    fill="white",
                )
                ovale1 = self.canva.create_oval(
                    (len(self.actifA) + 1) * self.echelle // 2
                    - 3 * self.hauteur_fenetre / 100
                    + increment,
                    self.largeur + 21 * self.hauteur_fenetre / 200,
                    (len(self.actifA) + 1) * self.echelle // 2
                    - self.hauteur_fenetre / 100
                    + increment,
                    self.largeur + 5 * self.hauteur_fenetre / 40,
                    width=2,
                    outline="white",
                )
                ovale2 = self.canva.create_oval(
                    self.hauteur_fenetre / 100
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 21 * self.hauteur_fenetre / 200,
                    3 * self.hauteur_fenetre / 100
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 5 * self.hauteur_fenetre / 40,
                    width=2,
                    outline="white",
                )
                increment += self.echelle * (len(self.actifA) + 1)
            increment = 0
            for i in range(len(self.actifA)):
                rectangle1 = self.canva.create_rectangle(
                    -7 * self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 14 * self.hauteur_fenetre / 100,
                    -self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 17 * self.hauteur_fenetre / 100,
                    width=1,
                    fill="red4",
                )
                self.listebouton3.append(rectangle1)
                rectangle2 = self.canva.create_rectangle(
                    self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 14 * self.hauteur_fenetre / 100,
                    7 * self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 17 * self.hauteur_fenetre / 100,
                    width=1,
                    fill="red4",
                )
                self.listebouton3.append(rectangle2)
                droite = self.canva.create_line(
                    -5 * self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 31 * self.hauteur_fenetre / 200,
                    -3 * self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 31 * self.hauteur_fenetre / 200,
                    width=2,
                    fill="white",
                    arrow="first",
                )

                gauche = self.canva.create_line(
                    3 * self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 31 * self.hauteur_fenetre / 200,
                    5 * self.hauteur_fenetre / 200
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 31 * self.hauteur_fenetre / 200,
                    width=2,
                    fill="white",
                    arrow="last",
                )
                self.canva.create_oval(
                    -3 * self.hauteur_fenetre / 100
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 29 * self.hauteur_fenetre / 200,
                    -self.hauteur_fenetre / 100
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 33 * self.hauteur_fenetre / 200,
                    width=2,
                    outline="white",
                )
                self.canva.create_oval(
                    self.hauteur_fenetre / 100
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 29 * self.hauteur_fenetre / 200,
                    3 * self.hauteur_fenetre / 100
                    + (len(self.actifA) + 1) * self.echelle // 2
                    + increment,
                    self.largeur + 33 * self.hauteur_fenetre / 200,
                    width=2,
                    outline="white",
                )
                increment += self.echelle * (len(self.actifA) + 1)

        self.etoile.delete("all")
        self.etoile1 = self.etoile.create_polygon(
            [
                self.hauteur_fenetre / 10,
                4 * self.hauteur_fenetre / 100,
                23 * self.hauteur_fenetre / 200,
                7 * self.hauteur_fenetre / 100,
                15 * self.hauteur_fenetre / 100,
                3 * self.hauteur_fenetre / 40,
                12 * self.hauteur_fenetre / 100,
                self.hauteur_fenetre / 10,
                13 * self.hauteur_fenetre / 100,
                13 * self.hauteur_fenetre / 100,
                self.hauteur_fenetre / 10,
                23 * self.hauteur_fenetre / 200,
                7 * self.hauteur_fenetre / 100,
                13 * self.hauteur_fenetre / 100,
                3 * self.hauteur_fenetre / 40,
                self.hauteur_fenetre / 10,
                5 * self.hauteur_fenetre / 100,
                3 * self.hauteur_fenetre / 40,
                17 * self.hauteur_fenetre / 200,
                7 * self.hauteur_fenetre / 100,
            ],
            fill="yellow",
            width=4,
            outline="black",
        )
        self.listeetoile[self.actifniveau][1]
        self.etoile2 = self.etoile.create_polygon(
            [
                3 * self.hauteur_fenetre / 10,
                4 * self.hauteur_fenetre / 100,
                63 * self.hauteur_fenetre / 200,
                7 * self.hauteur_fenetre / 100,
                35 * self.hauteur_fenetre / 100,
                3 * self.hauteur_fenetre / 40,
                32 * self.hauteur_fenetre / 100,
                self.hauteur_fenetre / 10,
                33 * self.hauteur_fenetre / 100,
                13 * self.hauteur_fenetre / 100,
                3 * self.hauteur_fenetre / 10,
                23 * self.hauteur_fenetre / 200,
                27 * self.hauteur_fenetre / 100,
                13 * self.hauteur_fenetre / 100,
                11 * self.hauteur_fenetre / 40,
                self.hauteur_fenetre / 10,
                25 * self.hauteur_fenetre / 100,
                3 * self.hauteur_fenetre / 40,
                57 * self.hauteur_fenetre / 200,
                7 * self.hauteur_fenetre / 100,
            ],
            fill="yellow",
            width=4,
            outline="black",
        )
        self.etoile3 = self.etoile.create_polygon(
            [
                5 * self.hauteur_fenetre / 10,
                4 * self.hauteur_fenetre / 100,
                103 * self.hauteur_fenetre / 200,
                7 * self.hauteur_fenetre / 100,
                55 * self.hauteur_fenetre / 100,
                3 * self.hauteur_fenetre / 40,
                52 * self.hauteur_fenetre / 100,
                self.hauteur_fenetre / 10,
                53 * self.hauteur_fenetre / 100,
                13 * self.hauteur_fenetre / 100,
                5 * self.hauteur_fenetre / 10,
                23 * self.hauteur_fenetre / 200,
                47 * self.hauteur_fenetre / 100,
                13 * self.hauteur_fenetre / 100,
                19 * self.hauteur_fenetre / 40,
                self.hauteur_fenetre / 10,
                45 * self.hauteur_fenetre / 100,
                3 * self.hauteur_fenetre / 40,
                97 * self.hauteur_fenetre / 200,
                7 * self.hauteur_fenetre / 100,
            ],
            fill="yellow",
            width=4,
            outline="black",
        )
        self.etoile.create_text(
            3 * self.hauteur_fenetre / 10,
            9 * self.hauteur_fenetre / 100,
            anchor="center",
            font="Helvetica " + str(int(2 * self.hauteur_fenetre / 100)) + " bold",
            text=str(self.listeetoile[self.actifniveau][1]),
        )
        self.etoile.create_text(
            5 * self.hauteur_fenetre / 10,
            9 * self.hauteur_fenetre / 100,
            anchor="center",
            font="Helvetica " + str(int(2 * self.hauteur_fenetre / 100)) + " bold",
            text=str(self.listeetoile[self.actifniveau][0]),
        )
        if self.emojie == 0 and self.nourriture == 1:
            self.etoile.create_text(
                3 * self.hauteur_fenetre / 10,
                19 * self.hauteur_fenetre / 100,
                anchor="n",
                text="cowabunga!",
                font="Helvetica "
                + str(int(4 * self.hauteur_fenetre / 100))
                + " normal",
                fill="lawn green",
            )
        else:
            self.etoile.create_text(
                3 * self.hauteur_fenetre / 10,
                19 * self.hauteur_fenetre / 100,
                anchor="n",
                text="gagné!",
                font="Helvetica "
                + str(int(4 * self.hauteur_fenetre / 100))
                + " normal",
                fill="lawn green",
            )
        self.etoile.create_text(
            3 * self.hauteur_fenetre / 10,
            26 * self.hauteur_fenetre / 100,
            anchor="n",
            text="niveau " + str(self.actifniveau + 1),
            font="Helvetica " + str(int(2 * self.hauteur_fenetre / 100)) + " normal",
            fill="light grey",
        )
        if self.actifniveau == 39:
            self.continuer2.config(
                text="credit",
                command=lambda: [
                    self.unpack(),
                    self.gagne.place_forget(),
                    self.credit(),
                ],
            )
        else:
            self.continuer2.config(
                text="niveau suivant",
                command=lambda: [
                    self.unpack(),
                    self.gagne.place_forget(),
                    self.changesysteme("niveau 0" + str(self.actifniveau + 2)),
                    self.pack(),
                ],
            )

    def credit(self):
        self.diamant.pack_forget()
        self.creditcanva.pack()
        self.menu.pack()

    def reesaye(self):
        self.actifniveau -= 1
        self.systeme.set("niveau 0" + str(self.actifniveau + 2))
        self.changesysteme("niveau 0" + str(self.actifniveau + 2))

    def echange(self, ligne1, ligne2):
        self.coup += 1
        a = str(self.coup)
        while len(a) < 3:
            a = "0" + a
        if self.coup == self.listeetoile[self.actifniveau][0] + 1:
            self.pause.itemconfig(self.pauseetoile[2], image=self.etoilegrise)
        elif self.coup == self.listeetoile[self.actifniveau][1] + 1:
            self.pause.itemconfig(self.pauseetoile[1], image=self.etoilegrise)
        if self.coup > self.listeetoile[self.actifniveau][1]:
            self.pause.itemconfig(self.itemcoup, text="nombre de coups: " + a)
        elif self.coup > self.listeetoile[self.actifniveau][0]:
            self.pause.itemconfig(
                self.itemcoup,
                text="nombre de coups: "
                + a
                + "/"
                + str(self.listeetoile[self.actifniveau][1]),
            )
        else:
            self.pause.itemconfig(
                self.itemcoup,
                text="nombre de coups: "
                + a
                + "/"
                + str(self.listeetoile[self.actifniveau][0]),
            )

        x, y = self.actifAi[ligne2].copy(), self.actifAi[ligne1].copy()
        self.actifAi[ligne1], self.actifAi[ligne2] = x, y
        x, y = self.listemultiplicateur[ligne2], self.listemultiplicateur[ligne1]
        self.listemultiplicateur[ligne1], self.listemultiplicateur[ligne2] = x, y
        x, y = self.actifBi[ligne2].copy(), self.actifBi[ligne1].copy()
        # tortugauss >>> escargauss
        self.actifBi[ligne1], self.actifBi[ligne2] = x, y

        for k in range(len(self.actifA)):
            self.changemult(0, k)

    def changemult(self, increment, ligne):
        self.listemultiplicateur[ligne] += increment
        if round(self.listemultiplicateur[ligne], 4) == 0:
            self.listemultiplicateur[ligne] += increment
        for i in range(len(self.actifA)):
            self.actifB[ligne] = self.actifBi[ligne] * self.listemultiplicateur[ligne]
        for k in range(len(self.actifA)):
            self.actifA[ligne][k] = (
                self.actifAi[ligne][k] * self.listemultiplicateur[ligne]
            )
        for k in range(len(self.actifA)):
            self.changex(0, k, 0)

        if self.variable.get() == "x":
            self.echellex = self.echelle / len(self.actifA)
            self.canva.coords(
                self.listeboule[ligne][0],
                self.largeur // 2
                + (self.echellex + 1)
                * (-len(self.actifA) * 3 / 8 + self.actifB[ligne]),
                (self.echelle + 1)
                * (len(self.actifA) * (ligne + 1 + 1 / (8 * len(self.actifA))))
                + (self.echelle + 1) * ligne,
            )
            decalage = (self.echelle + 1) * (
                len(self.actifA) * (ligne + 1 + 1 / (2 * len(self.actifA)))
            ) + (self.echelle + 1) * ligne

            if self.canva.coords(self.listeboule[ligne][0])[0] > self.largeur:
                self.canva.coords(
                    self.listefleche[ligne],
                    self.largeur - self.hauteur_fenetre / 10,
                    decalage,
                    self.largeur - self.hauteur_fenetre / 25,
                    decalage,
                )
                self.canva.coords(
                    self.listeboule[ligne][0],
                    -self.hauteur_fenetre / 10,
                    -self.hauteur_fenetre / 10,
                )
            elif self.canva.coords(self.listeboule[ligne][0])[0] < 0:
                self.canva.coords(
                    self.listefleche[ligne],
                    self.hauteur_fenetre / 10,
                    decalage,
                    4 * self.hauteur_fenetre / 100,
                    decalage,
                )
            else:
                self.canva.coords(
                    self.listefleche[ligne],
                    self.largeur // 2,
                    decalage,
                    self.largeur // 2,
                    decalage,
                )
        else:
            self.echellex = self.echelle / len(self.actifA)
            self.canva.coords(
                self.listeboule[ligne][0],
                (self.echelle + 1)
                * (len(self.actifA) * (ligne + 1 + 1 / (8 * len(self.actifA))))
                + (self.echelle + 1) * ligne,
                self.largeur // 2
                - (self.echellex + 1) * (len(self.actifA) * 3 / 8 + self.actifB[ligne]),
            )
            decalage = (self.echelle + 1) * (
                len(self.actifA) * (ligne + 1 + 1 / (2 * len(self.actifA)))
            ) + (self.echelle + 1) * ligne

            if self.canva.coords(self.listeboule[ligne][0])[1] > self.largeur:
                self.canva.coords(
                    self.listefleche[ligne],
                    decalage,
                    self.largeur - self.hauteur_fenetre / 10,
                    decalage,
                    self.largeur - self.hauteur_fenetre / 25,
                )
                self.canva.coords(
                    self.listeboule[ligne][0],
                    -self.hauteur_fenetre / 10,
                    -self.hauteur_fenetre / 10,
                )
            elif self.canva.coords(self.listeboule[ligne][0])[1] < 0:
                self.canva.coords(
                    self.listefleche[ligne],
                    decalage,
                    self.hauteur_fenetre / 10,
                    decalage,
                    self.hauteur_fenetre / 25,
                )
            else:
                self.canva.coords(
                    self.listefleche[ligne],
                    decalage,
                    self.largeur // 2,
                    decalage,
                    self.largeur // 2,
                )

    def changex(self, increment, ligne, gagne):
        self.bouton.coords(
            self.listejauge[ligne],
            self.hauteur_fenetre / 10 + ligne * self.hauteur_fenetre / 5,
            2 * self.hauteur_fenetre / 20 - 2 * self.hauteur_fenetre / 100,
            self.hauteur_fenetre / 10
            + (self.actifX[ligne] + increment) * 2 * self.hauteur_fenetre / 100
            + ligne * self.hauteur_fenetre / 5,
            2 * self.hauteur_fenetre / 20 - self.hauteur_fenetre / 200,
        )
        if self.variable.get() == "x":
            self.actifX[ligne] += increment
            self.echellex = self.echelle / len(self.actifA)
            bjuste = 0
            for i in range(len(self.listerectangle)):
                x11, y11, x21, y21 = self.canva.coords(self.listerectangle[i][ligne])
                self.canva.coords(
                    self.listerectangle[i][ligne],
                    self.largeur // 2,
                    i * (self.echelle + 1) * (len(self.actifA) + 1)
                    + (self.echelle + 1) * ligne,
                    self.largeur // 2
                    + self.actifA[i][ligne] * self.actifX[ligne] * (self.echellex + 1),
                    i * (self.echelle + 1) * (len(self.actifA) + 1)
                    + (self.echelle + 1) * ligne
                    + self.echelle
                    + 1,
                )
                x12, y12, x22, y22 = self.canva.coords(self.listerectangle[i][ligne])
                x1, y1 = self.canva.coords(self.listeboule[i][1])

                bobtenu = round(self.actifA.dot(self.actifX)[i], 3)

                self.canva.coords(
                    self.listeboule[i][1],
                    x1 + x22 - x21 + x12 - x11,
                    y1,
                )
                jauge = 0.2
                if x1 > self.largeur:
                    self.trans = ImageTk.PhotoImage(
                        Image.open("projet tortuga/trans.png")
                    )
                    self.canva.itemconfig(self.listeboule[i][1], image=self.trans)
                elif bobtenu + jauge >= round(self.actifB[i], 3) >= bobtenu - jauge:
                    self.gifcheck[i] = True
                    self.codegif[i] += 1
                    self.updategif(i, self.codegif[i])
                    bjuste += 1
                else:
                    self.canva.itemconfig(self.listeboule[i][1], image=self.mimtortue)
                    self.gifcheck[i] = False
            if bjuste == len(self.actifB) and gagne == 1:
                if self.actifniveau == 7:
                    anciennecomb = (
                        int(self.anciennecombine[0])
                        + round(int(self.anciennecombine[1]) / 10, 1),
                        int(self.anciennecombine[2])
                        + round(int(self.anciennecombine[3]) / 10, 1),
                    )

                    if (
                        self.actifX[0] == anciennecomb[0]
                        or self.actifX[1] == anciennecomb[1]
                    ):
                        self.bouton.itemconfig(
                            self.comment,
                            text="cette solution a déja était choisi au niveau précédent\nessayez d'en trouver une autre",
                        )
                    else:
                        self.gagné()
                else:
                    self.gagné()
            self.canva.create_line(
                self.largeur // 2,
                0,
                self.largeur // 2,
                self.hauteur + 1 + len(self.actifA),
                width=3,
                fill="gold",
            )
            self.canva.create_line(
                self.largeur // 2 - 2,
                0,
                self.largeur // 2 - 2,
                self.hauteur + 1 + len(self.actifA),
                width=1,
                fill="black",
            )
            self.canva.create_line(
                self.largeur // 2 + 2,
                0,
                self.largeur // 2 + 2,
                self.hauteur + 1 + len(self.actifA),
                width=1,
                fill="black",
            )
        else:
            self.actifX[ligne] += increment
            self.echellex = self.echelle / len(self.actifA)
            bjuste = 0
            for i in range(len(self.listerectangle)):
                self.gifcheck[i] = True
                x11, y11, x21, y21 = self.canva.coords(self.listerectangle[i][ligne])
                self.canva.coords(
                    self.listerectangle[i][ligne],
                    i * (self.echelle + 1) * (len(self.actifA) + 1)
                    + (self.echelle + 1) * ligne,
                    self.largeur // 2,
                    i * (self.echelle + 1) * (len(self.actifA) + 1)
                    + (self.echelle + 1) * ligne
                    + self.echelle
                    + 1,
                    self.largeur // 2
                    - self.actifA[i][ligne] * self.actifX[ligne] * (self.echellex + 1),
                )
                x12, y12, x22, y22 = self.canva.coords(self.listerectangle[i][ligne])
                x1, y1 = self.canva.coords(self.listeboule[i][1])

                bobtenu = round(self.actifA.dot(self.actifX)[i], 3)

                self.canva.coords(
                    self.listeboule[i][1],
                    x1,
                    y1 + y22 - y21 + y12 - y11,
                )

                jauge = 0.2
                if y1 > self.largeur:
                    self.trans = ImageTk.PhotoImage(
                        Image.open("projet tortuga/trans.png")
                    )
                    self.canva.itemconfig(self.listeboule[i][1], image=self.trans)
                elif bobtenu + jauge >= round(self.actifB[i], 3) >= bobtenu - jauge:
                    self.gifcheck[i] = True
                    self.codegif[i] += 1
                    self.updategif(i, self.codegif[i])
                    bjuste += 1
                else:
                    self.canva.itemconfig(self.listeboule[i][1], image=self.mimtortue)
                    self.gifcheck[i] = False
            if bjuste == len(self.actifB) and gagne == 1:
                if self.actifniveau == 7:
                    anciennecomb = (
                        int(self.anciennecombine[0])
                        + round(int(self.anciennecombine[1]) / 10, 1),
                        int(self.anciennecombine[2])
                        + round(int(self.anciennecombine[3]) / 10, 1),
                    )

                    if (
                        round(float(self.actifX[0]), 1) == anciennecomb[0]
                        or round(float(self.actifX[1]), 1) == anciennecomb[1]
                    ):
                        self.bouton.itemconfig(
                            self.comment,
                            text="cette solution a déja était choisi au niveau précédent\nessayez d'en trouver une autre",
                        )
                    else:
                        self.gagné()
                else:
                    self.gagné()

            self.canva.create_line(
                0,
                self.largeur // 2,
                self.hauteur + 1 + len(self.actifA),
                self.largeur // 2,
                width=3,
                fill="gold",
            )
            self.canva.create_line(
                0,
                self.largeur // 2 - 2,
                self.hauteur + 1 + len(self.actifA),
                self.largeur // 2 - 2,
                width=1,
                fill="black",
            )
            self.canva.create_line(
                0,
                self.largeur // 2 + 2,
                self.hauteur + 1 + len(self.actifA),
                self.largeur // 2 + 2,
                width=1,
                fill="black",
            )
        if (
            self.actifniveau == 11
            or self.actifniveau == 12
            or self.actifniveau == 13
            or self.actifniveau == 14
        ):
            if self.variable.get() == "x":
                bjuste = 0
                for i in range(len(self.listerectangle2)):
                    x11, y11, x21, y21 = self.canva2.coords(
                        self.listerectangle2[i][ligne]
                    )
                    self.canva2.coords(
                        self.listerectangle2[i][ligne],
                        self.largeur // 2,
                        i * (self.echelle + 1) * (len(self.actifA) + 1)
                        + (self.echelle + 1) * ligne,
                        self.largeur // 2
                        + self.actifA2[i][ligne]
                        * self.actifX[ligne]
                        * (self.echellex + 1),
                        i * (self.echelle + 1) * (len(self.actifA2) + 1)
                        + (self.echelle + 1) * ligne
                        + self.echelle
                        + 1,
                    )
                    x12, y12, x22, y22 = self.canva2.coords(
                        self.listerectangle2[i][ligne]
                    )
                    x1, y1 = self.canva2.coords(self.listeboule2[i][1])

                    bobtenu = round(self.actifA2.dot(self.actifX)[i], 3)
                    jauge = 0.2
                    self.canva2.coords(
                        self.listeboule2[i][1],
                        x1 + x22 - x21 + x12 - x11,
                        y1,
                    )
                    if x1 > self.largeur:
                        self.trans = ImageTk.PhotoImage(
                            Image.open("projet tortuga/trans.png")
                        )
                        self.canva.itemconfig(self.listeboule2[i][1], image=self.trans)
                    elif (
                        bobtenu + jauge >= round(self.actifB2[i], 3) >= bobtenu - jauge
                    ):
                        self.gifcheck2[i] = True
                        self.codegif2[i] += 1
                        self.updategif(i, self.codegif2[i], 2)
                        bjuste += 1
                    else:
                        self.canva2.itemconfig(
                            self.listeboule2[i][1], image=self.mimtortue
                        )
                        self.gifcheck2[i] = False
                self.canva2.create_line(
                    self.largeur // 2,
                    0,
                    self.largeur // 2,
                    self.hauteur + 1 + len(self.actifA),
                    width=3,
                    fill="gold",
                )
                self.canva2.create_line(
                    self.largeur // 2 - 2,
                    0,
                    self.largeur // 2 - 2,
                    self.hauteur + 1 + len(self.actifA),
                    width=1,
                    fill="black",
                )
                self.canva2.create_line(
                    self.largeur // 2 + 2,
                    0,
                    self.largeur // 2 + 2,
                    self.hauteur + 1 + len(self.actifA),
                    width=1,
                    fill="black",
                )
            else:
                bjuste = 0
                for i in range(len(self.listerectangle)):
                    self.gifcheck2[i] = True
                    x11, y11, x21, y21 = self.canva2.coords(
                        self.listerectangle2[i][ligne]
                    )
                    self.canva2.coords(
                        self.listerectangle2[i][ligne],
                        i * (self.echelle + 1) * (len(self.actifA) + 1)
                        + (self.echelle + 1) * ligne,
                        self.largeur // 2,
                        i * (self.echelle + 1) * (len(self.actifA) + 1)
                        + (self.echelle + 1) * ligne
                        + self.echelle
                        + 1,
                        self.largeur // 2
                        - self.actifA2[i][ligne]
                        * self.actifX[ligne]
                        * (self.echellex + 1),
                    )
                    x12, y12, x22, y22 = self.canva2.coords(
                        self.listerectangle2[i][ligne]
                    )
                    x1, y1 = self.canva2.coords(self.listeboule2[i][1])

                    bobtenu = round(self.actifA2.dot(self.actifX)[i], 3)

                    self.canva2.coords(
                        self.listeboule2[i][1],
                        x1,
                        y1 + y22 - y21 + y12 - y11,
                    )

                    jauge = 0.2
                    if y1 > self.largeur:
                        self.trans = ImageTk.PhotoImage(
                            Image.open("projet tortuga/trans.png")
                        )
                        self.canva2.itemconfig(self.listeboule2[i][1], image=self.trans)
                    elif (
                        bobtenu + jauge >= round(self.actifB2[i], 3) >= bobtenu - jauge
                    ):
                        self.gifcheck2[i] = True
                        self.codegif2[i] += 1
                        self.updategif(i, self.codegif2[i], 2)
                        bjuste += 1
                    else:
                        self.canva2.itemconfig(
                            self.listeboule2[i][1], image=self.mimtortue
                        )
                        self.gifcheck2[i] = False

                self.canva2.create_line(
                    0,
                    self.largeur // 2,
                    self.hauteur + 1 + len(self.actifA),
                    self.largeur // 2,
                    width=3,
                    fill="gold",
                )
                self.canva2.create_line(
                    0,
                    self.largeur // 2 - 2,
                    self.hauteur + 1 + len(self.actifA),
                    self.largeur // 2 - 2,
                    width=1,
                    fill="black",
                )
                self.canva2.create_line(
                    0,
                    self.largeur // 2 + 2,
                    self.hauteur + 1 + len(self.actifA),
                    self.largeur // 2 + 2,
                    width=1,
                    fill="black",
                )

    def gauss(self, ajoute, ligne1, ligne2):
        self.coup += 1
        a = str(self.coup)
        while len(a) < 3:
            a = "0" + a
            # Eytan, Lisa, Oriane et Violette sont des Goats
        if self.coup == self.listeetoile[self.actifniveau][0] + 1:
            self.pause.itemconfig(self.pauseetoile[2], image=self.etoilegrise)
        elif self.coup == self.listeetoile[self.actifniveau][1] + 1:
            self.pause.itemconfig(self.pauseetoile[1], image=self.etoilegrise)
        if self.coup > self.listeetoile[self.actifniveau][1]:
            self.pause.itemconfig(self.itemcoup, text="nombre de coups: " + a)
        elif self.coup > self.listeetoile[self.actifniveau][0]:
            self.pause.itemconfig(
                self.itemcoup,
                text="nombre de coups: "
                + a
                + "/"
                + str(self.listeetoile[self.actifniveau][1]),
            )
        else:
            self.pause.itemconfig(
                self.itemcoup,
                text="nombre de coups: "
                + a
                + "/"
                + str(self.listeetoile[self.actifniveau][0]),
            )

        if ajoute == 1:
            self.actifAi[ligne1] *= self.listemultiplicateur[ligne1]
            self.actifAi[ligne2] *= self.listemultiplicateur[ligne2]
            self.actifAi[ligne1] += self.actifAi[ligne2]
            self.actifAi[ligne1] /= self.listemultiplicateur[ligne1]
            self.actifAi[ligne2] /= self.listemultiplicateur[ligne2]
            self.actifBi[ligne1] *= self.listemultiplicateur[ligne1]
            self.actifBi[ligne2] *= self.listemultiplicateur[ligne2]
            self.actifBi[ligne1] += self.actifBi[ligne2]
            self.actifBi[ligne1] /= self.listemultiplicateur[ligne1]
            self.actifBi[ligne2] /= self.listemultiplicateur[ligne2]
            self.changemult(0, ligne1)
        elif ajoute == -1:
            self.actifAi[ligne1] *= self.listemultiplicateur[ligne1]
            self.actifAi[ligne2] *= self.listemultiplicateur[ligne2]
            self.actifAi[ligne1] -= self.actifAi[ligne2]
            self.actifAi[ligne1] /= self.listemultiplicateur[ligne1]
            self.actifAi[ligne2] /= self.listemultiplicateur[ligne2]
            self.actifBi[ligne1] *= self.listemultiplicateur[ligne1]
            self.actifBi[ligne2] *= self.listemultiplicateur[ligne2]
            self.actifBi[ligne1] -= self.actifBi[ligne2]
            self.actifBi[ligne1] /= self.listemultiplicateur[ligne1]
            self.actifBi[ligne2] /= self.listemultiplicateur[ligne2]
            self.changemult(0, ligne1)

    def click(self, event):
        self.boutonactif = 1
        if self.actifniveau == 5:
            if time.time() - self.lvl5timer1 > 5 and self.coup > 30:
                if self.nonsolution is None:
                    self.bouton.itemconfig(
                        self.comment,
                        text="tu as du mal? Si tu pense qu'il n y a pas de solution,\nalors appuis sur ce nouveau bouton",
                    )

                    self.nonsolution = self.bouton.create_rectangle(
                        45 * self.hauteur_fenetre / 100,
                        3 * self.hauteur_fenetre / 100,
                        60 * self.hauteur_fenetre / 100,
                        10 * self.hauteur_fenetre / 100,
                        width=2,
                        fill="white",
                    )
                    self.bouton.create_text(
                        46 * self.hauteur_fenetre / 100,
                        4 * self.hauteur_fenetre / 100,
                        anchor="nw",
                        text="pas de \nsolution",
                        font="Helvetica "
                        + str(int(2 * self.hauteur_fenetre / 100))
                        + " normal",
                        fill="black",
                    )
                else:
                    if (
                        3 * self.hauteur_fenetre / 100
                        < event.y
                        < 10 * self.hauteur_fenetre / 100
                        and self.stop
                    ):
                        if (
                            45 * self.hauteur_fenetre / 100
                            < event.x
                            < 60 * self.hauteur_fenetre / 100
                        ):
                            self.bouton.itemconfig(self.nonsolution, fill="Lavender")
                            self.gagné()

        if (
            3 * self.hauteur_fenetre / 100 < event.y < 7 * self.hauteur_fenetre / 100
            and self.stop
        ):
            for i in range(len(self.actifA)):
                if (
                    self.hauteur_fenetre / 20 + 2 * self.hauteur_fenetre / 10 * i
                    < event.x
                    < i * 2 * self.hauteur_fenetre / 10 + self.hauteur_fenetre / 10
                ):
                    self.bouton.itemconfig(
                        self.listebouton[i][0], fill=self.activecouleur[i]
                    )

                    if -2.5 < self.actifX[i]:
                        self.coup += 1
                        a = str(self.coup)
                        while len(a) < 3:
                            a = "0" + a
                        if self.coup == self.listeetoile[self.actifniveau][0] + 1:
                            self.pause.itemconfig(
                                self.pauseetoile[2], image=self.etoilegrise
                            )
                        elif self.coup == self.listeetoile[self.actifniveau][1] + 1:
                            self.pause.itemconfig(
                                self.pauseetoile[1], image=self.etoilegrise
                            )
                        if self.coup > self.listeetoile[self.actifniveau][1]:
                            self.pause.itemconfig(
                                self.itemcoup, text="nombre de coups: " + a
                            )
                        elif self.coup > self.listeetoile[self.actifniveau][0]:
                            self.pause.itemconfig(
                                self.itemcoup,
                                text="nombre de coups: "
                                + a
                                + "/"
                                + str(self.listeetoile[self.actifniveau][1]),
                            )
                        else:
                            self.pause.itemconfig(
                                self.itemcoup,
                                text="nombre de coups: "
                                + a
                                + "/"
                                + str(self.listeetoile[self.actifniveau][0]),
                            )
                        l = i
                        self.listeaction.append(lambda: self.changex(0.1, l, 1))
                        self.changex(-0.1, i, 1)
                elif (
                    self.hauteur_fenetre / 10 + 2 * self.hauteur_fenetre / 10 * i
                    < event.x
                    < 3 * self.hauteur_fenetre / 20 + i * 2 * self.hauteur_fenetre / 10
                ):
                    self.bouton.itemconfig(
                        self.listebouton[i][1], fill=self.activecouleur[i]
                    )

                    if self.actifX[i] < 2.5:
                        self.coup += 1
                        a = str(self.coup)
                        while len(a) < 3:
                            a = "0" + a
                        if self.coup == self.listeetoile[self.actifniveau][0] + 1:
                            self.pause.itemconfig(
                                self.pauseetoile[2], image=self.etoilegrise
                            )
                        elif self.coup == self.listeetoile[self.actifniveau][1] + 1:
                            self.pause.itemconfig(
                                self.pauseetoile[1], image=self.etoilegrise
                            )

                        if self.coup > self.listeetoile[self.actifniveau][1]:
                            self.pause.itemconfig(
                                self.itemcoup, text="nombre de coups: " + a
                            )
                        elif self.coup > self.listeetoile[self.actifniveau][0]:
                            self.pause.itemconfig(
                                self.itemcoup,
                                text="nombre de coups: "
                                + a
                                + "/"
                                + str(self.listeetoile[self.actifniveau][1]),
                            )
                        else:
                            self.pause.itemconfig(
                                self.itemcoup,
                                text="nombre de coups: "
                                + a
                                + "/"
                                + str(self.listeetoile[self.actifniveau][0]),
                            )
                        l = i
                        self.listeaction.append(lambda: self.changex(-0.1, l, 1))
                        self.changex(0.1, i, 1)
            if (
                4 * self.hauteur_fenetre / 5
                < event.x
                < 3 * self.hauteur_fenetre / 40 + 4 * self.hauteur_fenetre / 5
            ):
                self.bouton.itemconfig(self.boutonretour, fill="Lavender")
                self.retour()
        t1 = time.time()
        while self.boutonactif == 1:
            if time.time() - t1 > 0.2:
                if (
                    3 * self.hauteur_fenetre / 100
                    < event.y
                    < 7 * self.hauteur_fenetre / 100
                ) and self.stop:
                    for i in range(len(self.actifA)):
                        if (
                            self.hauteur_fenetre / 20
                            + 2 * self.hauteur_fenetre / 10 * i
                            < event.x
                            < self.hauteur_fenetre / 10
                            + i * 2 * self.hauteur_fenetre / 10
                        ):
                            self.bouton.itemconfig(
                                self.listebouton[i][0], fill=self.activecouleur[i]
                            )

                            if -2.5 < self.actifX[i]:
                                self.coup += 1
                                a = str(self.coup)
                                while len(a) < 3:
                                    a = "0" + a
                                if (
                                    self.coup
                                    == self.listeetoile[self.actifniveau][0] + 1
                                ):
                                    self.pause.itemconfig(
                                        self.pauseetoile[2], image=self.etoilegrise
                                    )
                                elif (
                                    self.coup
                                    == self.listeetoile[self.actifniveau][1] + 1
                                ):
                                    self.pause.itemconfig(
                                        self.pauseetoile[1], image=self.etoilegrise
                                    )

                                if self.coup > self.listeetoile[self.actifniveau][1]:
                                    self.pause.itemconfig(
                                        self.itemcoup, text="nombre de coups: " + a
                                    )
                                elif self.coup > self.listeetoile[self.actifniveau][0]:
                                    self.pause.itemconfig(
                                        self.itemcoup,
                                        text="nombre de coups: "
                                        + a
                                        + "/"
                                        + str(self.listeetoile[self.actifniveau][1]),
                                    )
                                else:
                                    self.pause.itemconfig(
                                        self.itemcoup,
                                        text="nombre de coups: "
                                        + a
                                        + "/"
                                        + str(self.listeetoile[self.actifniveau][0]),
                                    )
                                l = i

                                self.listeaction.append(lambda: self.changex(0.1, l, 1))
                                self.changex(-0.1, i, 1)
                        elif (
                            self.hauteur_fenetre / 10
                            + 2 * self.hauteur_fenetre / 10 * i
                            < event.x
                            < 3 * self.hauteur_fenetre / 20
                            + i * 2 * self.hauteur_fenetre / 10
                        ):
                            self.bouton.itemconfig(
                                self.listebouton[i][1], fill=self.activecouleur[i]
                            )

                            if self.actifX[i] < 2.5:
                                self.coup += 1
                                a = str(self.coup)
                                while len(a) < 3:
                                    a = "0" + a
                                if (
                                    self.coup
                                    == self.listeetoile[self.actifniveau][0] + 1
                                ):
                                    self.pause.itemconfig(
                                        self.pauseetoile[2], image=self.etoilegrise
                                    )
                                elif (
                                    self.coup
                                    == self.listeetoile[self.actifniveau][1] + 1
                                ):
                                    self.pause.itemconfig(
                                        self.pauseetoile[1], image=self.etoilegrise
                                    )

                                if self.coup > self.listeetoile[self.actifniveau][1]:
                                    self.pause.itemconfig(
                                        self.itemcoup, text="nombre de coups: " + a
                                    )
                                elif self.coup > self.listeetoile[self.actifniveau][0]:
                                    self.pause.itemconfig(
                                        self.itemcoup,
                                        text="nombre de coups: "
                                        + a
                                        + "/"
                                        + str(self.listeetoile[self.actifniveau][1]),
                                    )
                                else:
                                    self.pause.itemconfig(
                                        self.itemcoup,
                                        text="nombre de coups: "
                                        + a
                                        + "/"
                                        + str(self.listeetoile[self.actifniveau][0]),
                                    )
                                l = i
                                self.listeaction.append(
                                    lambda: self.changex(-0.1, l, 1)
                                )
                                self.changex(0.1, i, 1)
                t1 = time.time()
            self.update()
        for i in range(len(self.actifA)):
            self.bouton.itemconfig(self.listebouton[i][1], fill=self.couleurs[i])

    def click2(self, event):
        self.boutonactif = 0
        if self.variable.get() == "x":
            décallage = (
                len(self.actifA) + 1
            ) * self.echelle // 2 - 5 * self.hauteur_fenetre / 100
            if (
                self.largeur + self.hauteur_fenetre / 10
                < event.x
                < self.largeur + 13 * self.hauteur_fenetre / 100
            ):
                for i in range(len(self.actifB)):
                    if (
                        3 * self.hauteur_fenetre / 200
                        + self.echelle * (len(self.actifA) + 1) * i
                        < event.y - décallage
                        < 9 * self.hauteur_fenetre / 200
                        + self.echelle * (len(self.actifA) + 1) * i
                    ):
                        self.coup += 1
                        a = str(self.coup)
                        while len(a) < 3:
                            a = "0" + a
                        if self.coup == self.listeetoile[self.actifniveau][1] + 1:
                            self.pause.itemconfig(
                                self.pauseetoile[1], image=self.etoilegrise
                            )
                        elif self.coup == self.listeetoile[self.actifniveau][0] + 1:
                            self.pause.itemconfig(
                                self.pauseetoile[2], image=self.etoilegrise
                            )
                        if self.coup > self.listeetoile[self.actifniveau][1]:
                            self.pause.itemconfig(
                                self.itemcoup, text="nombre de coups: " + a
                            )
                        elif self.coup > self.listeetoile[self.actifniveau][0]:
                            self.pause.itemconfig(
                                self.itemcoup,
                                text="nombre de coups: "
                                + a
                                + "/"
                                + str(self.listeetoile[self.actifniveau][1]),
                            )
                        else:
                            self.pause.itemconfig(
                                self.itemcoup,
                                text="nombre de coups: "
                                + a
                                + "/"
                                + str(self.listeetoile[self.actifniveau][0]),
                            )

                        self.changemult(0.1, i)
                        l = i
                        self.listeaction.append(lambda: self.changemult(-0.1, l))
                        self.canva.itemconfig(self.listebouton2[2 * i], fill="red3")
                        self.boutonactif = 1
                    elif (
                        11 * self.hauteur_fenetre / 200
                        + self.echelle * (len(self.actifA) + 1) * i
                        < event.y - décallage
                        < 17 * self.hauteur_fenetre / 200
                        + self.echelle * (len(self.actifA) + 1) * i
                    ):
                        self.coup += 1
                        a = str(self.coup)
                        while len(a) < 3:
                            a = "0" + a
                        if self.coup == self.listeetoile[self.actifniveau][0] + 1:
                            self.pause.itemconfig(
                                self.pauseetoile[2], image=self.etoilegrise
                            )
                        elif self.coup == self.listeetoile[self.actifniveau][1] + 1:
                            self.pause.itemconfig(
                                self.pauseetoile[1], image=self.etoilegrise
                            )
                        if self.coup > self.listeetoile[self.actifniveau][1]:
                            self.pause.itemconfig(
                                self.itemcoup, text="nombre de coups: " + a
                            )
                        elif self.coup > self.listeetoile[self.actifniveau][0]:
                            self.pause.itemconfig(
                                self.itemcoup,
                                text="nombre de coups: "
                                + a
                                + "/"
                                + str(self.listeetoile[self.actifniveau][1]),
                            )
                        else:
                            self.pause.itemconfig(
                                self.itemcoup,
                                text="nombre de coups: "
                                + a
                                + "/"
                                + str(self.listeetoile[self.actifniveau][0]),
                            )

                        self.changemult(-0.1, i)
                        l = i
                        self.listeaction.append(lambda: self.changemult(0.1, l))
                        self.canva.itemconfig(self.listebouton2[2 * i + 1], fill="red3")
                        self.boutonactif = 1
            elif (
                self.largeur + 14 * self.hauteur_fenetre / 100
                < event.x
                < self.largeur + 17 * self.hauteur_fenetre / 100
            ):
                for i in range(len(self.actifB)):
                    if (
                        3 * self.hauteur_fenetre / 200
                        + self.echelle * (len(self.actifA) + 1) * i
                        < event.y - décallage
                        < 9 * self.hauteur_fenetre / 200
                        + self.echelle * (len(self.actifA) + 1) * i
                    ):
                        self.echange(i - 1, i)
                        l = i
                        self.listeaction.append(lambda: self.echange(l - 1, l))
                        self.canva.itemconfig(self.listebouton3[2 * i], fill="red3")
                        self.boutonactif = 1
                    elif (
                        11 * self.hauteur_fenetre / 200
                        + self.echelle * (len(self.actifA) + 1) * i
                        < event.y - décallage
                        < 17 * self.hauteur_fenetre / 200
                        + self.echelle * (len(self.actifA) + 1) * i
                    ):
                        self.echange(i, (i + 1) % len(self.actifB))
                        l = i
                        self.listeaction.append(
                            lambda: self.echange(l, (l + 1) % len(self.actifB))
                        )
                        self.canva.itemconfig(self.listebouton3[2 * i + 1], fill="red3")
                        self.boutonactif = 1

            self.actifgauss = 0
            if (
                self.largeur + 6 * self.hauteur_fenetre / 100
                < event.x
                < self.largeur + 9 * self.hauteur_fenetre / 100
            ):
                for i in range(len(self.actifB)):
                    if (
                        7 * self.hauteur_fenetre / 200
                        + self.echelle * (len(self.actifA) + 1) * i
                        < event.y - décallage
                        < 13 * self.hauteur_fenetre / 200
                        + self.echelle * (len(self.actifA) + 1) * i
                    ):
                        self.coordclick = (
                            self.largeur + 6 * self.hauteur_fenetre / 100 - event.x,
                            7 * self.hauteur_fenetre / 200
                            + self.echelle * (len(self.actifA) + 1) * i
                            - event.y
                            + décallage,
                            self.largeur + 9 * self.hauteur_fenetre / 100 - event.x,
                            13 * self.hauteur_fenetre / 200
                            + self.echelle * (len(self.actifA) + 1) * i
                            - event.y
                            + décallage,
                        )

                        self.actifgauss = 1 + i
                        for j in range(len(self.gaussemplacement)):
                            if self.gaussemplacement[j] == self.actifgauss:
                                self.gaussemplacement[j] = 0
                        self.boutonactif = 1
            elif (
                self.hauteur + 7 * self.hauteur_fenetre / 200
                < event.y
                < self.hauteur + 13 * self.hauteur_fenetre / 200
            ):
                if (
                    4 * self.hauteur_fenetre / 100
                    < event.x
                    < 7 * self.hauteur_fenetre / 100
                ):
                    i = self.gaussemplacement[0]
                    self.gaussemplacement[0] = 0
                    if i != 0:
                        self.coordclick = (
                            self.canva.coords(self.listeovalgauss[i - 1][0])[0]
                            - event.x,
                            self.canva.coords(self.listeovalgauss[i - 1][0])[1]
                            - event.y,
                            self.canva.coords(self.listeovalgauss[i - 1][0])[2]
                            - event.x,
                            self.canva.coords(self.listeovalgauss[i - 1][0])[3]
                            - event.y,
                        )
                        self.actifgauss = i

                    self.boutonactif = 1
                if (
                    14 * self.hauteur_fenetre / 100
                    < event.x
                    < 17 * self.hauteur_fenetre / 100
                ):
                    i = self.gaussemplacement[1]
                    self.gaussemplacement[1] = 0
                    if i != 0:
                        self.coordclick = (
                            self.canva.coords(self.listeovalgauss[i - 1][0])[0]
                            - event.x,
                            self.canva.coords(self.listeovalgauss[i - 1][0])[1]
                            - event.y,
                            self.canva.coords(self.listeovalgauss[i - 1][0])[2]
                            - event.x,
                            self.canva.coords(self.listeovalgauss[i - 1][0])[3]
                            - event.y,
                        )
                        self.actifgauss = i

                    self.boutonactif = 1
                if (
                    54 * self.hauteur_fenetre / 100
                    < event.x
                    < 57 * self.hauteur_fenetre / 100
                ):
                    i = self.gaussemplacement[2]
                    self.gaussemplacement[2] = 0
                    if i != 0:
                        self.coordclick = (
                            self.canva.coords(self.listeovalgauss[i - 1][0])[0]
                            - event.x,
                            self.canva.coords(self.listeovalgauss[i - 1][0])[1]
                            - event.y,
                            self.canva.coords(self.listeovalgauss[i - 1][0])[2]
                            - event.x,
                            self.canva.coords(self.listeovalgauss[i - 1][0])[3]
                            - event.y,
                        )
                        self.actifgauss = i

                    self.boutonactif = 1
                if (
                    64 * self.hauteur_fenetre / 100
                    < event.x
                    < 67 * self.hauteur_fenetre / 100
                ):
                    i = self.gaussemplacement[3]
                    self.gaussemplacement[3] = 0
                    if i != 0:
                        self.coordclick = (
                            self.canva.coords(self.listeovalgauss[i - 1][0])[0]
                            - event.x,
                            self.canva.coords(self.listeovalgauss[i - 1][0])[1]
                            - event.y,
                            self.canva.coords(self.listeovalgauss[i - 1][0])[2]
                            - event.x,
                            self.canva.coords(self.listeovalgauss[i - 1][0])[3]
                            - event.y,
                        )
                        self.actifgauss = i

                    self.boutonactif = 1
            if (
                self.hauteur + 3 * self.hauteur_fenetre / 100
                < event.y
                < self.hauteur + 7 * self.hauteur_fenetre / 100
            ):
                if (
                    22 * self.hauteur_fenetre / 100
                    < event.x
                    < 3 * self.hauteur_fenetre / 10
                ):
                    if self.gauss1actif == 1:
                        self.canva.itemconfig(self.gaussrectangle1, fill="red3")
                        self.gauss(
                            1,
                            self.gaussemplacement[0] - 1,
                            self.gaussemplacement[1] - 1,
                        )
                        A = self.gaussemplacement[0]
                        B = self.gaussemplacement[1]

                        self.listeaction.append(
                            lambda: self.gauss(
                                -1,
                                A - 1,
                                B - 1,
                            )
                        )

                if (
                    72 * self.hauteur_fenetre / 100
                    < event.x
                    < 8 * self.hauteur_fenetre / 10
                ):
                    if self.gauss2actif == 1:
                        self.canva.itemconfig(self.gaussrectangle2, fill="red3")
                        self.gauss(
                            -1,
                            self.gaussemplacement[2] - 1,
                            self.gaussemplacement[3] - 1,
                        )
                        A = self.gaussemplacement[2]
                        B = self.gaussemplacement[3]

                        self.listeaction.append(
                            lambda: self.gauss(
                                1,
                                A - 1,
                                B - 1,
                            )
                        )
            t1 = time.time()
            while self.boutonactif == 1:
                if time.time() - t1 > 0.2:
                    if (
                        self.largeur + self.hauteur_fenetre / 10
                        < event.x
                        < self.largeur + 13 * self.hauteur_fenetre / 100
                    ):
                        for i in range(len(self.actifB)):
                            if (
                                3 * self.hauteur_fenetre / 200
                                + self.echelle * (len(self.actifA) + 1) * i
                                < event.y - décallage
                                < 9 * self.hauteur_fenetre / 200
                                + self.echelle * (len(self.actifA) + 1) * i
                            ):
                                self.coup += 1
                                a = str(self.coup)
                                while len(a) < 3:
                                    a = "0" + a
                                if (
                                    self.coup
                                    == self.listeetoile[self.actifniveau][0] + 1
                                ):
                                    self.pause.itemconfig(
                                        self.pauseetoile[2], image=self.etoilegrise
                                    )
                                elif (
                                    self.coup
                                    == self.listeetoile[self.actifniveau][1] + 1
                                ):
                                    self.pause.itemconfig(
                                        self.pauseetoile[1], image=self.etoilegrise
                                    )

                                if self.coup > self.listeetoile[self.actifniveau][1]:
                                    self.pause.itemconfig(
                                        self.itemcoup, text="nombre de coups: " + a
                                    )
                                elif self.coup > self.listeetoile[self.actifniveau][0]:
                                    self.pause.itemconfig(
                                        self.itemcoup,
                                        text="nombre de coups: "
                                        + a
                                        + "/"
                                        + str(self.listeetoile[self.actifniveau][1]),
                                    )
                                else:
                                    self.pause.itemconfig(
                                        self.itemcoup,
                                        text="nombre de coups: "
                                        + a
                                        + "/"
                                        + str(self.listeetoile[self.actifniveau][0]),
                                    )

                                self.changemult(0.1, i)
                                l = i
                                self.listeaction.append(
                                    lambda: self.changemult(-0.1, l)
                                )
                                self.canva.itemconfig(
                                    self.listebouton2[2 * i], fill="red3"
                                )
                            elif (
                                11 * self.hauteur_fenetre / 200
                                + self.echelle * (len(self.actifA) + 1) * i
                                < event.y - décallage
                                < 17 * self.hauteur_fenetre / 200
                                + self.echelle * (len(self.actifA) + 1) * i
                            ):
                                self.coup += 1
                                a = str(self.coup)
                                while len(a) < 3:
                                    a = "0" + a
                                if (
                                    self.coup
                                    == self.listeetoile[self.actifniveau][0] + 1
                                ):
                                    self.pause.itemconfig(
                                        self.pauseetoile[2], image=self.etoilegrise
                                    )
                                elif (
                                    self.coup
                                    == self.listeetoile[self.actifniveau][1] + 1
                                ):
                                    self.pause.itemconfig(
                                        self.pauseetoile[1], image=self.etoilegrise
                                    )
                                if self.coup > self.listeetoile[self.actifniveau][1]:
                                    self.pause.itemconfig(
                                        self.itemcoup, text="nombre de coups: " + a
                                    )
                                elif self.coup > self.listeetoile[self.actifniveau][0]:
                                    self.pause.itemconfig(
                                        self.itemcoup,
                                        text="nombre de coups: "
                                        + a
                                        + "/"
                                        + str(self.listeetoile[self.actifniveau][1]),
                                    )
                                else:
                                    self.pause.itemconfig(
                                        self.itemcoup,
                                        text="nombre de coups: "
                                        + a
                                        + "/"
                                        + str(self.listeetoile[self.actifniveau][0]),
                                    )

                                self.changemult(-0.1, i)
                                l = i
                                self.listeaction.append(lambda: self.changemult(0.1, l))
                                self.canva.itemconfig(
                                    self.listebouton2[2 * i + 1], fill="red3"
                                )
                    t1 = time.time()
                self.update()
        else:
            décallage = (
                len(self.actifA) + 1
            ) * self.echelle // 2 - 5 * self.hauteur_fenetre / 100
            if (
                self.largeur + self.hauteur_fenetre / 10
                < event.y
                < self.largeur + 13 * self.hauteur_fenetre / 100
            ):
                for i in range(len(self.actifB)):
                    if (
                        3 * self.hauteur_fenetre / 200
                        + self.echelle * (len(self.actifA) + 1) * i
                        < event.x - décallage
                        < 9 * self.hauteur_fenetre / 200
                        + self.echelle * (len(self.actifA) + 1) * i
                    ):
                        self.coup += 1
                        a = str(self.coup)
                        while len(a) < 3:
                            a = "0" + a
                        if self.coup == self.listeetoile[self.actifniveau][0] + 1:
                            self.pause.itemconfig(
                                self.pauseetoile[2], image=self.etoilegrise
                            )
                        elif self.coup == self.listeetoile[self.actifniveau][1] + 1:
                            self.pause.itemconfig(
                                self.pauseetoile[1], image=self.etoilegrise
                            )
                        if self.coup > self.listeetoile[self.actifniveau][1]:
                            self.pause.itemconfig(
                                self.itemcoup, text="nombre de coups: " + a
                            )
                        elif self.coup > self.listeetoile[self.actifniveau][0]:
                            self.pause.itemconfig(
                                self.itemcoup,
                                text="nombre de coups: "
                                + a
                                + "/"
                                + str(self.listeetoile[self.actifniveau][1]),
                            )
                        else:
                            self.pause.itemconfig(
                                self.itemcoup,
                                text="nombre de coups: "
                                + a
                                + "/"
                                + str(self.listeetoile[self.actifniveau][0]),
                            )

                        self.changemult(0.1, i)
                        l = i
                        self.listeaction.append(lambda: self.changemult(-0.1, l))
                        self.canva.itemconfig(self.listebouton2[2 * i], fill="red3")
                        self.boutonactif = 1
                    elif (
                        11 * self.hauteur_fenetre / 200
                        + self.echelle * (len(self.actifA) + 1) * i
                        < event.x - décallage
                        < 17 * self.hauteur_fenetre / 200
                        + self.echelle * (len(self.actifA) + 1) * i
                    ):
                        self.coup += 1
                        a = str(self.coup)
                        while len(a) < 3:
                            a = "0" + a
                        if self.coup == self.listeetoile[self.actifniveau][0] + 1:
                            self.pause.itemconfig(
                                self.pauseetoile[2], image=self.etoilegrise
                            )
                        elif self.coup == self.listeetoile[self.actifniveau][1] + 1:
                            self.pause.itemconfig(
                                self.pauseetoile[1], image=self.etoilegrise
                            )
                        if self.coup > self.listeetoile[self.actifniveau][1]:
                            self.pause.itemconfig(
                                self.itemcoup, text="nombre de coups: " + a
                            )
                        elif self.coup > self.listeetoile[self.actifniveau][0]:
                            self.pause.itemconfig(
                                self.itemcoup,
                                text="nombre de coups: "
                                + a
                                + "/"
                                + str(self.listeetoile[self.actifniveau][1]),
                            )
                        else:
                            self.pause.itemconfig(
                                self.itemcoup,
                                text="nombre de coups: "
                                + a
                                + "/"
                                + str(self.listeetoile[self.actifniveau][0]),
                            )

                        self.changemult(-0.1, i)
                        l = i
                        self.listeaction.append(lambda: self.changemult(0.1, l))
                        self.canva.itemconfig(self.listebouton2[2 * i + 1], fill="red3")
                        self.boutonactif = 1
            elif (
                self.largeur + 14 * self.hauteur_fenetre / 100
                < event.y
                < self.largeur + 17 * self.hauteur_fenetre / 100
            ):
                for i in range(len(self.actifB)):
                    if (
                        3 * self.hauteur_fenetre / 200
                        + self.echelle * (len(self.actifA) + 1) * i
                        < event.x - décallage
                        < 9 * self.hauteur_fenetre / 200
                        + self.echelle * (len(self.actifA) + 1) * i
                    ):
                        self.echange(i - 1, i)
                        l = i
                        self.listeaction.append(lambda: self.echange(l - 1, l))
                        self.canva.itemconfig(self.listebouton3[2 * i], fill="red3")
                        self.boutonactif = 1
                    elif (
                        11 * self.hauteur_fenetre / 200
                        + self.echelle * (len(self.actifA) + 1) * i
                        < event.x - décallage
                        < 17 * self.hauteur_fenetre / 200
                        + self.echelle * (len(self.actifA) + 1) * i
                    ):
                        self.echange(i, (i + 1) % len(self.actifB))
                        self.canva.itemconfig(self.listebouton3[2 * i + 1], fill="red3")
                        self.boutonactif = 1
                        l = i
                        self.listeaction.append(
                            lambda: self.echange(l, (l + 1) % len(self.actifB))
                        )

            self.actifgauss = 0
            if (
                self.largeur + 6 * self.hauteur_fenetre / 100
                < event.y
                < self.largeur + 9 * self.hauteur_fenetre / 100
            ):
                for i in range(len(self.actifB)):
                    if (
                        7 * self.hauteur_fenetre / 200
                        + self.echelle * (len(self.actifA) + 1) * i
                        < event.x - décallage
                        < 13 * self.hauteur_fenetre / 200
                        + self.echelle * (len(self.actifA) + 1) * i
                    ):
                        self.coordclick = (
                            7 * self.hauteur_fenetre / 200
                            + self.echelle * (len(self.actifA) + 1) * i
                            - event.x
                            + décallage,
                            self.largeur + 6 * self.hauteur_fenetre / 100 - event.y,
                            13 * self.hauteur_fenetre / 200
                            + self.echelle * (len(self.actifA) + 1) * i
                            - event.x
                            + décallage,
                            self.largeur + 9 * self.hauteur_fenetre / 100 - event.y,
                        )

                        self.actifgauss = 1 + i
                        for j in range(len(self.gaussemplacement)):
                            if self.gaussemplacement[j] == self.actifgauss:
                                self.gaussemplacement[j] = 0
                        self.boutonactif = 1
            elif (
                7 * self.hauteur_fenetre / 200
                <= event.y
                <= 13 * self.hauteur_fenetre / 200
            ):
                if (
                    self.hauteur + 1 + len(self.actifA) + 4 * self.hauteur_fenetre / 100
                    < event.x
                    < self.hauteur
                    + 1
                    + len(self.actifA)
                    + 7 * self.hauteur_fenetre / 100
                ):
                    i = self.gaussemplacement[0]
                    self.gaussemplacement[0] = 0
                    if i != 0:
                        self.coordclick = (
                            self.canva.coords(self.listeovalgauss[i - 1][0])[0]
                            - event.x,
                            self.canva.coords(self.listeovalgauss[i - 1][0])[1]
                            - event.y,
                            self.canva.coords(self.listeovalgauss[i - 1][0])[2]
                            - event.x,
                            self.canva.coords(self.listeovalgauss[i - 1][0])[3]
                            - event.y,
                        )
                        self.actifgauss = i

                    self.boutonactif = 1
                elif (
                    self.hauteur
                    + 1
                    + len(self.actifA)
                    + 14 * self.hauteur_fenetre / 100
                    < event.x
                    < self.hauteur
                    + 1
                    + len(self.actifA)
                    + 17 * self.hauteur_fenetre / 100
                ):
                    i = self.gaussemplacement[1]
                    self.gaussemplacement[1] = 0
                    if i != 0:
                        self.coordclick = (
                            self.canva.coords(self.listeovalgauss[i - 1][0])[0]
                            - event.x,
                            self.canva.coords(self.listeovalgauss[i - 1][0])[1]
                            - event.y,
                            self.canva.coords(self.listeovalgauss[i - 1][0])[2]
                            - event.x,
                            self.canva.coords(self.listeovalgauss[i - 1][0])[3]
                            - event.y,
                        )
                        self.actifgauss = i

                    self.boutonactif = 1
            elif (
                47 * self.hauteur_fenetre / 200
                <= event.y
                <= 53 * self.hauteur_fenetre / 200
            ):
                if (
                    self.hauteur + 1 + len(self.actifA) + 4 * self.hauteur_fenetre / 100
                    < event.x
                    < self.hauteur
                    + 1
                    + len(self.actifA)
                    + 7 * self.hauteur_fenetre / 100
                ):
                    i = self.gaussemplacement[2]
                    self.gaussemplacement[2] = 0
                    if i != 0:
                        self.coordclick = (
                            self.canva.coords(self.listeovalgauss[i - 1][0])[0]
                            - event.x,
                            self.canva.coords(self.listeovalgauss[i - 1][0])[1]
                            - event.y,
                            self.canva.coords(self.listeovalgauss[i - 1][0])[2]
                            - event.x,
                            self.canva.coords(self.listeovalgauss[i - 1][0])[3]
                            - event.y,
                        )
                        self.actifgauss = i

                    self.boutonactif = 1
                if (
                    self.hauteur
                    + 1
                    + len(self.actifA)
                    + 14 * self.hauteur_fenetre / 100
                    < event.x
                    < self.hauteur
                    + 1
                    + len(self.actifA)
                    + 17 * self.hauteur_fenetre / 100
                ):
                    i = self.gaussemplacement[3]
                    self.gaussemplacement[3] = 0
                    if i != 0:
                        self.coordclick = (
                            self.canva.coords(self.listeovalgauss[i - 1][0])[0]
                            - event.x,
                            self.canva.coords(self.listeovalgauss[i - 1][0])[1]
                            - event.y,
                            self.canva.coords(self.listeovalgauss[i - 1][0])[2]
                            - event.x,
                            self.canva.coords(self.listeovalgauss[i - 1][0])[3]
                            - event.y,
                        )
                        self.actifgauss = i

                    self.boutonactif = 1
            if (
                self.hauteur + 1 + len(self.actifA) + 13 * self.hauteur_fenetre / 200
                < event.x
                < self.hauteur + 1 + len(self.actifA) + 129 * self.hauteur_fenetre / 200
            ):
                if (
                    8 * self.hauteur_fenetre / 100
                    < event.y
                    < 12 * self.hauteur_fenetre / 100
                ):
                    if self.gauss1actif == 1:
                        self.canva.itemconfig(self.gaussrectangle1, fill="red3")
                        self.gauss(
                            1,
                            self.gaussemplacement[0] - 1,
                            self.gaussemplacement[1] - 1,
                        )

                        A = self.gaussemplacement[0]
                        B = self.gaussemplacement[1]

                        self.listeaction.append(
                            lambda: self.gauss(
                                -1,
                                A - 1,
                                B - 1,
                            )
                        )

                if (
                    28 * self.hauteur_fenetre / 100
                    < event.y
                    < 32 * self.hauteur_fenetre / 100
                ):
                    if self.gauss2actif == 1:
                        self.canva.itemconfig(self.gaussrectangle2, fill="red3")
                        self.gauss(
                            -1,
                            self.gaussemplacement[2] - 1,
                            self.gaussemplacement[3] - 1,
                        )

                        A = self.gaussemplacement[2]
                        B = self.gaussemplacement[3]

                        self.listeaction.append(
                            lambda: self.gauss(
                                1,
                                A - 1,
                                B - 1,
                            )
                        )

            t1 = time.time()
            while self.boutonactif == 1:
                if time.time() - t1 > 0.2:
                    if (
                        self.largeur + self.hauteur_fenetre / 10
                        < event.y
                        < self.largeur + 13 * self.hauteur_fenetre / 100
                    ):
                        for i in range(len(self.actifB)):
                            if (
                                3 * self.hauteur_fenetre / 200
                                + self.echelle * (len(self.actifA) + 1) * i
                                < event.x - décallage
                                < 9 * self.hauteur_fenetre / 200
                                + self.echelle * (len(self.actifA) + 1) * i
                            ):
                                self.coup += 1
                                a = str(self.coup)
                                while len(a) < 3:
                                    a = "0" + a
                                if (
                                    self.coup
                                    == self.listeetoile[self.actifniveau][0] + 1
                                ):
                                    self.pause.itemconfig(
                                        self.pauseetoile[2], image=self.etoilegrise
                                    )
                                elif (
                                    self.coup
                                    == self.listeetoile[self.actifniveau][1] + 1
                                ):
                                    self.pause.itemconfig(
                                        self.pauseetoile[1], image=self.etoilegrise
                                    )
                                if self.coup > self.listeetoile[self.actifniveau][1]:
                                    self.pause.itemconfig(
                                        self.itemcoup, text="nombre de coups: " + a
                                    )
                                elif self.coup > self.listeetoile[self.actifniveau][0]:
                                    self.pause.itemconfig(
                                        self.itemcoup,
                                        text="nombre de coups: "
                                        + a
                                        + "/"
                                        + str(self.listeetoile[self.actifniveau][1]),
                                    )
                                else:
                                    self.pause.itemconfig(
                                        self.itemcoup,
                                        text="nombre de coups: "
                                        + a
                                        + "/"
                                        + str(self.listeetoile[self.actifniveau][0]),
                                    )

                                self.changemult(0.1, i)
                                l = i
                                self.listeaction.append(
                                    lambda: self.changemult(-0.1, l)
                                )
                                self.canva.itemconfig(
                                    self.listebouton2[2 * i], fill="red3"
                                )
                            elif (
                                11 * self.hauteur_fenetre / 200
                                + self.echelle * (len(self.actifA) + 1) * i
                                < event.x - décallage
                                < 17 * self.hauteur_fenetre / 200
                                + self.echelle * (len(self.actifA) + 1) * i
                            ):
                                self.coup += 1
                                a = str(self.coup)
                                while len(a) < 3:
                                    a = "0" + a
                                self.pause.itemconfig(
                                    self.itemcoup, text="nombre de coups: " + a
                                )
                                self.changemult(-0.1, i)
                                l = i
                                self.listeaction.append(lambda: self.changemult(0.1, l))
                                self.canva.itemconfig(
                                    self.listebouton2[2 * i + 1], fill="red3"
                                )
                    t1 = time.time()
                self.update()

    def click3(self, event):
        if (event.y - 9 * self.hauteur_fenetre / 200) ** 2 + (
            event.x - self.largeur_fenetre + 15 * self.hauteur_fenetre / 200
        ) ** 2 < (7 * self.hauteur_fenetre / 200) ** 2:
            self.unpack()
            self.blanc1[0].pack()
            self.continuer.pack()
            self.blanc2[0].pack()
            self.parametre.pack()
            self.blanc2[1].pack()
            self.menu.pack()

        if (event.y - 9 * self.hauteur_fenetre / 200) ** 2 + (
            event.x
            + self.hauteur_fenetre / 10
            - self.largeur_fenetre
            + 15 * self.hauteur_fenetre / 200
        ) ** 2 < (7 * self.hauteur_fenetre / 200) ** 2:
            self.recommence()

    def motion(self, event):
        if self.actifgauss != 0:
            x0, y0, x1, y1 = self.coordclick
            self.canva.coords(
                self.listeovalgauss[self.actifgauss - 1][0],
                event.x + x0,
                event.y + y0,
                event.x + x1,
                event.y + y1,
            )
            self.canva.coords(
                self.listeovalgauss[self.actifgauss - 1][1],
                event.x + (x0 + x1) // 2,
                event.y + (y0 + y1) // 2,
            )
            self.update()

    def declick2(self, event):
        self.boutonactif = 0
        for i in range(len(self.listebouton2)):
            self.canva.itemconfig(self.listebouton2[i], fill="red4")
            self.canva.itemconfig(self.listebouton3[i], fill="red4")
        if self.variable.get() == "x":
            if self.actifgauss != 0:
                if (
                    self.hauteur + 7 * self.hauteur_fenetre / 200
                    < event.y
                    < self.hauteur + 13 * self.hauteur_fenetre / 200
                ):
                    if (
                        4 * self.hauteur_fenetre / 100
                        < event.x
                        < 7 * self.hauteur_fenetre / 100
                    ):
                        if self.gaussemplacement[0] != 0:
                            self.canva.coords(
                                self.listeovalgauss[self.gaussemplacement[0] - 1][0],
                                self.largeur + 6 * self.hauteur_fenetre / 100,
                                -3 * self.hauteur_fenetre / 200
                                + (len(self.actifA) + 1) * self.echelle // 2
                                + (self.gaussemplacement[0] - 1)
                                * (len(self.actifA) + 1)
                                * self.echelle,
                                self.largeur + 9 * self.hauteur_fenetre / 100,
                                3 * self.hauteur_fenetre / 200
                                + (len(self.actifA) + 1) * self.echelle // 2
                                + (self.gaussemplacement[0] - 1)
                                * (len(self.actifA) + 1)
                                * self.echelle,
                            )

                            self.canva.coords(
                                self.listeovalgauss[self.gaussemplacement[0] - 1][1],
                                self.largeur + 3 * self.hauteur_fenetre / 40,
                                (len(self.actifA) + 1) * self.echelle // 2
                                + (self.gaussemplacement[0] - 1)
                                * (len(self.actifA) + 1)
                                * self.echelle,
                            )
                        self.canva.coords(
                            self.listeovalgauss[self.actifgauss - 1][0],
                            4 * self.hauteur_fenetre / 100,
                            self.hauteur + 7 * self.hauteur_fenetre / 200,
                            7 * self.hauteur_fenetre / 100,
                            self.hauteur + 13 * self.hauteur_fenetre / 200,
                        )
                        self.canva.coords(
                            self.listeovalgauss[self.actifgauss - 1][1],
                            11 * self.hauteur_fenetre / 200,
                            self.hauteur + self.hauteur_fenetre / 20,
                        )
                        self.gaussemplacement[0] = self.actifgauss
                    elif (
                        14 * self.hauteur_fenetre / 100
                        < event.x
                        < 17 * self.hauteur_fenetre / 100
                    ):
                        if self.gaussemplacement[1] != 0:
                            self.canva.coords(
                                self.listeovalgauss[self.gaussemplacement[1] - 1][0],
                                self.largeur + 6 * self.hauteur_fenetre / 100,
                                -3 * self.hauteur_fenetre / 200
                                + (len(self.actifA) + 1) * self.echelle // 2
                                + (self.gaussemplacement[1] - 1)
                                * (len(self.actifA) + 1)
                                * self.echelle,
                                self.largeur + 9 * self.hauteur_fenetre / 100,
                                3 * self.hauteur_fenetre / 200
                                + (len(self.actifA) + 1) * self.echelle // 2
                                + (self.gaussemplacement[1] - 1)
                                * (len(self.actifA) + 1)
                                * self.echelle,
                            )
                            self.canva.coords(
                                self.listeovalgauss[self.gaussemplacement[1] - 1][1],
                                self.largeur + 3 * self.hauteur_fenetre / 40,
                                (len(self.actifA) + 1) * self.echelle // 2
                                + (self.gaussemplacement[1] - 1)
                                * (len(self.actifA) + 1)
                                * self.echelle,
                            )
                        self.canva.coords(
                            self.listeovalgauss[self.actifgauss - 1][0],
                            14 * self.hauteur_fenetre / 100,
                            self.hauteur + 7 * self.hauteur_fenetre / 200,
                            17 * self.hauteur_fenetre / 100,
                            self.hauteur + 13 * self.hauteur_fenetre / 200,
                        )
                        self.canva.coords(
                            self.listeovalgauss[self.actifgauss - 1][1],
                            31 * self.hauteur_fenetre / 200,
                            self.hauteur + self.hauteur_fenetre / 20,
                        )
                        self.gaussemplacement[1] = self.actifgauss
                    elif (
                        54 * self.hauteur_fenetre / 100
                        < event.x
                        < 57 * self.hauteur_fenetre / 100
                    ):
                        if self.gaussemplacement[2] != 0:
                            self.canva.coords(
                                self.listeovalgauss[self.gaussemplacement[2] - 1][0],
                                self.largeur + 6 * self.hauteur_fenetre / 100,
                                -3 * self.hauteur_fenetre / 200
                                + (len(self.actifA) + 1) * self.echelle // 2
                                + (self.gaussemplacement[2] - 1)
                                * (len(self.actifA) + 1)
                                * self.echelle,
                                self.largeur + 9 * self.hauteur_fenetre / 100,
                                3 * self.hauteur_fenetre / 200
                                + (len(self.actifA) + 1) * self.echelle // 2
                                + (self.gaussemplacement[2] - 1)
                                * (len(self.actifA) + 1)
                                * self.echelle,
                            )
                            self.canva.coords(
                                self.listeovalgauss[self.gaussemplacement[2] - 1][1],
                                self.largeur + 3 * self.hauteur_fenetre / 40,
                                (len(self.actifA) + 1) * self.echelle // 2
                                + (self.gaussemplacement[2] - 1)
                                * (len(self.actifA) + 1)
                                * self.echelle,
                            )
                        self.canva.coords(
                            self.listeovalgauss[self.actifgauss - 1][0],
                            54 * self.hauteur_fenetre / 100,
                            self.hauteur + 7 * self.hauteur_fenetre / 200,
                            57 * self.hauteur_fenetre / 100,
                            self.hauteur + 13 * self.hauteur_fenetre / 200,
                        )
                        self.canva.coords(
                            self.listeovalgauss[self.actifgauss - 1][1],
                            111 * self.hauteur_fenetre / 200,
                            self.hauteur + 5 * self.hauteur_fenetre / 100,
                        )
                        self.gaussemplacement[2] = self.actifgauss
                    elif (
                        64 * self.hauteur_fenetre / 100
                        < event.x
                        < 67 * self.hauteur_fenetre / 100
                    ):
                        if self.gaussemplacement[3] != 0:
                            self.canva.coords(
                                self.listeovalgauss[self.gaussemplacement[3] - 1][0],
                                self.largeur + 6 * self.hauteur_fenetre / 100,
                                -3 * self.hauteur_fenetre / 200
                                + (len(self.actifA) + 1) * self.echelle // 2
                                + (self.gaussemplacement[3] - 1)
                                * (len(self.actifA) + 1)
                                * self.echelle,
                                self.largeur + 9 * self.hauteur_fenetre / 100,
                                3 * self.hauteur_fenetre / 200
                                + (len(self.actifA) + 1) * self.echelle // 2
                                + (self.gaussemplacement[3] - 1)
                                * (len(self.actifA) + 1)
                                * self.echelle,
                            )
                            self.canva.coords(
                                self.listeovalgauss[self.gaussemplacement[3] - 1][1],
                                self.largeur + 3 * self.hauteur_fenetre / 40,
                                (len(self.actifA) + 1) * self.echelle // 2
                                + (self.gaussemplacement[3] - 1)
                                * (len(self.actifA) + 1)
                                * self.echelle,
                            )
                        self.canva.coords(
                            self.listeovalgauss[self.actifgauss - 1][0],
                            64 * self.hauteur_fenetre / 100,
                            self.hauteur + 7 * self.hauteur_fenetre / 200,
                            67 * self.hauteur_fenetre / 100,
                            self.hauteur + 13 * self.hauteur_fenetre / 200,
                        )
                        self.canva.coords(
                            self.listeovalgauss[self.actifgauss - 1][1],
                            131 * self.hauteur_fenetre / 200,
                            self.hauteur + self.hauteur_fenetre / 20,
                        )

                        self.gaussemplacement[3] = self.actifgauss
                    else:
                        self.canva.coords(
                            self.listeovalgauss[self.actifgauss - 1][0],
                            self.largeur + 6 * self.hauteur_fenetre / 100,
                            -3 * self.hauteur_fenetre / 200
                            + (len(self.actifA) + 1) * self.echelle // 2
                            + (self.actifgauss - 1)
                            * (len(self.actifA) + 1)
                            * self.echelle,
                            self.largeur + 9 * self.hauteur_fenetre / 100,
                            3 * self.hauteur_fenetre / 200
                            + (len(self.actifA) + 1) * self.echelle // 2
                            + (self.actifgauss - 1)
                            * (len(self.actifA) + 1)
                            * self.echelle,
                        )
                        self.canva.coords(
                            self.listeovalgauss[self.actifgauss - 1][1],
                            self.largeur + 3 * self.hauteur_fenetre / 40,
                            (len(self.actifA) + 1) * self.echelle // 2
                            + (self.actifgauss - 1)
                            * (len(self.actifA) + 1)
                            * self.echelle,
                        )

                else:
                    self.canva.coords(
                        self.listeovalgauss[self.actifgauss - 1][0],
                        self.largeur + 6 * self.hauteur_fenetre / 100,
                        -3 * self.hauteur_fenetre / 200
                        + (len(self.actifA) + 1) * self.echelle // 2
                        + (self.actifgauss - 1) * (len(self.actifA) + 1) * self.echelle,
                        self.largeur + 9 * self.hauteur_fenetre / 100,
                        3 * self.hauteur_fenetre / 200
                        + (len(self.actifA) + 1) * self.echelle // 2
                        + (self.actifgauss - 1) * (len(self.actifA) + 1) * self.echelle,
                    )
                    self.canva.coords(
                        self.listeovalgauss[self.actifgauss - 1][1],
                        self.largeur + 3 * self.hauteur_fenetre / 40,
                        (len(self.actifA) + 1) * self.echelle // 2
                        + (self.actifgauss - 1) * (len(self.actifA) + 1) * self.echelle,
                    )
        else:
            if self.actifgauss != 0:
                if (
                    7 * self.hauteur_fenetre / 200
                    < event.y
                    < 13 * self.hauteur_fenetre / 200
                ):
                    if (
                        self.hauteur
                        + 1
                        + len(self.actifA)
                        + 4 * self.hauteur_fenetre / 100
                        < event.x
                        < self.hauteur
                        + 1
                        + len(self.actifA)
                        + 7 * self.hauteur_fenetre / 100
                    ):
                        if self.gaussemplacement[0] != 0:
                            self.canva.coords(
                                self.listeovalgauss[self.gaussemplacement[0] - 1][0],
                                -3 * self.hauteur_fenetre / 200
                                + (len(self.actifA) + 1) * self.echelle / 2
                                + (self.gaussemplacement[0] - 1)
                                * (len(self.actifA) + 1)
                                * self.echelle,
                                self.largeur + 6 * self.hauteur_fenetre / 100,
                                3 * self.hauteur_fenetre / 200
                                + (len(self.actifA) + 1) * self.echelle / 2
                                + (self.gaussemplacement[0] - 1)
                                * (len(self.actifA) + 1)
                                * self.echelle,
                                self.largeur + 9 * self.hauteur_fenetre / 100,
                            )
                            self.canva.coords(
                                self.listeovalgauss[self.gaussemplacement[0] - 1][1],
                                (len(self.actifA) + 1) * self.echelle // 2
                                + (self.gaussemplacement[0] - 1)
                                * (len(self.actifA) + 1)
                                * self.echelle,
                                self.largeur + 3 * self.hauteur_fenetre / 40,
                            )
                        self.canva.coords(
                            self.listeovalgauss[self.actifgauss - 1][0],
                            self.hauteur
                            + 1
                            + len(self.actifA)
                            + 4 * self.hauteur_fenetre / 100,
                            7 * self.hauteur_fenetre / 200,
                            self.hauteur
                            + 1
                            + len(self.actifA)
                            + 7 * self.hauteur_fenetre / 100,
                            13 * self.hauteur_fenetre / 200,
                        )
                        self.canva.coords(
                            self.listeovalgauss[self.actifgauss - 1][1],
                            self.hauteur
                            + 1
                            + len(self.actifA)
                            + 11 * self.hauteur_fenetre / 200,
                            5 * self.hauteur_fenetre / 100,
                        )
                        self.gaussemplacement[0] = self.actifgauss
                    elif (
                        self.hauteur
                        + 1
                        + len(self.actifA)
                        + 14 * self.hauteur_fenetre / 100
                        < event.x
                        < self.hauteur
                        + 1
                        + len(self.actifA)
                        + 17 * self.hauteur_fenetre / 100
                    ):
                        if self.gaussemplacement[1] != 0:
                            self.canva.coords(
                                self.listeovalgauss[self.gaussemplacement[1] - 1][0],
                                -3 * self.hauteur_fenetre / 200
                                + (len(self.actifA) + 1) * self.echelle // 2
                                + (self.gaussemplacement[1] - 1)
                                * (len(self.actifA) + 1)
                                * self.echelle,
                                self.largeur + 6 * self.hauteur_fenetre / 100,
                                3 * self.hauteur_fenetre / 200
                                + (len(self.actifA) + 1) * self.echelle // 2
                                + (self.gaussemplacement[1] - 1)
                                * (len(self.actifA) + 1)
                                * self.echelle,
                                self.largeur + 9 * self.hauteur_fenetre / 100,
                            )
                            self.canva.coords(
                                self.listeovalgauss[self.gaussemplacement[1] - 1][1],
                                (len(self.actifA) + 1) * self.echelle // 2
                                + (self.gaussemplacement[1] - 1)
                                * (len(self.actifA) + 1)
                                * self.echelle,
                                self.largeur + 3 * self.hauteur_fenetre / 40,
                            )
                        self.canva.coords(
                            self.listeovalgauss[self.actifgauss - 1][0],
                            self.hauteur
                            + 1
                            + len(self.actifA)
                            + 14 * self.hauteur_fenetre / 100,
                            7 * self.hauteur_fenetre / 200,
                            self.hauteur
                            + 1
                            + len(self.actifA)
                            + 17 * self.hauteur_fenetre / 100,
                            13 * self.hauteur_fenetre / 200,
                        )
                        self.canva.coords(
                            self.listeovalgauss[self.actifgauss - 1][1],
                            self.hauteur
                            + 1
                            + len(self.actifA)
                            + 31 * self.hauteur_fenetre / 200,
                            5 * self.hauteur_fenetre / 100,
                        )
                        self.gaussemplacement[1] = self.actifgauss
                    else:
                        self.canva.coords(
                            self.listeovalgauss[self.actifgauss - 1][0],
                            -3 * self.hauteur_fenetre / 200
                            + (len(self.actifA) + 1) * self.echelle // 2
                            + (self.actifgauss - 1)
                            * (len(self.actifA) + 1)
                            * self.echelle,
                            self.largeur + 6 * self.hauteur_fenetre / 100,
                            3 * self.hauteur_fenetre / 200
                            + (len(self.actifA) + 1) * self.echelle // 2
                            + (self.actifgauss - 1)
                            * (len(self.actifA) + 1)
                            * self.echelle,
                            self.largeur + 9 * self.hauteur_fenetre / 100,
                        )
                        self.canva.coords(
                            self.listeovalgauss[self.actifgauss - 1][1],
                            (len(self.actifA) + 1) * self.echelle // 2
                            + (self.actifgauss - 1)
                            * (len(self.actifA) + 1)
                            * self.echelle,
                            self.largeur + 3 * self.hauteur_fenetre / 40,
                        )
                elif (
                    47 * self.hauteur_fenetre / 200
                    < event.y
                    < 53 * self.hauteur_fenetre / 200
                ):
                    if (
                        self.hauteur
                        + 1
                        + len(self.actifA)
                        + 4 * self.hauteur_fenetre / 100
                        < event.x
                        < self.hauteur
                        + 1
                        + len(self.actifA)
                        + 7 * self.hauteur_fenetre / 100
                    ):
                        if self.gaussemplacement[2] != 0:
                            self.canva.coords(
                                self.listeovalgauss[self.gaussemplacement[2] - 1][0],
                                -3 * self.hauteur_fenetre / 200
                                + (len(self.actifA) + 1) * self.echelle // 2
                                + (self.gaussemplacement[2] - 1)
                                * (len(self.actifA) + 1)
                                * self.echelle,
                                self.largeur + 6 * self.hauteur_fenetre / 100,
                                3 * self.hauteur_fenetre / 200
                                + (len(self.actifA) + 1) * self.echelle // 2
                                + (self.gaussemplacement[2] - 1)
                                * (len(self.actifA) + 1)
                                * self.echelle,
                                self.largeur + 9 * self.hauteur_fenetre / 100,
                            )
                            self.canva.coords(
                                self.listeovalgauss[self.gaussemplacement[2] - 1][1],
                                (len(self.actifA) + 1) * self.echelle // 2
                                + (self.gaussemplacement[2] - 1)
                                * (len(self.actifA) + 1)
                                * self.echelle,
                                self.largeur + 3 * self.hauteur_fenetre / 40,
                            )
                        self.canva.coords(
                            self.listeovalgauss[self.actifgauss - 1][0],
                            self.hauteur
                            + 1
                            + len(self.actifA)
                            + 4 * self.hauteur_fenetre / 100,
                            47 * self.hauteur_fenetre / 200,
                            self.hauteur
                            + 1
                            + len(self.actifA)
                            + 7 * self.hauteur_fenetre / 100,
                            53 * self.hauteur_fenetre / 200,
                        )
                        self.canva.coords(
                            self.listeovalgauss[self.actifgauss - 1][1],
                            self.hauteur
                            + 1
                            + len(self.actifA)
                            + 11 * self.hauteur_fenetre / 200,
                            self.hauteur_fenetre / 4,
                        )
                        self.gaussemplacement[2] = self.actifgauss
                    elif (
                        self.hauteur
                        + 1
                        + len(self.actifA)
                        + 14 * self.hauteur_fenetre / 100
                        < event.x
                        < self.hauteur
                        + 1
                        + len(self.actifA)
                        + 17 * self.hauteur_fenetre / 100
                    ):
                        if self.gaussemplacement[3] != 0:
                            self.canva.coords(
                                self.listeovalgauss[self.gaussemplacement[3] - 1][0],
                                -3 * self.hauteur_fenetre / 200
                                + (len(self.actifA) + 1) * self.echelle // 2
                                + (self.gaussemplacement[3] - 1)
                                * (len(self.actifA) + 1)
                                * self.echelle,
                                self.largeur + 6 * self.hauteur_fenetre / 100,
                                3 * self.hauteur_fenetre / 200
                                + (len(self.actifA) + 1) * self.echelle // 2
                                + (self.gaussemplacement[3] - 1)
                                * (len(self.actifA) + 1)
                                * self.echelle,
                                self.largeur + 9 * self.hauteur_fenetre / 100,
                            )
                            self.canva.coords(
                                self.listeovalgauss[self.gaussemplacement[3] - 1][1],
                                (len(self.actifA) + 1) * self.echelle // 2
                                + (self.gaussemplacement[3] - 1)
                                * (len(self.actifA) + 1)
                                * self.echelle,
                                self.largeur + 3 * self.hauteur_fenetre / 40,
                            )
                        self.canva.coords(
                            self.listeovalgauss[self.actifgauss - 1][0],
                            self.hauteur
                            + 1
                            + len(self.actifA)
                            + 14 * self.hauteur_fenetre / 100,
                            47 * self.hauteur_fenetre / 200,
                            self.hauteur
                            + 1
                            + len(self.actifA)
                            + 17 * self.hauteur_fenetre / 100,
                            53 * self.hauteur_fenetre / 200,
                        )
                        self.canva.coords(
                            self.listeovalgauss[self.actifgauss - 1][1],
                            self.hauteur
                            + 1
                            + len(self.actifA)
                            + 31 * self.hauteur_fenetre / 200,
                            self.hauteur_fenetre / 4,
                        )

                        self.gaussemplacement[3] = self.actifgauss
                    else:
                        self.canva.coords(
                            self.listeovalgauss[self.actifgauss - 1][0],
                            -3 * self.hauteur_fenetre / 200
                            + (len(self.actifA) + 1) * self.echelle // 2
                            + (self.actifgauss - 1)
                            * (len(self.actifA) + 1)
                            * self.echelle,
                            self.largeur + 6 * self.hauteur_fenetre / 100,
                            3 * self.hauteur_fenetre / 200
                            + (len(self.actifA) + 1) * self.echelle // 2
                            + (self.actifgauss - 1)
                            * (len(self.actifA) + 1)
                            * self.echelle,
                            self.largeur + 9 * self.hauteur_fenetre / 100,
                        )
                        self.canva.coords(
                            self.listeovalgauss[self.actifgauss - 1][1],
                            (len(self.actifA) + 1) * self.echelle // 2
                            + (self.actifgauss - 1)
                            * (len(self.actifA) + 1)
                            * self.echelle,
                            self.largeur + 3 * self.hauteur_fenetre / 40,
                        )

                else:
                    self.canva.coords(
                        self.listeovalgauss[self.actifgauss - 1][0],
                        -3 * self.hauteur_fenetre / 200
                        + (len(self.actifA) + 1) * self.echelle // 2
                        + (self.actifgauss - 1) * (len(self.actifA) + 1) * self.echelle,
                        self.largeur + 6 * self.hauteur_fenetre / 100,
                        3 * self.hauteur_fenetre / 200
                        + (len(self.actifA) + 1) * self.echelle // 2
                        + (self.actifgauss - 1) * (len(self.actifA) + 1) * self.echelle,
                        self.largeur + 9 * self.hauteur_fenetre / 100,
                    )
                    self.canva.coords(
                        self.listeovalgauss[self.actifgauss - 1][1],
                        (len(self.actifA) + 1) * self.echelle // 2
                        + (self.actifgauss - 1) * (len(self.actifA) + 1) * self.echelle,
                        self.largeur + 3 * self.hauteur_fenetre / 40,
                    )
        if self.gaussemplacement[0] != 0 and self.gaussemplacement[1] != 0:
            self.canva.itemconfig(self.gaussrectangle1, fill="red4")
            self.gauss1actif = 1
        else:
            self.canva.itemconfig(self.gaussrectangle1, fill="grey42")
            self.gauss1actif = 0

        if self.gaussemplacement[2] != 0 and self.gaussemplacement[3] != 0:
            self.canva.itemconfig(self.gaussrectangle2, fill="red4")
            self.gauss2actif = 1
        else:
            self.canva.itemconfig(self.gaussrectangle2, fill="grey42")
            self.gauss2actif = 0

    def declick(self, event):
        self.boutonactif = 0
        for i in range(len(self.listebouton)):
            self.bouton.itemconfig(self.listebouton[i][0], fill=self.couleurs[i])
            self.bouton.itemconfig(self.listebouton[i][1], fill=self.couleurs[i])
        if self.nonsolution is not None:
            self.bouton.itemconfig(self.nonsolution, fill="white")
        self.bouton.itemconfig(self.boutonretour, fill="white")

    def clickniveau(self, event):
        for i in range(2):
            for j in range(8):
                if (
                    3 * self.hauteur_fenetre / 100 + 2 * self.hauteur_fenetre / 10 * j
                    < event.x
                    < 17 * self.hauteur_fenetre / 100
                    + 2 * self.hauteur_fenetre / 10 * j
                    and 12 * self.hauteur_fenetre / 100
                    + 12 * self.hauteur_fenetre / 100 * i
                    < event.y
                    < 2 * self.hauteur_fenetre / 10
                    + 12 * self.hauteur_fenetre / 100 * i
                ):
                    if self.niveauvalidé[i * 8 + j] == True:
                        self.niveaucanva.itemconfig(
                            self.listeniveau[i * 8 + j][0], fill="palegreen1"
                        )
                        self.actifniveauselect = i * 8 + j
                    elif self.niveauvalidé[i * 8 + j - 1] == True or i * 8 + j == 0:
                        self.niveaucanva.itemconfig(
                            self.listeniveau[i * 8 + j][0], fill="lightskyblue1"
                        )
                        self.actifniveauselect = i * 8 + j
        for i in range(2, 5):
            for j in range(8):
                if (
                    3 * self.hauteur_fenetre / 100 + 2 * self.hauteur_fenetre / 10 * j
                    < event.x
                    < 17 * self.hauteur_fenetre / 100
                    + 2 * self.hauteur_fenetre / 10 * j
                    and 22 * self.hauteur_fenetre / 100
                    + 12 * self.hauteur_fenetre / 100 * i
                    < event.y
                    < 3 * self.hauteur_fenetre / 10
                    + 12 * self.hauteur_fenetre / 100 * i
                ):
                    if self.niveauvalidé[i * 8 + j] == True:
                        self.niveaucanva.itemconfig(
                            self.listeniveau[i * 8 + j][0], fill="palegreen1"
                        )
                        self.actifniveauselect = i * 8 + j
                    elif self.niveauvalidé[i * 8 + j - 1] == True or i * 8 + j == 0:
                        self.niveaucanva.itemconfig(
                            self.listeniveau[i * 8 + j][0], fill="lightskyblue1"
                        )
                        self.actifniveauselect = i * 8 + j

    def recommence(self):
        self.changesysteme("Usopp est un gros blaireau")

    def retour(self):
        if len(self.listeaction):
            self.listeaction[-1]()
            self.listeaction.pop()

    def declickniveau(self, event):
        if self.actifniveauselect != None:
            i = self.actifniveauselect // 8
            j = self.actifniveauselect % 8
            if self.niveauvalidé[i * 8 + j] == True:
                self.niveaucanva.itemconfig(
                    self.listeniveau[i * 8 + j][0], fill="light green"
                )
                self.actifniveauselect = i * 8 + j
            else:
                self.niveaucanva.itemconfig(
                    self.listeniveau[i * 8 + j][0], fill="lightskyblue2"
                )
                self.actifniveauselect = i * 8 + j
            if i < 2:
                if (
                    3 * self.hauteur_fenetre / 100 + 2 * self.hauteur_fenetre / 10 * j
                    < event.x
                    < 17 * self.hauteur_fenetre / 100
                    + 2 * self.hauteur_fenetre / 10 * j
                    and 12 * self.hauteur_fenetre / 100
                    + 12 * self.hauteur_fenetre / 100 * i
                    < event.y
                    < 2 * self.hauteur_fenetre / 10
                    + 12 * self.hauteur_fenetre / 100 * i
                ):
                    self.menu.pack_forget()
                    self.niveaucanva.pack_forget()
                    self.systeme.set("niveau 0" + str(self.actifniveauselect + 1))
                    self.actifniveau = self.actifniveauselect
                    self.changesysteme("01")
                    self.pack()
            else:
                if (
                    3 * self.hauteur_fenetre / 100 + 2 * self.hauteur_fenetre / 10 * j
                    < event.x
                    < 17 * self.hauteur_fenetre / 100
                    + 2 * self.hauteur_fenetre / 10 * j
                    and 22 * self.hauteur_fenetre / 100
                    + 12 * self.hauteur_fenetre / 100 * i
                    < event.y
                    < 3 * self.hauteur_fenetre / 10
                    + 12 * self.hauteur_fenetre / 100 * i
                ):
                    self.menu.pack_forget()
                    self.niveaucanva.pack_forget()
                    self.systeme.set("niveau 0" + str(self.actifniveauselect + 1))
                    self.actifniveau = self.actifniveauselect
                    self.changesysteme("01")
                    self.pack()

    def gagné(self):
        self.stop = False
        self.gagne.place_forget()
        self.niveauvalidé[self.actifniveau] = True
        fichier = open("projet tortuga/usopp.txt", "r")
        info = fichier.readlines()[0]
        fichier.close()
        ancienresultat = int(info[self.actifniveau])
        self.niveaucanva.itemconfig(
            self.listeniveau[self.actifniveau][2], image=self.etoilejaune2
        )
        self.niveaucanva.itemconfig(
            self.listeniveau[self.actifniveau][3], image=self.etoilejaune2
        )
        self.niveaucanva.itemconfig(
            self.listeniveau[self.actifniveau][4], image=self.etoilejaune2
        )
        self.remarque.config(self.listetext[self.actifniveau])
        self.remarque.pack()
        info = info[: self.actifniveau] + "3" + info[self.actifniveau + 1 :]
        self.comptediamant += 3 - ancienresultat
        if self.coup > self.listeetoile[self.actifniveau][0]:
            self.etoile.itemconfig(self.etoile3, fill="light grey")
            self.comptediamant -= 1
            if ancienresultat < 2:
                self.niveaucanva.itemconfig(
                    self.listeniveau[self.actifniveau][4], image=self.etoilegrise2
                )
                info = info[: self.actifniveau] + "2" + info[self.actifniveau + 1 :]
            else:
                self.comptediamant += 1
        if self.coup > self.listeetoile[self.actifniveau][1]:
            self.etoile.itemconfig(self.etoile2, fill="light grey")
            self.comptediamant -= 1
            if ancienresultat < 1:
                self.niveaucanva.itemconfig(
                    self.listeniveau[self.actifniveau][3], image=self.etoilegrise2
                )
                info = info[: self.actifniveau] + "1" + info[self.actifniveau + 1 :]
            else:
                self.comptediamant += 1
        fichier = open("projet tortuga/usopp.txt", "w")
        self.diamant.itemconfig(self.nombrediamant, text=str(self.comptediamant))

        self.etoile.create_text(
            3 * self.hauteur_fenetre / 10,
            15 * self.hauteur_fenetre / 100,
            anchor="n",
            text="nombre de coups: " + str(self.coup),
            font="Helvetica " + str(int(3 * self.hauteur_fenetre / 100)) + " normal",
            fill="black",
        )
        if self.actifniveau == 6:
            self.anciennecombine = (
                str(int(self.actifX[0]))
                + str(int(self.actifX[0] % 1 * 10))
                + str(int(self.actifX[1]))
                + str(int(self.actifX[1] % 1 * 10))
            )
        fichier.write(
            info
            + str(self.pouvoirunlock)
            + "\n"
            + str(self.emojie)
            + self.skindebloque
            + str(self.nourriture)
            + self.nourrituredebloque
            + self.anciennecombine
        )
        fichier.close()
        self.niveaucanva.itemconfig(
            self.listeniveau[self.actifniveau][0], fill="light green"
        )
        if self.actifniveau < 39:
            if not self.niveauvalidé[self.actifniveau + 1]:
                self.niveaucanva.itemconfig(
                    self.listeniveau[self.actifniveau + 1][0], fill="lightskyblue2"
                )
        t1 = time.time()
        t2 = time.time()
        while t2 - t1 < 1:
            self.update()
            t2 = time.time()
        self.gagne.place(
            x=self.largeur_fenetre / 2, y=self.hauteur_fenetre / 3, anchor="c"
        )
        for k in range(len(self.actifA)):
            self.gifcheck[k] = False
        self.frames0 = [0 for k in range(len(self.actifA))]
        self.systeme.set("niveau 0" + str(self.actifniveau + 2))

    def updategif(self, k, code, canva=1):
        if self.gifcheck[k] and self.codegif[k] == code and canva == 1:
            try:
                if self.frames0[k] <= len(self.frames1[self.emojie]):
                    self.frames1[self.emojie].append(
                        ImageTk.PhotoImage(
                            self.frames[self.emojie][
                                self.frames0[k] % len(self.frames[self.emojie])
                            ].resize(
                                (
                                    int(
                                        (self.echelle + 1)
                                        * (
                                            len(self.actifA)
                                            * (3 / (4 * len(self.actifA)))
                                        )
                                        + 1
                                    ),
                                    int(
                                        (self.echellex + 1) * (len(self.actifA) * 3 / 4)
                                        + 1
                                    ),
                                )
                            )
                        )
                    )
                x, y = self.canva.coords(self.listeboule[k][1])
                self.canva.delete(self.listeboule[k][1])
                self.listeboule[k][1] = self.canva.create_image(
                    x,
                    y,
                    anchor=tk.NW,
                    image=self.frames1[self.emojie][
                        self.frames0[k] % len(self.frames[self.emojie])
                    ],
                )
                self.frames0[k] += 1
                if self.variable.get() == "x":
                    self.canva.create_rectangle(
                        self.largeur + 1,
                        1,
                        self.largeur + 5 * self.hauteur_fenetre / 100 + 2,
                        self.hauteur + 1,
                        fill="white",
                        width=0,
                    )
                else:
                    self.canva.create_rectangle(
                        1,
                        self.largeur + 1,
                        self.hauteur + 1,
                        self.largeur + 5 * self.hauteur_fenetre / 100 + 2,
                        fill="white",
                        width=0,
                    )
                self.after(
                    int(self.delay[self.emojie]), lambda: self.updategif(k, code)
                )
            except IndexError:
                pass

        elif self.gifcheck2[k] and self.codegif2[k] == code and canva == 2:
            try:
                if self.frames02[k] <= len(self.frames12[self.emojie]):
                    self.frames12[self.emojie].append(
                        ImageTk.PhotoImage(
                            self.frames[self.emojie][
                                self.frames02[k] % len(self.frames[self.emojie])
                            ].resize(
                                (
                                    int(
                                        (self.echelle + 1)
                                        * (
                                            len(self.actifA)
                                            * (3 / (4 * len(self.actifA)))
                                        )
                                        + 1
                                    ),
                                    int(
                                        (self.echellex + 1) * (len(self.actifA) * 3 / 4)
                                        + 1
                                    ),
                                )
                            )
                        )
                    )
                x, y = self.canva2.coords(self.listeboule2[k][1])
                self.canva2.delete(self.listeboule2[k][1])
                self.listeboule2[k][1] = self.canva2.create_image(
                    x,
                    y,
                    anchor=tk.NW,
                    image=self.frames12[self.emojie][
                        self.frames02[k] % len(self.frames[self.emojie])
                    ],
                )
                self.frames02[k] += 1
                if self.variable.get() == "x":
                    self.canva2.create_rectangle(
                        self.largeur + 1,
                        1,
                        self.largeur + 5 * self.hauteur_fenetre / 100 + 2,
                        self.hauteur + 1,
                        fill="white",
                        width=0,
                    )
                else:
                    self.canva2.create_rectangle(
                        1,
                        self.largeur + 1,
                        self.hauteur + 1,
                        self.largeur + 5 * self.hauteur_fenetre / 100 + 2,
                        fill="white",
                        width=0,
                    )
                self.after(
                    int(self.delay[self.emojie]), lambda: self.updategif(k, code, 2)
                )
            except IndexError:
                pass

    def pack(self):
        self.preparecanva()
        self.preparebouton()
        self.pause.pack()
        self.zonejeu.pack()

        self.canva.pack(side="left")
        if (
            self.actifniveau == 11
            or self.actifniveau == 12
            or self.actifniveau == 13
            or self.actifniveau == 14
        ):
            self.preparecanva2()
            self.canva2.pack(side="right")
            self.blanc4.pack()
        else:
            self.canva2.delete("all")
        self.bouton.pack()

    def unpack(self):
        self.pause.pack_forget()
        self.zonejeu.pack_forget()
        self.bouton.pack_forget()
        self.canva2.pack_forget()
        self.blanc4.pack_forget()


fenetre = Tortugauss(ListeA, ListeB, listeetoile)

"Merci."

"""bug à regler:
- bug du reesayer
- bug du multiplicatif
-bug du petage de cable de la tortue
"""
