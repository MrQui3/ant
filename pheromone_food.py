import pygame

class pheromone:
    def __init__(self, x, y):
        self.time = 300
        self.rect = pygame.Rect(x, y, 2, 2)

