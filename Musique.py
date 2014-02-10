import pygame, os

pygame.mixer.init(22050, -16, 1, 4096)

filename = "Fond.wav"
if not os.path.exists(filename):
    raise IOError("File '%s' not found!"%filename)
background = pygame.mixer.Sound(filename)


canalBackground = pygame.mixer.Channel(1)
background.set_volume(10.0)
background.play(-1)

print 'playing',filename

while pygame.mixer.get_busy():
    print filename, 'is playing'
    

print 'fin', filename
