import pygame

class Pheromone:
    def __init__(self, cords: list, distance: int):
        self.pheromone_distance = distance
        self.cords = cords
        self.time = 1800
        self.rect = pygame.Rect(cords[0], cords[1], 5, 5)
