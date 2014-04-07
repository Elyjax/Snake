# Importe la biblioteque pygame
import pygame
# La syntaxe from x import y permet de ne pas devoir ecrire x.y mais juste y
# L'etoile indique que l'on importe tout
from pickle import *
from Sauvegarde import *
from constantes import *
from pygame.locals import * # Quelques constantes utiles

def options(fenetre):

    font1 = pygame.font.Font('font1.ttf', 30)
    font2 = pygame.font.Font("font1.ttf", 40)
    couleurRouge = (255, 0, 0)
    couleurGrise = (100, 100, 100)

    selectionActuelle = 0
    ouvert = True

    selections = ["Vitesse", "Musique", "Retour"]
    sauvegarde = Sauvegarde()
    try:
        sauvegarde = load(file("sauvegarde", "rb"))
    except IOError: # Si le fichier n'exsite pas, on le cree
        dump(sauvegarde, file("sauvegarde", "wb"))

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

                if selections[selectionActuelle] == "Vitesse":
                    if event.key == K_LEFT:
                        sauvegarde.vitesse -= 1
                        if sauvegarde.vitesse < 1:
                            sauvegarde.vitesse = 1

                    if event.key == K_RIGHT:
                        sauvegarde.vitesse += 1
                        if sauvegarde.vitesse > 9:
                            sauvegarde.vitesse = 9

                if event.key == K_RETURN:
                    if selections[selectionActuelle] == "Retour":
                        ouvert = False

                    if selections[selectionActuelle] == "Musique":
                        if sauvegarde.jouerMusique:
                            sauvegarde.jouerMusique = False
                        else:
                            sauvegarde.jouerMusique = True

        fenetre.fill((0, 0, 0))  # On efface l'ecran

        # On affiche le menu
        espacement = fenetre.get_rect().height / (len(selections) + 1)
        for i in range(0, len(selections)):
            if i == selectionActuelle:
                text = font2.render(selections[i], 1, couleurRouge)
            else:
                text = font1.render(selections[i], 1, couleurGrise)
            position = text.get_rect()
            position.centerx = fenetre.get_rect().centerx
            position.centery = espacement * (i + 1)
            fenetre.blit(text, position)

            if selections[i] == "Vitesse" :
                # Affichage de la vitesse
                textBis = font2.render(str(sauvegarde.vitesse), 1, couleurRouge)
                positionBis = position
                positionBis.centerx = fenetre.get_width() - 1.5 * textBis.get_width()
                fenetre.blit(textBis, positionBis)
            if selections[i] == "Musique" :
                # Affichage de la vitesse
                if sauvegarde.jouerMusique:
                    textBis = font2.render("On", 1, couleurRouge)
                else:
                    textBis = font2.render("Off", 1, couleurRouge)
                positionBis = position
                positionBis.centerx = fenetre.get_width() - 1.5 * textBis.get_width()
                fenetre.blit(textBis, positionBis)

        pygame.display.flip()

    # On sauvegarde les options
    dump(sauvegarde, file("sauvegarde", "wb"))
