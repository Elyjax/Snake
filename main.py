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

font1 = pygame.font.SysFont("default", 40)
font2 = pygame.font.SysFont("default", 60)

selectionActuelle = 1
ouvert = True

while ouvert:
    for event in pygame.event.get():
        if event.type == QUIT:
            ouvert = False
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                if selectionActuelle == 1:
                    jouer(fenetre)
                if selectionActuelle == 2:
                    ouvert = False
            if event.key == K_UP:
                selectionActuelle -= 1
                if selectionActuelle < 1:
                    selectionActuelle = 1
            if event.key == K_DOWN:
                selectionActuelle += 1
                if selectionActuelle > 2:
                    selectionActuelle = 2

    couleurJouer = (100, 100, 100)  # Couleur grise
    couleurQuitter = (100, 100, 100)
    if selectionActuelle == 1:
        couleurJouer = (255, 0, 0)  # Couleur rouge
    if selectionActuelle == 2:
        couleurQuitter = (255, 0, 0)

    fenetre.fill((0, 0, 0))  # On efface l'ecran

    # On affiche le menu
    if selectionActuelle == 1:
        text = font2.render("Jouer", 1, couleurJouer)
    else:
        text = font1.render("Jouer", 1, couleurJouer)
    position = text.get_rect()
    position.centerx = fenetre.get_rect().centerx
    position.centery = fenetre.get_rect().bottom * 0.25
    fenetre.blit(text, position)

    if selectionActuelle == 2:
        text = font2.render("Quitter", 1, couleurQuitter)
    else:
        text = font1.render("Quitter", 1, couleurQuitter)
    position = text.get_rect()
    position.centerx = fenetre.get_rect().centerx
    position.centery = fenetre.get_rect().bottom * 0.75
    fenetre.blit(text, position)

    pygame.display.flip()

pygame.quit()
