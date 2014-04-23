from pygame.locals import *  # Quelques constantes utiles (K_UP, K_RIGHT...)
from time import sleep
from pickle import *
from Serpent import *
from Fruit import *
from Musique import *
from Sauvegarde import *

def jouer(fenetre):
    # Creation de l'objet de type Serpent
    serpent = Serpent(64, 64)
    # Creation de l'objet de type fruits
    fruits = list()
    fruits.append(Fruit(serpent))
    pygame.font.init()

    fontScore = pygame.font.Font("Fonts/font2.ttf", 20)
    fontGameOver = pygame.font.Font("Fonts/font3.ttf", 80)
    fontPause = pygame.font.Font("Fonts/font4.ttf", 60)

    # Cree une table de correspondance entre les constantes qui represente les
    # fleche directionnelles et le nom de la direction
    table = dict()
    table[K_UP] = "haut"
    table[K_RIGHT] = "droite"
    table[K_DOWN] = "bas"
    table[K_LEFT] = "gauche"

    sauvegarde = Sauvegarde()
    try:
        sauvegarde = load(file("sauvegarde", "rb"))
    except IOError: # Si le fichier n'exsite pas, on le cree
        dump(sauvegarde, file("sauvegarde", "wb"))

    #Creation de l'objet de type Musique
    musique = Musique()
    # On joue la musique si elle est activee dans les options
    if sauvegarde.jouerMusique == "On":
        musique.MoteurMusique()

    # Chargement de l'image de fond
    fond = pygame.image.load("Images/Fond.png").convert()
    # Creation de polices de caracteres
    scoreActuel = 0
    compteur = 0
    clock = pygame.time.Clock()
    ouvert = True
    pause = False

    while ouvert:
        for event in pygame.event.get(): # Gestion des evenements
            # Ferme l'application quand on clique sur la croix
            if event.type == QUIT:
                musique.Stop()
                exit()
            if event.type == KEYDOWN:
                # On met le jeu en pause lors de l'appuis sur ESC
                if event.key == K_ESCAPE:
                    if pause:
                        pause = False
                    else:
                        pause = True
                        textePause = fontPause.render("Pause", 1, (110, 200, 255))
                        position = textePause.get_rect()
                        position.center = fenetre.get_rect().center
                        fenetre.blit(textePause, position)
                        pygame.display.flip()

                # Teste si la touche est une fleche
                toucheFleche = (K_UP, K_RIGHT, K_DOWN, K_LEFT)
                if event.key in toucheFleche and pause == False:
                    # Teste si le changement c'est bien effectue
                        if serpent.changerDirection(table[event.key]):
                            serpent.miseAJour(fruits)
                            compteur = 0
                # L'appui sur une touche fleche change la direction du serpent et
                # lance automatique une mise a jour

        if pause == False:
            # On ajoute le temps ecoule depuis la derniere mise jour a un compteur
            # On met a jour le serpent si compteur > delaisMiseAJour
	    # On selectionne delaisMiseAJour selon la vitesse du serpent
            # Plus delaisMiseAJour est grand plus le serpent sera lent
            delaisMiseAJour = [200, 100, 50, 25][sauvegarde.vitesse]
            compteur += clock.tick()
            if compteur >= delaisMiseAJour:
                serpent.miseAJour(fruits)
                compteur = 0

            # Si le serpent rencontre un bord du niveau ou se rentre dedans, on quitte
            if serpent.testCollision():
                musique.Stop()
                break
            # On efface l'ecran
            fenetre.fill((0, 0, 0))

            # On affiche le fond
            for i in range(tailleBord, nombreCasesLargeur - tailleBord):
                for j in range(tailleBord, nombreCasesHauteur - tailleBord):
                    fenetre.blit(fond, (i * tailleCase, j * tailleCase))

            # Affichage des fruits
            for fruit in fruits:
                fruit.afficher(fenetre)

            # Affichage des serpents
            serpent.afficher(fenetre)

            # Mise a jour des scores
            scoreActuel = len(serpent.positionsCorps) - 1
            if scoreActuel > sauvegarde.score:
                sauvegarde.score = scoreActuel
                dump(sauvegarde, file("sauvegarde", "wb"))

            # Affichage des scores
            fenetre.blit(fontScore.render("Score : " + str(scoreActuel), 1,
                (255, 255, 255)), (0, 0))
            fenetre.blit(fontScore.render("Meilleur score : " + str(sauvegarde.score), 1,
                (255, 255, 255)), (0, 16))

            # On actualise l'ecran
            pygame.display.flip()

    # Affichage de l'ecran de GameOver
    fenetre.fill((0, 0, 0))
    gameOver = fontGameOver.render("Game Over !", 1, (230, 160, 20))
    fen = fenetre.get_rect()
    position = gameOver.get_rect()
    position.center = fen.center
    fenetre.blit(gameOver, position)
    score = fontScore.render("Votre score : " + str(scoreActuel), 1, (255, 255, 255))
    position = score.get_rect()
    position.centerx = fen.centerx
    position.centery = fen.height * 0.75
    fenetre.blit(score, position)
    pygame.display.flip()
    sleep(2)
    pygame.event.clear()
