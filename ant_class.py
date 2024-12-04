import random
import math


class Ant:
    def __init__(self, x, y, pygame_width, pygame_height, nest: int):
        self.cords = [x, y]
        self.size = [5, 10]

        # 0 = no food, 1 = having food, 2 = seeing food, 3 = seeing home
        self.having_food = 0

        self.pheromone_time = 0
        # Distance from nest/food
        self.distance = 0

        self.last_pheromone_distance = math.inf

        self.pygame_width = pygame_width
        self.pygame_height = pygame_height
        # Which nest the ant belongs to
        self.nest = nest

        self.search_radius = 31

        self.target = self.new_target()

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
            self.target = self.new_target()

        self.distance += 1

    def testing_searching(self, object: list):
        if (self.cords[0] + self.search_radius * 2 >= object[0] >= self.cords[0] - self.search_radius * 2 and
                self.cords[1] + self.search_radius * 2 >= object[1] >= self.cords[1] - self.search_radius * 2):
            return True
        return False

    def smelling_pheromones(self, pheromones: list):
        shortest_pheromone_time = math.inf
        for pheromone in pheromones:
            if self.testing_searching([pheromone.rect.x, pheromone.rect.y]) and pheromone.pheromone_distance < self.last_pheromone_distance:
                self.last_pheromone_distance = pheromone.pheromone_distance
                self.target = [pheromone.rect.x + random.randint(-30, 30), pheromone.rect.y + random.randint(-30, 30)]


    def colliding_objects(self, object: list, object_size: list):
        x1_min, y1_min = self.cords[0], self.cords[1]
        x1_max, y1_max = x1_min + self.size[0], y1_min + self.size[1]
        x2_min, y2_min = object[0], object[1]
        x2_max, y2_max = x2_min + object_size[0], y2_min + object_size[1]

        return not (x1_max < x2_min or x1_min > x2_max or y1_max < y2_min or y1_min > y2_max)

    def new_target(self):
        target = [self.cords[0] + random.randint(-100, 100), self.cords[1] + random.randint(-100, 100)]
        if target[0] > self.pygame_width:
            target[0] = self.pygame_width
        elif target[0] < 0:
            target[0] = 0
        if target[1] > self.pygame_height:
            target[1] = self.pygame_height
        elif target[1] < 0:
            target[1] = 0

        return target
