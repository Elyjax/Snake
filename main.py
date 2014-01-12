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
compteur = 0
clock = pygame.time.Clock()
ouvert = True
while ouvert:
    for event in pygame.event.get():  # Gestion des evenements
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
            # L'appui sur une touche lance automatique une mise a jour
            # afin d'eviter que certaine commande ne soit pas prise en
            # compte car une autre touche a ete pressee avant le cycle
            # de mise a jour
            serpent.miseAJour()
            temps = 0
    # On ajoute le temps ecoule depuis la derniere misea jour a un compteur
    # On met a jour le serpent si compteur > delaisMiseAJour
    # Plus delaisMiseAJour est grand plus le serpent sera lent
    compteur += clock.tick()
    if compteur >= delaisMiseAJour:
        serpent.miseAJour()
        compteur = 0
    fenetre.fill((0, 0, 0))  # On efface l'ecran
    serpent.afficher(fenetre)
    pygame.display.flip()  # On actualise l'ecran
