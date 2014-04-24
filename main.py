# Importe la biblioteque pygame
import pygame
# La syntaxe from x import y permet de ne pas devoir ecrire x.y mais juste y
# L'etoile indique que l'on importe tout
from constantes import *
from Sauvegarde import *
from jouer import *
from options import *

pygame.init()

sauvegarde = Sauvegarde()
try:
    sauvegarde = load(file("sauvegarde", "rb"))
except IOError: # Si le fichier n'exsite pas, on le cree
    dump(sauvegarde, file("sauvegarde", "wb"))

# Ouvre une fenetre dont les dimensions dependent des options en hauteur et largeur
fenetre = pygame.display.set_mode((tailleCase * (sauvegarde.largeur + 2 * tailleBord),
                                    tailleCase * (sauvegarde.hauteur + 2 * tailleBord)))
# On definit le titre de la fenetre
pygame.display.set_caption("Snake")

font1 = pygame.font.Font('Fonts/font1.ttf', 40)
font2 = pygame.font.Font("Fonts/font1.ttf", 80)

selectionActuelle = 0
menu = ["Jouer", "Options", "Quitter"]
nbMenu = len(menu)
ouvert = True

while ouvert:
    for event in pygame.event.get():
        if event.type == QUIT:
            ouvert = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                ouvert = False
            if event.key == K_RETURN:
                if menu[selectionActuelle] == "Jouer":
                    jouer(fenetre)
                if menu[selectionActuelle] == "Options":
                    options(fenetre)
                if menu[selectionActuelle] == "Quitter":
                    ouvert = False
            if event.key == K_UP:
                selectionActuelle -= 1
                if selectionActuelle < 0:
                    selectionActuelle = 0
            if event.key == K_DOWN:
                selectionActuelle += 1
                if selectionActuelle >= nbMenu:
                    selectionActuelle = nbMenu - 1

    fenetre.fill(couleurBlanche)  # On efface l'ecran

    # On affiche le menu
    espacement = fenetre.get_rect().height / (nbMenu + 1)
    for i in range(0, nbMenu):
        if i == selectionActuelle:
            text = font2.render(menu[i], 1, couleurRouge)
        else:
            text = font1.render(menu[i], 1, couleurNoire)
        position = text.get_rect()
        position.centerx = fenetre.get_rect().centerx
        position.centery = espacement * (i + 1)
        fenetre.blit(text, position)

    pygame.display.flip()

pygame.quit()
