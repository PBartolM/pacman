import pygame
from pygame.locals import *
from constants import *
from pacman import Pacman
from ghost import Ghost
from pastilla import *


class GameController(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
        self.background = None

    def setBackground(self):
        self.background = pygame.image.load('maze.png')
        self.background = pygame.transform.scale(self.background, (SCREENWIDTH, SCREENHEIGHT))

    def startGame(self):
        self.setBackground()
        self.pacman = Pacman()
        self.ghost = Ghost()
        self.pastilla = Pastilla()
        self.pastillaGrande = PastillaGrande()

    def update(self):
        dt = self.clock.tick(30) / 1000.0
        self.pacman.update(dt)
        self.colisiones()
        self.checkEvents()
        self.render()

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

    def colisiones(self):
        pallet = self.pacman.comer(self.pastilla)
        if pallet:
            self.pastilla.desaparece(self.screen)

        powerpallet = self.pacman.comer(self.pastillaGrande)
        if powerpallet:
            self.pastillaGrande.desaparece(self.screen)
            self.ghost.color = BLUE

        comefantasma= self.pacman.colisionFantasma(self.ghost)
        if comefantasma:
            if self.ghost.color == BLUE:
                self.ghost.radius=0

            else:
                self.pacman.radius=0

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.pacman.render(self.screen)
        self.ghost.render(self.screen)
        self.pastilla.render(self.screen)
        self.pastillaGrande.render(self.screen)
        pygame.display.update()


if __name__ == "__main__":
    game = GameController()
    game.startGame()
    while True:
        game.update()
