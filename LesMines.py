
# Modification date: Sun Dec 12 17:39:40 2021

# Production date: Sun Sep  3 15:42:51 2023

import random

class Mine:
    def __init__(self, nom, coordonnées, signe = "#", fake_coordonnées = [], vrai_signe = "*"):
        self.nom = nom
        self.vrai_coordonnées = coordonnées
        self.signe = signe
        self.vrai_signe = vrai_signe
        le_fake_nombre = random.randint(0, 2)
        if le_fake_nombre == 0:
            le_fake_nombre = -1
        else:
            le_fake_nombre = 1

        self.coordonnées = [int(self.vrai_coordonnées[0]) + le_fake_nombre, int(coordonnées[1])]

    
    def joueur_mis_son_pied(self, other):
        if self.coordonnées == other.coordonnées:
            return True
        else:
            return False

class Robot:
    def __init__(self, nom, coordonnées, signe, direction = None):
        """
        Cette function crée une objet "Robot" avec nom comme string, coordonnées comme un liste avec x et y qui sont integers (x, y), et direction comme "droite", "gauche", "haut" ou "bas".
        """
        self.signe = signe
        self.coordonnées = coordonnées
        self.direction = direction
        self.nom = nom

    #avancer
    def avancer(self):
        if self.direction == "6":
            self.coordonnées[0] += 1
            #print("Le Robot" , "\"" + self.nom + "\":" , "a avancé vers la droite!", "\nRobot ", "\"" + self.nom + "\":", self.coordonnées, self.direction)
        elif self.direction == "4":
            self.coordonnées[0] -= 1
            #print("Le Robot" , "\"" + self.nom + "\":" , "a avancé vers la gauche!", "\nRobot ", "\"" + self.nom + "\":", self.coordonnées, self.direction)
        elif self.direction == "8":
            self.coordonnées[1] -= 1
            #print("Le Robot" , "\"" + self.nom + "\":" , "a avancé vers le haut!", "\nRobot ", "\"" + self.nom + "\":", self.coordonnées, self.direction)
        elif self.direction == "5":
            self.coordonnées[1] += 1
            #print("Le Robot" , "\"" + self.nom + "\":" , "a avancé vers le bas!", "\nRobot ", "\"" + self.nom + "\":", self.coordonnées, self.direction)
    
    #reculer
    def reculer(self):
        if self.direction == "6":
            self.coordonnées[0] -= 1
            #print("Le Robot" , "\"" + self.nom + "\":" , "a avancé vers la droite!", "\nRobot ", "\"" + self.nom + "\":", self.coordonnées, self.direction)
        elif self.direction == "4":
            self.coordonnées[0] += 1
            #print("Le Robot" , "\"" + self.nom + "\":" , "a avancé vers la gauche!", "\nRobot ", "\"" + self.nom + "\":", self.coordonnées, self.direction)
        elif self.direction == "8":
            self.coordonnées[1] += 1
            #print("Le Robot" , "\"" + self.nom + "\":" , "a avancé vers le haut!", "\nRobot ", "\"" + self.nom + "\":", self.coordonnées, self.direction)
        elif self.direction == "5":
            self.coordonnées[1] -= 1
            #print("Le Robot" , "\"" + self.nom + "\":" , "a avancé vers le bas!", "\nRobot ", "\"" + self.nom + "\":", self.coordonnées, self.direction)
    


Scout = Robot("Scout", [0, 0], "S", "droite")



import os

clear = lambda: os.system('clear')

carte = []

hauteur = int(input("hauteur de la carte: "))
longueur = int(input("longueur de la carte: "))

clear()


robots = [Scout]

for i in range(hauteur):
    for j in range(longueur//4):
        nombre_au_hazard = random.randint(1, longueur-4)
        robots.append(Mine("Mine" + str(i), [nombre_au_hazard, i]))
    

"""
for i in range(len(robots)):
    print(robots[i].nom, robots[i].coordonnées, robots[i].signe, robots[i].direction)
"""

for l in range(hauteur):
    carte.append([])
    for h in range(longueur):
        carte[l].append("|_|")

def print_carte(carte, alive):
    for h in range(len(carte)):
        laligne = ""
        for l in range(len(carte[0])):
            for r in range(len(robots)):
                ilyarobot = False
                robot_actuelle = robots[r]
                if robot_actuelle.coordonnées == [l, h]:
                    #print(robot_actuelle.nom, robot_actuelle.coordonnées, robot_actuelle.signe, robot_actuelle.direction)
                    """
                    if robot_actuelle.nom != "Scout" and robot_actuelle.coordonnées == Scout.coordonnées:
                        laligne = laligne + "|" + Scout.signe + "|"
                    """
                    if not alive:
                        if Scout.coordonnées == robot_actuelle.coordonnées:
                            laligne = laligne + "|" + "X" + "|"
                        else:
                            try:
                                laligne = laligne + "|" + robot_actuelle.vrai_signe + "|"
                            except:
                                pass
                    else:
                        if robot_actuelle.nom == "Scout":
                            laligne = laligne + "|" + robot_actuelle.signe + "|"
                        if robot_actuelle.nom != "Scout" and alive and robot_actuelle.coordonnées != Scout.coordonnées: 
                            laligne = laligne + "|" + robot_actuelle.signe + "|"
                        ilyarobot = True
                        continue
            if not ilyarobot and l == len(laligne) / 3:
                laligne = laligne + carte[h][l]
        print(laligne)
        #print(len(laligne) / 3)
        

alive = True
gagné = False
while alive and not gagné:
    print_carte(carte, alive)
    laphrase = str(Scout.nom) + " direction: " + str(Scout.direction) + ", " + str(Scout.nom) + " coordonnées: " + str(Scout.coordonnées) +  "\nAvancer vers la droite(6), la gauche(4), le haut(8) ou le bas(5)?: "
    choix1 = str(input(laphrase))
    if choix1 == "6" or choix1 == "4" or choix1 == "8" or choix1 == "5":
        Scout.direction = choix1
        Scout.avancer()
        for i in range(len(robots)):
            if not robots[i] == Scout:
                if robots[i].vrai_coordonnées == Scout.coordonnées:
                    alive = False
                    clear()
                    print_carte(carte, alive)
                    input("T'ES MORT!")
                    continue
        if Scout.coordonnées[0] >= longueur:
            clear()
            print_carte(carte, alive)
            input("T'AS SURVECU!")

    if alive and not gagné:       
        clear()

#print_carte(carte, alive)
