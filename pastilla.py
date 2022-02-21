import pygame
from vector import Vector2
from constants import *


class Pastilla(object):
    def __init__(self):

        self.position = Vector2(300, 400)
        self.color = WHITE
        self.radius = int(4 * TILEWIDTH / 16)
        self.collideRadius = int(4 * TILEWIDTH / 16)
        self.visible = True

    def render(self, screen):
        if self.visible:
            p = self.position.asInt()
            pygame.draw.circle(screen, self.color, p, self.radius)

    def desaparece(self, screen):
        if self.visible:
            self.visible=False
            p = self.position.asInt()
            pygame.draw.circle(screen, self.color, p, 0)


class PastillaGrande(Pastilla):
    def __init__(self):
        Pastilla.__init__(self)
        self.position = Vector2(350, 400)
        self.radius = int(14 * TILEWIDTH / 16)
