import home
import random
import pygame

class Ant:
    def __init__(self, screen: pygame.Surface):
        self.position = (random.randint(10, 590), random.randint(10, 590))
        self.size = (5, 10)
        self.rotation = random.randint(0, 359)
        self.speed = 1
        self.color = (255, 0, 0)
        self.ant = pygame.Rect(self.position[0], self.position[1], 5, 10)
        self.ant = pygame.transform.rotate(screen, 90)
