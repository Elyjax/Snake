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

font = pygame.font.SysFont("default", 40)
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
					selectionActuelle = 2
			if event.key == K_DOWN:
				selectionActuelle += 1
				if selectionActuelle > 2:
					selectionActuelle = 1

	couleurJouer = (0, 255, 0)  # Couleur verte
	couleurQuitter = (0, 255, 0)
	if selectionActuelle == 1:
		couleurJouer = (255, 0, 0)  # Couleur rouge
	if selectionActuelle == 2:
		couleurQuitter = (255, 0, 0)

	fenetre.fill((0, 0, 0))  # On efface l'ecran
	# On affiche le menu
	fenetre.blit(font.render("Jouer", 1, couleurJouer), (100, 50))
	fenetre.blit(font.render("Quitter", 1, couleurQuitter), (100, 100))
	pygame.display.flip()

pygame.quit()
