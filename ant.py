import random
import pygame
import home


class Ant:
    def __init__(self):
        self.ant = pygame.Rect(home.home.x, home.home.y, 10, 10)
        self.target = (random.randint(-200, 200), random.randint(-200, 200))
        self.having_food = False
        self.pheromone_time = 0

    def new_target(self):
        self.target = (random.randint(-200, 200), random.randint(-200, 200))

    def sensoring_food(self, food_pheromones: list):
        left = pygame.Rect(self.ant.x-20, self.ant.y-10, 20, 30)
        above = pygame.Rect(self.ant.x-10, self.ant.y-20, 30, 20)
        right = pygame.Rect(self.ant.x+10, self.ant.y-20, 20, 30)
        below = pygame.Rect(self.ant.x-10, self.ant.y-10, 30, 20)

        for i in food_pheromones:
            if left.colliderect(i.rect) != -1:
                if above.colliderect(i.rect) == left.colliderect(i.rect):
                    self.target = (-40, -40)
                    return 6
                elif below.colliderect(i.rect) == left.colliderect(i.rect):
                    self.target = (-40, +40)
                    return 7
                self.target = (-40, 0)
                return 8
            if above.colliderect(i.rect) != -1:
                if above.colliderect(i.rect) == right.colliderect(i.rect):
                    self.target = (+40, -40)
                    return 3
                self.target = (0, -40)
                return 2
            if right.colliderect(i.rect) != -1:
                if below.colliderect(i.rect) == right.colliderect(i.rect):
                    self.target = (+40, +40)
                    return 5
                self.target = (+40, 0)
                return 4
            if below.colliderect(i.rect) != -1:
                self.target = (0, +40)
