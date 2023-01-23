import pygame

class pheromone:
    def __init__(self, x, y):
        self.time = 500
        self.rect = pygame.Rect(x, y, 2, 2)

