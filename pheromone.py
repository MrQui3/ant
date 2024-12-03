import pygame

class Pheromone:
    def __init__(self, cords: list, distance: int):
        self.pheromone_distance = distance
        self.time = 1200
        self.rect = pygame.Rect(cords[0], cords[1], 2, 2)
