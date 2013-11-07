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
        # Initialisation provisoire avant aleatoire
        typeFruit = "POMME"
        # Charge l'image du fruit suivant son type
        # Dictionnaire interne pour connaitre le type de fruit
        fruits = dict()
        fruits["POMME"] = "Pomme.png"
        
        # Charge l'image du fruit et la convertie dans le bon format
        self.image = pygame.image.load(fruits[typeFruit]).convert()
        
        collisionCreation = True
        while collisionCreation == True:
            self.positionFruit = Position(
                        random.randint(0, nombreCasesLargeur - 1) * tailleCase,
                        random.randint(0, nombreCasesHauteur - 1) * tailleCase)
            collisionCreation = False
            for corps in serpent.positionsCorps:
                if self.positionFruit == corps:
                    collisionCreatrion = True

    def afficher(self, fenetre):
        # Affichage du fruit
        fenetre.blit(self.image,(self.positionFruit.x, self.positionFruit.y))

    
        
        
    
        