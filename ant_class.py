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
        if (self.cords[0] + self.search_radius * 2 >= object[0] >= self.cords[0] - self.search_radius * 2 and
                self.cords[1] + self.search_radius * 2 >= object[1] >= self.cords[1] - self.search_radius * 2):
            return True
        return False

    def smelling_pheromones(self, pheromones: list):
        smallest_pheromone_distance = 1000000

        for pheromone in pheromones:
            if self.testing_searching([pheromone.rect.x, pheromone.rect.y]) and pheromone.pheromone_distance < smallest_pheromone_distance:
                smallest_pheromone_distance = pheromone.pheromone_distance
                self.target = [pheromone.rect.x + random.randint(-10, 10), pheromone.rect.y + random.randint(-10, 10)]

    def seeing_objects(self, object: list):
        if (self.cords[0] + 5 >= object[0] >= self.cords[0] - 5 and
                self.cords[1] + 5 >= object[1] >= self.cords[1] - 5):
            return True
        return False
