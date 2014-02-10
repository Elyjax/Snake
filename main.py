# Importe la biblioteque pygame
import pygame
# La syntaxe from x import y permet de ne pas devoir ecrire x.y mais juste y
# L'etoile indique que l'on importe tout
from pygame.locals import *  # Quelques constantes utiles (K_UP, K_RIGHT...)
from Serpent import *
from Fruit import *
from constantes import *
from Musique import *

pygame.init()
# Ouvre une fenetre de tailleCase * nombreCasesLargeur
#                  sur tailleCase * nombreCasesHauteur
fenetre = pygame.display.set_mode((tailleCase * nombreCasesLargeur,
                                   tailleCase * nombreCasesHauteur))
# Creation de l'objet de type Serpent
serpent = Serpent(0, 0)
# Creation de l'objet de type fruits
fruits = list()
fruits.append(Fruit(serpent))
#Creation de l'objet de type Musique
musique = Musique()
musique.MoteurMusique()

# Creation police de caractere pour texte potentiel
pygame.font.init()
font = pygame.font.SysFont("default", 30)

# Cree une table de correspondance entre les constantes qui represente les
# fleche directionnelles et le nom de la direction
table = dict()
table[K_UP] = "haut"
table[K_RIGHT] = "droite"
table[K_DOWN] = "bas"
table[K_LEFT] = "gauche"
meilleurScore = 0
try:
    fichierScore = open("score.txt", "r")
    meilleurScore = fichierScore.read()
    fichierScore.close()
except IOError: # Si le fichier n'exsite pas, on le cree
    fichierScore = open("score.txt", "w")
    fichierScore.write("0")
    fichierScore.close()

scoreActuel = 0
compteur = 0
clock = pygame.time.Clock()
ouvert = True
while ouvert:
    for event in pygame.event.get(): # Gestion des evenements
        # Ferme l'application quand on clique sur la croix
        if event.type == QUIT:
            ouvert = False
        if event.type == KEYDOWN:
            # Ferme aussi l'application quand on appui sur ESC
            if event.key == K_ESCAPE:
                ouvert = False
            # Teste si la touche est une fleche
            toucheFleche = (K_UP, K_RIGHT, K_DOWN, K_LEFT)
            if event.key in toucheFleche:
                # Teste si le changement c'est bien effectue
                if serpent.changerDirection(table[event.key]):
                    serpent.miseAJour(fruits)
                    compteur = 0
            # L'appui sur une touche fleche change la direction du serpent et
            # lance automatique une mise a jour

    # On ajoute le temps ecoule depuis la derniere mise jour a un compteur
    # On met a jour le serpent si compteur > delaisMiseAJour
    # Plus delaisMiseAJour est grand plus le serpent sera lent
    compteur += clock.tick()
    if compteur >= delaisMiseAJour:
        serpent.miseAJour(fruits)
        compteur = 0

    # Si le serpent rencontre un bord du niveau ou se rentre dedans, on quitte
    if serpent.testCollision():
        break
    # Affichage
    fenetre.fill((0, 0, 0))  # On efface l'ecran

    # Affichage des fruits
    for fruit in fruits:
        fruit.afficher(fenetre)

    # Affichage des serpents
    serpent.afficher(fenetre)

    # Mise a jour des scores
    scoreActuel = str(len(serpent.positionsCorps) - 1)
    if scoreActuel > meilleurScore:
        meilleurScore = scoreActuel
        fichierScore = open("score.txt", "w")
        fichierScore.write(str(meilleurScore))
        fichierScore.close()
            
    # Affichage des scores
    fenetre.blit(font.render("Score : " + str(scoreActuel), 1,
                             (255, 255, 255)), (0, 0))
    fenetre.blit(font.render("Meilleur score : " + str(meilleurScore), 1,
                             (255, 255, 255)), (0, 16))
    
    pygame.display.flip()  # On actualise l'ecran

pygame.quit()
