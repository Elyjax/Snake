# Importe la biblioteque pygame
import pygame
# La syntaxe from x import y permet de ne pas devoir ecrire x.y mais juste y
# L'etoile indique que l'on importe tout
from constantes import *
from jouer import *

pygame.init()

# Ouvre une fenetre de tailleCase * nombreCasesLargeur
#                  sur tailleCase * nombreCasesHauteur
fenetre = pygame.display.set_mode((tailleCase * nombreCasesLargeur,
    tailleCase * nombreCasesHauteur))

font1 = pygame.font.Font('font1.ttf', 40)
font2 = pygame.font.Font("font1.ttf", 60)

couleurRouge = (255, 0, 0)
couleurGrise = (100, 100, 100)
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

    fenetre.fill((0, 0, 0))  # On efface l'ecran

    # On affiche le menu
    espacement = fenetre.get_rect().height / (nbMenu + 1)
    for i in range(0, nbMenu):
        if i == selectionActuelle:
            text = font2.render(menu[i], 1, couleurRouge)
        else:
            text = font1.render(menu[i], 1, couleurGrise)
        position = text.get_rect()
        position.centerx = fenetre.get_rect().centerx
        position.centery = espacement * (i + 1)
        fenetre.blit(text, position)

    pygame.display.flip()

pygame.quit()
