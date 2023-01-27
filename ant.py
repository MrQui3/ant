import random
import pygame


class Ant:
    def __init__(self, x, y, pygame_width, pygame_height):
        self.ant = pygame.Rect(x, y, 10, 10)
        self.target = (random.randint(0, pygame_width), random.randint(0, pygame_height))
        # 0 = no food, 1 = having food, 2 = seeing food, 3 = seeing home
        self.having_food = 0
        self.pheromone_time = 0
        self.distance = 0


    def sensoring_pheromones(self, food_pheromones: list):
        left = pygame.Rect(self.ant.x-30, self.ant.y-30, 30, 70)
        above = pygame.Rect(self.ant.x-30, self.ant.y-30, 70, 30)
        right = pygame.Rect(self.ant.x+10, self.ant.y-30, 30, 70)
        below = pygame.Rect(self.ant.x-30, self.ant.y+10, 70, 30)
        smallest_pheromone = 1000000


        for i in food_pheromones:
            if left.colliderect(i.rect) is True:
                if above.colliderect(i.rect) is True:
                    if i.distance_from_nest < smallest_pheromone:
                        smallest_pheromone = i.distance_from_nest
                        self.target = (i.rect.x, i.rect.y)
                        i.time = 100
                elif below.colliderect(i.rect) is True:
                    if i.distance_from_nest < smallest_pheromone:
                        smallest_pheromone = i.distance_from_nest
                        self.target = (i.rect.x, i.rect.y)
                        i.time = 100
                else:
                    if i.distance_from_nest < smallest_pheromone:
                        smallest_pheromone = i.distance_from_nest
                        self.target = (i.rect.x, i.rect.y)
                        i.time = 100
            if above.colliderect(i.rect) is True:
                if right.colliderect(i.rect) is True:
                    if i.distance_from_nest < smallest_pheromone:
                        smallest_pheromone = i.distance_from_nest
                        self.target = (i.rect.x, i.rect.y)
                        i.time = 100
                else:
                    if i.distance_from_nest < smallest_pheromone:
                        smallest_pheromone = i.distance_from_nest
                        self.target = (i.rect.x, i.rect.y)
                        i.time = 100
            if right.colliderect(i.rect) is True:
                if below.colliderect(i.rect) is True:
                    if i.distance_from_nest < smallest_pheromone:
                        smallest_pheromone = i.distance_from_nest
                        self.target = (i.rect.x, i.rect.y)
                        i.time = 100
                else:
                    if i.distance_from_nest < smallest_pheromone:
                        smallest_pheromone = i.distance_from_nest
                        self.target = (i.rect.x, i.rect.y)
                        i.time = 100
            if below.colliderect(i.rect) is True:
                if i.distance_from_nest < smallest_pheromone:
                    smallest_pheromone = i.distance_from_nest
                    self.target = (i.rect.x, i.rect.y)
                    i.time = 100





