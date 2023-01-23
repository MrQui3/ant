import random
import pygame


class Ant:
    def __init__(self, x, y, pygame_width, pygame_height):
        self.ant = pygame.Rect(x, y, 10, 10)
        self.target = (random.randint(0, pygame_width), random.randint(0, pygame_height))
        # 0 = no food, 1 = having food, 2 = seeing food, 3 = seeing home
        self.having_food = 0
        self.pheromone_time = 0
        self.dected = 0


    def sensoring_pheromones(self, food_pheromones: list):
        left = pygame.Rect(self.ant.x-30, self.ant.y-20, 30, 40)
        above = pygame.Rect(self.ant.x-20, self.ant.y-30, 40, 30)
        right = pygame.Rect(self.ant.x+20, self.ant.y-30, 30, 40)
        below = pygame.Rect(self.ant.x-20, self.ant.y-20, 40, 30)
        density = [0, 0, 0, 0, 0, 0, 0, 0]
        # the position of random food in this rect
        left_above_food = (0, 0)
        left_food = (0, 0)
        left_below_food = (0, 0)
        right_food = (0, 0)
        right_below_food = (0, 0)
        right_above_food = (0, 0)
        above_food = (0, 0)
        below_food = (0, 0)


        for i in food_pheromones:
            if left.colliderect(i.rect) is True:
                if above.colliderect(i.rect) is True:
                    density[0] += i.time
                    left_above_food = (i.rect.x, i.rect.y)
                    break
                elif below.colliderect(i.rect) is True:
                    density[6] += i.time
                    left_below_food = (i.rect.x, i.rect.y)
                    break
                density[7] += i.time
                left_food = (i.rect.x, i.rect.y)
                break
            if above.colliderect(i.rect) is True:
                if right.colliderect(i.rect) is True:
                    density[2] += i.time
                    right_above_food = (i.rect.x, i.rect.y)
                    break
                density[1] += i.time
                above_food = (i.rect.x, i.rect.y)
                break
            if right.colliderect(i.rect) is True:
                if below.colliderect(i.rect) is True:
                    density[4] += i.time
                    right_below_food = (i.rect.x, i.rect.y)
                    break
                density[3] += i.time
                right_food = (i.rect.x, i.rect.y)
                break
            if below.colliderect(i.rect) is True:
                density[5] += i.time
                below_food = (i.rect.x, i.rect.y)
                break
        for i in range(len(density)):
            if max(density) == density[i] and density[i] != 0 and i == 0:
                self.target = left_above_food
            if max(density) == density[i] and density[i] != 0 and i == 1:
                self.target = above_food
            if max(density) == density[i] and density[i] != 0 and i == 2:
                self.target = right_above_food
            if max(density) == density[i] and density[i] != 0 and i == 3:
                self.target = right_food
            if max(density) == density[i] and density[i] != 0 and i == 4:
                self.target = right_below_food
            if max(density) == density[i] and density[i] != 0 and i == 5:
                self.target = below_food
            if max(density) == density[i] and density[i] != 0 and i == 6:
                self.target = left_below_food
            if max(density) == density[i] and density[i] != 0 and i == 7:
                self.target = left_food

