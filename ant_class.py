import random
import pygame


class Ant:
    def __init__(self, x, y, pygame_width, pygame_height, nest: int):
        self.cords = [x, y]
        self.target = [random.randint(0, pygame_width), random.randint(0, pygame_height)]

        # 0 = no food, 1 = having food, 2 = seeing food, 3 = seeing home
        self.having_food = 0

        self.pheromone_time = 0
        self.distance = 0
        self.pygame_width = pygame_width
        self.pygame_height = pygame_height
        # Which nest the ant belongs to
        self.nest = nest

        self.search_radius = 31


    def move(self):
        if self.target[0] > self.cords[0]:
            self.cords[0] += 1
        elif self.target[0] < self.cords[0]:
            self.cords[0] -= 1
        if self.target[1] > self.cords[1]:
            self.cords[1] += 1
        elif self.target[1] < self.cords[1]:
            self.cords[1] -= 1

        if self.target == self.cords:
            self.target = [random.randint(0, self.pygame_width), random.randint(0, self.pygame_height)]

        self.distance += 1

    def testing_searching(self, object: list):
        if (self.cords[0] + 5 >= object[0] >= self.cords[0] - 5 and
                self.cords[1] + 5 >= object[1] >= self.cords[1] - 5):
            return True
        return False

    def smelling_pheromones(self, pheromones: list):
        smallest_pheromone_distance = 1000000

        for pheromone in pheromones:
            if self.testing_searching(pheromone.cords) and pheromone.pheromone_distance < smallest_pheromone_distance:
                smallest_pheromone_distance = pheromone.pheromone_distance
                self.target = [pheromone.cords[0] + random.randint(-10, 10), pheromone.cords[1] + random.randint(-10, 10)]

    def seeing_objects(self, object: list):
        if (self.cords[0] + self.search_radius*2 >= object[0] >= self.cords[0] - self.search_radius*2 and
                self.cords[1] + self.search_radius*2 >= object[1] >= self.cords[1] - self.search_radius*2):
            return True
        return False

    '''def sensoring_pheromones(self, pheromones: list):
        checking_rect = pygame.Rect(self.cords[0], self.cords[1]-30, 70, 70)
        smallest_pheromone = 1000000

        for i in pheromones:
            if self.cords[0] + 31 >= i.rect.x >= self.cords[1] - 31:
                if checking_rect.colliderect(i.rect) is True and i.distance_from_nest < smallest_pheromone and i.nest == self.nest:
                    smallest_pheromone = i.distance_from_nest
                    self.target = (i.rect.x + random.randint(-10, 10), i.rect.y + random.randint(-10, 10))'''
