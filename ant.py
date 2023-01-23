import random
import pygame
import home


class Ant:
    def __init__(self):
        self.ant = pygame.Rect(home.home.x, home.home.y, 10, 10)
        self.target = (random.randint(-200, 200), random.randint(-200, 200))
        # 0 = no food, 1 = having food, 2 = seeing food, 3 = seeing home
        self.having_food = 0
        self.pheromone_time = 0
        self.dected = 0
        self.direction = 0

    def new_target(self):
        self.target = (random.randint(-200, 200), random.randint(-200, 200))

    def sensoring_pheromones(self, food_pheromones: list):
        left = pygame.Rect(self.ant.x-30, self.ant.y-20, 30, 40)
        above = pygame.Rect(self.ant.x-20, self.ant.y-30, 40, 30)
        right = pygame.Rect(self.ant.x+20, self.ant.y-30, 30, 40)
        below = pygame.Rect(self.ant.x-20, self.ant.y-20, 40, 30)
        density = [0, 0, 0, 0, 0, 0, 0, 0]


        for i in food_pheromones:
            if left.colliderect(i.rect) is True:
                if above.colliderect(i.rect) is True:
                    density[0] += i.time
                    break
                elif below.colliderect(i.rect) is True:
                    density[6] += i.time
                    break
                density[7] += i.time
                break
            if above.colliderect(i.rect) is True:
                if right.colliderect(i.rect) is True:
                    density[2] += i.time
                    break
                density[1] += i.time
                break
            if right.colliderect(i.rect) is True:
                if below.colliderect(i.rect) is True:
                    density[4] += i.time
                    break
                density[3] += i.time
                break
            if below.colliderect(i.rect) is True:
                density[5] += i.time
                break
        for i in range(len(density)):
            if max(density) == density[i] and density[i] != 0 and i == 0 and random.randint(0, 2) == 1:
                self.target = (-40, -40)
                self.direction = 0
            if max(density) == density[i] and density[i] != 0 and i == 1 and random.randint(0, 2) == 1:
                self.target = (0, -40)
                self.direction = 1
            if max(density) == density[i] and density[i] != 0 and i == 2 and random.randint(0, 2) == 1:
                self.target = (+40, -40)
                self.direction = 2
            if max(density) == density[i] and density[i] != 0 and i == 3 and random.randint(0, 2) == 1:
                self.target = (+40, 0)
                self.direction = 3
            if max(density) == density[i] and density[i] != 0 and i == 4 and random.randint(0, 2) == 1:
                self.target = (+40, +40)
                self.direction = 4
            if max(density) == density[i] and density[i] != 0 and i == 5 and random.randint(0, 2) == 1:
                self.target = (0, +40)
                self.direction = 5
            if max(density) == density[i] and density[i] != 0 and i == 6 and random.randint(0, 2) == 1:
                self.target = (-40, +40)
                self.direction = 6
            if max(density) == density[i] and density[i] != 0 and i == 7:
                self.target = (-40, 0)
                self.direction = 7

    def directionr(self, position):
        if self.ant.x > position[0]:
            if self.ant.y > position[1]:
                self.target = (-40, -40)
                return 0
            if self.ant.y < position[1]:
                self.target = (-40, +40)
                return 0
            self.target = (-40, 0)
            return 0
        if self.ant.x < position[0]:
            if self.ant.y > position[1]:
                self.target = (+40, -40)
                return 0
            if self.ant.y < position[1]:
                self.target = (+40, +40)
                return 0
            self.target = (+40, 0)
            return 0
        if self.ant.x == position[0]:
            if self.ant.y > position[1]:
                self.target = (0, -40)
                return 0
            if self.ant.y < position[1]:
                self.target = (0, +40)
                return 0
            return 0

