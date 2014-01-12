import pygame
from Position import *
from constantes import *


class Serpent:
    def __init__(self, x, y):
        # Charge l'image du serpent et la convertie dans le bon format
        self.image = pygame.image.load("Serpent.png").convert()
        self.positionTete = Position(x, y)
        self.positionsCorps = list()
        self.direction = "droite"

    def miseAJour(self):
        if self.direction == "droite":
            self.positionTete.x += tailleCase
        elif self.direction == "gauche":
            self.positionTete.x -= tailleCase
        elif self.direction == "haut":
            self.positionTete.y -= tailleCase
        elif self.direction == "bas":
            self.positionTete.y += tailleCase

    def afficher(self, fenetre):
        # Affichage de la tete
        fenetre.blit(self.image, (self.positionTete.x, self.positionTete.y))
        for corps in self.positionsCorps:
            # Affichage de chaque element du corps
            fenetre.blit(self.image, (corps.x, corps.y))

    def changerDirection(self, direction):
        # Si la nouvelle direction est egal a l'actuelle, on quitte
        if direction == self.direction:
            return False
        # Si la nouvelle direction est dans le sens oppose de l'actuelle
        # on quitte afin que le snake ne se rentre pas dedans
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
