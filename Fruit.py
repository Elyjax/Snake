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
        # Charge l'image du fruit et la convertie dans le bon format
        self.image = pygame.image.load("Images/Fruits.png").convert_alpha()
        self.serpent = serpent
        self.generer()
    
    def generer(self):
        i = random.randint(0, 3)
        if i == 0 or i == 1:
            self.typeFruit = 0  # Pomme
        if i == 2:
            self.typeFruit = 1  # Banane
        if i == 3:
            self.typeFruit = 2  # Orange

        # On verifie que le fruit n'apparait pas dans le serpent
        collisionCreation = True
        while collisionCreation == True:
            self.positionFruit = Position(
                random.randint(tailleBord, nombreCasesLargeur - tailleBord - 1) * tailleCase,
                random.randint(tailleBord, nombreCasesHauteur - tailleBord - 1) * tailleCase)
            collisionCreation = False
            for corps in self.serpent.positionsCorps:
                if self.positionFruit.x == corps.x and \
                   self.positionFruit.y == corps.y:
                    collisionCreation = True

    def afficher(self, fenetre):
        surfaceAffichee = (self.typeFruit * tailleCase, 0, tailleCase, tailleCase)
        # Affichage du fruit en fonction de son type
        fenetre.blit(self.image,(self.positionFruit.x, self.positionFruit.y), surfaceAffichee)
