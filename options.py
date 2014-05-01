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
    font2 = pygame.font.Font("Fonts/font1.ttf", 70)
    selectionActuelle = 0
    largeurMin = 20
    largeurMax= 30
    hauteurMin = 10
    hauteurMax = 20
    ouvert = True
    vitesses = ["Lente", "Normale", "Rapide", "Extreme"]
    selections = ["Vitesse", "Largeur", "Hauteur", "Musique", "Retour"]

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

                # Gestion du changement de la largeur
                if selections[selectionActuelle] == "Largeur":
                    if event.key == K_LEFT:
                        sauvegarde.largeur -= 1
                        if sauvegarde.largeur < largeurMin:
                            sauvegarde.largeur = largeurMin

                    if event.key == K_RIGHT:
                        sauvegarde.largeur += 1
                        if sauvegarde.largeur > largeurMax:
                            sauvegarde.largeur = largeurMax

                # Gestion du changement de la hauteur
                if selections[selectionActuelle] == "Hauteur":
                    if event.key == K_LEFT:
                        sauvegarde.hauteur -= 1
                        if sauvegarde.hauteur < hauteurMin:
                            sauvegarde.hauteur = hauteurMin

                    if event.key == K_RIGHT:
                        sauvegarde.hauteur += 1
                        if sauvegarde.hauteur > hauteurMax:
                            sauvegarde.hauteur = hauteurMax

                if event.key == K_RETURN:
                    if selections[selectionActuelle] == "Retour":
                        ouvert = False

        		    # Bascule de la musique entre On et Off
                    if selections[selectionActuelle] == "Musique":
                        if sauvegarde.jouerMusique == "On":
                            sauvegarde.jouerMusique = "Off"
                        else:
                            sauvegarde.jouerMusique = "On"

        fenetre.fill(couleurBlanche)  # On efface l'ecran

        # On affiche le menu
        espacement = fenetre.get_rect().height / (len(selections) + 1)
        for i in range(0, len(selections)):
            # On affiche d'abord l'option (Vitesse, Musique, etc)
            # La police change de couleur et taille lorsqu'on selectionne l'option
            if i == selectionActuelle:
                option = font2.render(selections[i], 1, couleurRouge)
            else:
                option = font1.render(selections[i], 1, couleurNoire)

            position = option.get_rect()
            position.centerx = fenetre.get_rect().centerx
            position.centery = espacement * (i + 1)
            fenetre.blit(option, position)

            # Puis on affiche sa valeur
            if selections[i] == "Vitesse":
                texte = vitesses[sauvegarde.vitesse]

            if selections[i] == "Largeur":
                texte = str(sauvegarde.largeur)

            if selections[i] == "Hauteur":
                texte = str(sauvegarde.hauteur)

            if selections[i] == "Musique":
                texte = sauvegarde.jouerMusique

            if selections[i] == "Retour":
                texte = ""

            if i == selectionActuelle:
                valeurOption = font2.render(texte, 1, couleurRouge)
            else:
                valeurOption = font1.render(texte, 1, couleurNoire)

            positionBis = valeurOption.get_rect()
            positionBis.centery = espacement * (i + 1)
            positionBis.centerx = position.right + (fenetre.get_width() - position.right) / 2
            fenetre.blit(valeurOption, positionBis)

        pygame.display.flip()

    # On sauvegarde les options
    dump(sauvegarde, file("sauvegarde", "wb"))

    fenetre = pygame.display.set_mode((tailleCase * (sauvegarde.largeur + 2 * tailleBord),
                                        tailleCase * (sauvegarde.hauteur + 2 * tailleBord)))
