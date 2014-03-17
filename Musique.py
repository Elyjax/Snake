import pygame, os

class Musique:
    def __init__(self):
        # Initialise le mixer
        pygame.mixer.init(22050, -16, 1, 4096)
        # Canal 1 : fond sonor ( Hautbois )
        filename = "Fond.wav"
        if not os.path.exists(filename):
            raise IOError("File '%s' not found!"%filename)
        self.musique = pygame.mixer.Sound(filename)
        self.canal = pygame.mixer.Channel(1)
        self.canal.set_volume(10.0)
        
    def MoteurMusique(self):
        self.canal.play(self.musique, -1, 0, 0)

    def Pause(self):
        if self.canal.get_busy():
            self.canal.Pause()
        else:
            self.canal.Unpause()

    def Stop(self):
        self.canal.stop()
        

