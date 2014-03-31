# Importe la biblioteque pygame
import pygame
# La syntaxe from x import y permet de ne pas devoir ecrire x.y mais juste y
# L'etoile indique que l'on importe tout
from constantes import *

def options(fenetre):
    
    selectionActuelle = 0
    selections = ["Vitesse", "Musique", "Menu"]
    
    ouvert = True

    while ouvert:
        for event in pygame.event.get(): # Gestion des evenements
            # Ferme l'application quand on clique sur la croix
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                # Ferme aussi l'application quand on appui sur ESC
                    if event.key == K_ESCAPE:
                        ouvert = False
                    if event.key == K_UP:
                        selectionActuelle -= 1
                        if selectionActuelle < 0:
                            selectionActuelle = 0
                    if event.key == K_DOWN:
                        selectionActuelle += 1
                        if selectionActuelle >= len(selections):
                            selectionActuelle = len(selections) - 1
