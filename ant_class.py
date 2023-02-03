import random
import pygame


class Ant:
    def __init__(self, x, y, pygame_width, pygame_height, nest):
        self.ant = pygame.Rect(x, y, 10, 10)
        self.target = (random.randint(0, pygame_width), random.randint(0, pygame_height))
        # 0 = no food, 1 = having food, 2 = seeing food, 3 = seeing home
        self.having_food = 0
        self.pheromone_time = 0
        self.distance = 0
        self.pygame_width = pygame_width
        self.nest = nest


    def sensoring_pheromones(self, food_pheromones: list):
        checking_rect = pygame.Rect(self.ant.x-30, self.ant.y-30, 70, 70)
        smallest_pheromone = 1000000


        for i in food_pheromones:
            if checking_rect.colliderect(i.rect) is True and i.distance_from_nest < smallest_pheromone and i.nest == self.nest:
                smallest_pheromone = i.distance_from_nest
                self.target = (i.rect.x + random.randint(-10, 10), i.rect.y + random.randint(-10, 10))






