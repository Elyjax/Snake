import pygame, os

class Musique:
    def __init__(self):
        # Initialise le mixer
        pygame.mixer.init(22050, -16, 1, 4096)
        # Canal 1 : fond sonor ( Hautbois )
        filename = "Fond.wav"
        if not os.path.exists(filename):
            raise IOError("File '%s' not found!"%filename)
        self.background = pygame.mixer.Sound(filename)
        self.canalBackground = pygame.mixer.Channel(1)
        
    def MoteurMusique(self):
        self.canalBackground.set_volume(10.0)
        self.canalBackground.play(self.background, -1, 0, 0)
        

