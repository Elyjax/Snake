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
        
        if pourcentage >= 50 and self.filename == FILENAME5:
            self.filename = FILENAME6
            changement = True
            # Au dela de 75pourcents on lance la derniere piste
        elif pourcentage >= 35 and self.filename == FILENAME4:
            self.filename = FILENAME5
            changement = True
            # Au dela de 50pourcents on lance la cinquieme piste
        elif pourcentage >= 25 and self.filename == FILENAME3:
            self.filename = FILENAME4
            changement = True
            # Au dela de 35pourcents on lance la quatrieme piste
        elif pourcentage >= 15 and self.filename == FILENAME2:
            self.filename = FILENAME3
            changement = True
            # Au dela de 25pourcents on lance la troisieme piste
        elif pourcentage >= 10 and self.filename == FILENAME1:
            self.filename = FILENAME2
            changement = True
            # Au dela de 15pourcents on lance la seconde piste


        if changement == True:
            # on recharge la nouvelle musique
            if not os.path.exists(self.filename):
                raise IOError("File '%s' not found!"%self.filename)
            pygame.mixer.music.queue(self.filename)
            changement = False

        # Relance la musique si arrete
        if pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.play()
        
            

