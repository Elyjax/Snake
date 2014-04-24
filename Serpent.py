import pygame
from Position import Position
from constantes import *
from Fruit import *
import random

class Serpent:
    def __init__(self, x, y):
        # Charge l'image du corps du serpent et la convertie dans le bon format
        self.imageCorps = pygame.image.load("Images/Corps.png").convert_alpha()
        # Charge l'image de la tete du serpent
        # Celle ci contient les quatres positions possibles de la tete
        self.imageTete = pygame.image.load("Images/Tetes.png").convert_alpha()
        self.positionsCorps = list()
        self.positionsCorps.append(Position(x, y))
        self.positionsCorps.append(Position(-tailleCase, -tailleCase))
        self.positionTete = self.positionsCorps[0]
        self.direction = "droite"

    def miseAJour(self, fruits):
        pos = Position(self.positionTete.x, self.positionTete.y)
        if self.direction == "droite":
            self.positionTete.x += tailleCase
        elif self.direction == "gauche":
            self.positionTete.x -= tailleCase
        elif self.direction == "haut":
            self.positionTete.y -= tailleCase
        elif self.direction == "bas":
            self.positionTete.y += tailleCase
        for corps in self.positionsCorps[1 :]:
            tmp = Position(corps.x, corps.y)
            corps.x = pos.x
            corps.y = pos.y
            pos = tmp
        self.testManger(fruits)

    def afficher(self, fenetre):
        # Affichage de la tete
        # On n'affiche que la partie de l'image qui contient la tete dans la
        # bonne direction
        if self.direction == "haut":
            pos = 0
        elif self.direction == "bas":
            pos = 1
        elif self.direction == "droite":
            pos = 2
        elif self.direction == "gauche":
            pos = 3
        surfaceAfficher = (pos * tailleCase, 0, tailleCase, tailleCase)
        fenetre.blit(self.imageTete, (self.positionTete.x, self.positionTete.y)
                     , surfaceAfficher)

        # Affichage de chaque element du corps
        for corps in self.positionsCorps[1 :]:
            fenetre.blit(self.imageCorps, (corps.x, corps.y), (0, 0, tailleCase, tailleCase))

    def changerDirection(self, direction):
        # Si la nouvelle direction est egal a l'actuelle, on quitte
        if direction == self.direction:
            return False
        # Si la nouvelle direction est dans le sens oppose de l'actuelle
        # on renvoit faux afin que le snake ne se rentre pas dedans
        if direction == "haut" and self.direction == "bas":
            return False
        if direction == "droite" and self.direction == "gauche":
            return False
        if direction == "bas" and self.direction == "haut":
            return False
        if direction == "gauche" and self.direction == "droite":
            return False
        # Sinon on change la direction et on renvoit vrai
        self.direction = direction
        return True

    def malus(self):
        self.positionsCorps.reverse()
        self.positionTete = self.positionsCorps[0]
        tete = self.positionTete
        corps = self.positionsCorps[1]
        if tete.y > corps.y:
            self.direction = "bas"
        elif tete.y < corps.y:
            self.direction = "haut"
        elif tete.x < corps.x:
            self.direction = "gauche"
        elif tete.x > corps.x:
            self.direction = "droite"

    def testCollision(self):
        for corps in self.positionsCorps[1 :]:
            if self.positionTete.x == corps.x and \
               self.positionTete.y == corps.y:
                return True
            if self.positionTete.x >= (nombreCasesLargeur - tailleBord) * tailleCase:
                return True
            if self.positionTete.y >= (nombreCasesHauteur - tailleBord) * tailleCase:
                return True
            if self.positionTete.x < tailleBord * tailleCase:
		print("ok")
                return True
            if self.positionTete.y < tailleBord * tailleCase:
                return True
        return False

    def testManger(self, fruits):
        for index, fruit in enumerate(fruits):
            if self.positionTete.x == fruit.positionFruit.x and \
               self.positionTete.y == fruit.positionFruit.y:
                if fruit.typeFruit == 1:
                    self.malus()
                if fruit.typeFruit == 2:
                    for i in range(0, 10):
                        self.positionsCorps.append(Position(-tailleCase, -tailleCase))
                fruits.pop(index)
                fruits.append(Fruit(self))
                self.positionsCorps.append(Position(-tailleCase, -tailleCase))
