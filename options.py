# Importe la biblioteque pygame
import pygame
# La syntaxe from x import y permet de ne pas devoir ecrire x.y mais juste y
# L'etoile indique que l'on importe tout
from pickle import *
from Sauvegarde import *
from constantes import *
from pygame.locals import * # Quelques constantes utiles

def options(fenetre):

    font1 = pygame.font.Font("Fonts/font1.ttf", 40)
    font2 = pygame.font.Font("Fonts/font1.ttf", 80)
    selectionActuelle = 0
    ouvert = True
    vitesses = ["Lente", "Normale", "Rapide", "Extreme"]
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

		# Deplacement dans le menu avec les fleches directionnelle
                if event.key == K_UP:
                    selectionActuelle -= 1
                    if selectionActuelle < 0:
                        selectionActuelle = 0

                if event.key == K_DOWN:
                    selectionActuelle += 1
                    if selectionActuelle >= len(selections):
                        selectionActuelle = len(selections) - 1

		# Modification de la vitesse
		# 4 niveaux de vitesses differents
                if selections[selectionActuelle] == "Vitesse":
                    if event.key == K_LEFT:
                        sauvegarde.vitesse -= 1
                        if sauvegarde.vitesse < 0:
                            sauvegarde.vitesse = 0

                    if event.key == K_RIGHT:
                        sauvegarde.vitesse += 1
                        if sauvegarde.vitesse > 3:
                            sauvegarde.vitesse = 3

		# Bascule de la musique entre On et Off
                if event.key == K_RETURN:
                    if selections[selectionActuelle] == "Retour":
                        ouvert = False

                    if selections[selectionActuelle] == "Musique":
                        if sauvegarde.jouerMusique == "On":
                            sauvegarde.jouerMusique = "Off"
                        else:
                            sauvegarde.jouerMusique = "On"

        fenetre.fill(couleurBlanche)  # On efface l'ecran

        # On affiche le menu
        espacement = fenetre.get_rect().height / (len(selections) + 1)
        for i in range(0, len(selections)):
            if i == selectionActuelle:
                text = font2.render(selections[i], 1, couleurRouge)
            else:
                text = font1.render(selections[i], 1, couleurNoire)
            position = text.get_rect()
            position.centerx = fenetre.get_rect().centerx
            position.centery = espacement * (i + 1)
            fenetre.blit(text, position)

            if selections[i] == "Vitesse" :
                # Affichage de la vitesse
		if i == selectionActuelle:
	            textBis = font2.render(vitesses[sauvegarde.vitesse], 1, couleurRouge)
		else:
		    textBis = font1.render(vitesses[sauvegarde.vitesse], 1, couleurNoire)
		positionBis = textBis.get_rect()
		positionBis.centery = espacement * (i + 1)
                positionBis.centerx = position.right + (fenetre.get_width() - position.right) / 2
                fenetre.blit(textBis, positionBis)

            if selections[i] == "Musique" :
                # Affichage de l'option musique
		if i == selectionActuelle:
                    textBis = font2.render(sauvegarde.jouerMusique, 1, couleurRouge)
                else:
                    textBis = font1.render(sauvegarde.jouerMusique, 1, couleurNoire)
		positionBis = textBis.get_rect()
		positionBis.centery = espacement * (i + 1)
                positionBis.centerx = position.right + (fenetre.get_width() - position.right) / 2
                fenetre.blit(textBis, positionBis)
	
        pygame.display.flip()

    # On sauvegarde les options
    dump(sauvegarde, file("sauvegarde", "wb"))
