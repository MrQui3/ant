import random
import pygame
import home


class Ant:
    def __init__(self):
        self.ant = pygame.Rect(home.pos[0], home.pos[1], 10, 10)
        self.target = (random.randint(-200, 200), random.randint(-200, 200))

    def new_target(self):
        self.target = (random.randint(-200, 200), random.randint(-200, 200))
