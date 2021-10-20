import pygame
from random import randint
import threading
black = (0, 0, 0)


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [0, 0]

        self.rect = self.image.get_rect()


    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def accelerate(self, direction):
        self.velocity[0] = direction * randint(3, 6)
        self.velocity[1] = randint(-6, 6)

    def delay(self, n, direction):
        t = threading.Timer(n, self.accelerate, args=(direction,))
        t.start()

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)

    def resetPos(self, color):
        self.rect.x = 345
        self.rect.y = 195
        self.velocity[0] = self.velocity[0]
        self.velocity[1] = randint(-8, 8)



