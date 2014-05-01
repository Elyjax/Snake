import pygame, os
from constantes import *

class Musique:
    def __init__(self):
        # Initialise le mixer
        pygame.mixer.init(22050, -16, 1, 4096)
        self.filename = FILENAME1
        if not os.path.exists(self.filename):
            raise IOError("File '%s' not found!"%self.filename)
        pygame.mixer.music.load(self.filename)
        self.canal = pygame.mixer.Channel(1)
        pygame.mixer.music.set_volume(1.0)

    def jouer(self):
        pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def reprendre(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()
        self.FILENAME = FILENAME1

    def moteurMusique(self, tailleSerpent, x, y):
        # Moteur de la musique, lance la piste suivante suivant la taille du
        # serpent. La taille du serpent est ramene en pourcentage par rapport
        # a l'aire de la grille de jeu comme elle est variable.
        pourcentage = tailleSerpent * 100 / (x * y)

        changement = False # Sert a detecter un changement de musique

        # On adapte la piste audio en fonction du pourcentage
        # Il y a 6 paliers differents
        if pourcentage >= 30 and self.filename == FILENAME5:
            self.filename = FILENAME6
            changement = True
        elif pourcentage >= 25 and self.filename == FILENAME4:
            self.filename = FILENAME5
            changement = True
        elif pourcentage >= 20 and self.filename == FILENAME3:
            self.filename = FILENAME4
            changement = True
        elif pourcentage >= 10 and self.filename == FILENAME2:
            self.filename = FILENAME3
            changement = True
        elif pourcentage >= 5 and self.filename == FILENAME1:
            self.filename = FILENAME2
            changement = True

        if changement == True:
            # on recharge la nouvelle musique
            if not os.path.exists(self.filename):
                raise IOError("File '%s' not found!"%self.filename)
            pygame.mixer.music.queue(self.filename)

        # Relance la musique si arrete
        if pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.play()


