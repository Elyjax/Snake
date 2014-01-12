import pygame
from pygame.locals import *
from Serpent import *
from constantes import *

pygame.init()
# Ouvre une fenetre de tailleCase * nombreCasesLargeur
#                  sur tailleCase * nombreCasesHauteur
fenetre = pygame.display.set_mode((tailleCase * nombreCasesLargeur,
                                   tailleCase * nombreCasesHauteur))
# Creation de l'objet de type Serpent
serpent = Serpent(0, 0)
clock = pygame.time.Clock()
ouvert = True
while ouvert:
    for event in pygame.event.get():
        # Ferme l'application quand on clique sur la croix
        if event.type == QUIT:
            ouvert = False
        # Change la direction du serpent lors de l'appui sur une touche fleche
        if event.type == KEYDOWN:
            if event.key == K_UP:
                serpent.changerDirection("haut")
            if event.key == K_RIGHT:
                serpent.changerDirection("droite")
            if event.key == K_DOWN:
                serpent.changerDirection("bas")
            if event.key == K_LEFT:
                serpent.changerDirection("gauche")
    pygame.time.delay(100)
    clock.tick()
    print(clock.get_fps())
    serpent.miseAJour()
    serpent.afficher(fenetre)
    pygame.display.flip()
