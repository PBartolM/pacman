import pygame
from pygame.locals import *
from vector import Vector2
from constants import *


class Ghost(object):
    def __init__(self):
        self.position = Vector2(400, 400)
        self.radius = 10
        self.color = RED

    def render(self, screen):
        p = self.position.asInt()
        pygame.draw.circle(screen, self.color, p, self.radius)

    # obsoleto , lo dejo pero ya no vale
    # def muerte(self, screen):
    #     p = self.position.asInt()
    #     pygame.draw.circle(screen, self.color, p, 0)
    # obsoleto , lo dejo pero ya no vale
    # def miedo(self, screen):
    #     if self.color == BLUE:
    #         p = self.position.asInt()
    #         pygame.draw.circle(screen, self.color, p, 0)
