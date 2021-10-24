import pygame
from random import randint
import threading
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 00, 00)

color_list = (white, green, blue, red)

class Ball(pygame.sprite.Sprite):

#   __init__ låter dig initialisera classens attribut, i detta fall self, width och height
    def __init__(self, width, height):

        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)
        self.color = white

        pygame.draw.rect(self.image, self.color, [0, 0, width, height])

        self.velocity = [0, 0]

        self.rect = self.image.get_rect()


    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def accelerate(self, direction):
        self.velocity[0] = direction * randint(3, 6)
        self.velocity[1] = randint(-6, 6)

    def delay(self, n, func, arg):
        t = threading.Timer(n, func, args=(arg,))
        t.start()

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)

    def resetPos(self):
        self.rect.x = 345
        self.rect.y = 195
        self.velocity[0] = self.velocity[0]
        self.velocity[1] = randint(-8, 8)

    def changeColor(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color, [0, 0, 10, 10])



