import pygame

class pheromone:
    def __init__(self, x, y, distance):
        self.distance_from_nest = distance
        self.rect = pygame.Rect(x, y, 2, 2)
        self.time = 1800

