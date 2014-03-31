# Import Pygame
import pygame
# Import aleatoire
import random
# Import les classes necessaires
from Position import *
from constantes import *
from Serpent import *


class Fruit :
    def __init__(self, serpent):
        i = random.randint(0, 3)
        if i == 0 or i == 1:
            self.typeFruit = 0
        if i == 2:
            self.typeFruit = 1
        if i == 3:
            self.typeFruit = 2
            
        # Charge l'image du fruit et la convertie dans le bon format
        self.image = pygame.image.load("Images/Fruits.png").convert_alpha()

        collisionCreation = True
        while collisionCreation == True:
            self.positionFruit = Position(
                random.randint(tailleBord, nombreCasesLargeur - tailleBord - 1) * tailleCase,
                random.randint(tailleBord, nombreCasesHauteur - tailleBord - 1) * tailleCase)
            collisionCreation = False
            for corps in serpent.positionsCorps:
                if self.positionFruit.x == corps.x and \
                   self.positionFruit.y == corps.y:
                    collisionCreation = True

    def afficher(self, fenetre):
        surfaceAffichee = (self.typeFruit * tailleCase, 0, tailleCase, tailleCase)
        # Affichage du fruits
        fenetre.blit(self.image,(self.positionFruit.x, self.positionFruit.y), surfaceAffichee)
