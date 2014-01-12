# Importe la biblioteque pygame
import pygame
# La syntaxe from x import y permet de ne pas devoir ecrire x.y mais juste y
# L'etoile indique que l'on importe tout
from pygame.locals import *  # Quelques constantes utiles (K_UP, K_RIGHT...)
from Serpent import *
from constantes import *

pygame.init()
# Ouvre une fenetre de tailleCase * nombreCasesLargeur
#                  sur tailleCase * nombreCasesHauteur
fenetre = pygame.display.set_mode((tailleCase * nombreCasesLargeur,
                                   tailleCase * nombreCasesHauteur))
# Creation de l'objet de type Serpent
serpent = Serpent(0, 0)
# Cree une table de correspondance entre les constantes qui represente les
# fleche directionnelles et le nom de la direction
table = dict()
table[K_UP] = "haut"
table[K_RIGHT] = "droite"
table[K_DOWN] = "bas"
table[K_LEFT] = "gauche"
compteur = 0
clock = pygame.time.Clock()
ouvert = True
while ouvert:
    for event in pygame.event.get():  # Gestion des evenements
        # Ferme l'application quand on clique sur la croix
        if event.type == QUIT:
            ouvert = False
        if event.type == KEYDOWN:
            # Ferme aussi l'application quand on appui sur ESC
            if event.key == K_ESCAPE:
                ouvert = False
            if event.key in (K_UP, K_RIGHT, K_DOWN, K_LEFT):
                serpent.changerDirection(table[event.key])
                serpent.miseAJour()
                compteur = 0
            # L'appui sur une touche fleche change la direction du serpent et
            # lance automatique une mise a jour

    # On ajoute le temps ecoule depuis la derniere mise jour a un compteur
    # On met a jour le serpent si compteur > delaisMiseAJour
    # Plus delaisMiseAJour est grand plus le serpent sera lent
    compteur += clock.tick()
    if compteur >= delaisMiseAJour:
        serpent.miseAJour()
        compteur = 0
    fenetre.fill((0, 0, 0))  # On efface l'ecran
    serpent.afficher(fenetre)
    pygame.display.flip()  # On actualise l'ecran
