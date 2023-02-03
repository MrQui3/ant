import math
import pygame
import ant_class
import pheromone_home
import pheromone_food
import random
import time

# Creating simulation variables
ants = []
FPS = 60
width = 800
height = 800
ant_number = 10
food = []
home_pheromones = []
food_pheromones = []
home = [pygame.Rect(100, 100, 25, 25), pygame.Rect(700, 100, 25, 25)]
home_points = [0, 0]
# walls = []

# Creating pygame variables
pygame.init()
screen = pygame.display.set_mode([width, height], pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])

# Creating Ants
for i in range(round(ant_number/len(home))):
    ants.append(ant_class.Ant(home[0].x, home[0].y, width, height, 0))
for i in range(round(ant_number/len(home))):
    ants.append(ant_class.Ant(home[1].x, home[1].y, width, height, 1))

# Creating Food
for i in range(round(math.sqrt(20))):
    for i2 in range(round(math.sqrt(50))):
        food.append(pygame.Rect(700 + i, 500 + i2, 5, 5))

for i in range(round(math.sqrt(20))):
    for i2 in range(round(math.sqrt(50))):
        food.append(pygame.Rect(100 + i, 500 + i2, 5, 5))

for i in range(round(math.sqrt(50))):
    for i2 in range(round(math.sqrt(100))):
        food.append(pygame.Rect(300 + i, 700 + i2, 5, 5))

'''
# Creating walls
walls.append(pygame.Rect(300, 600, 200, 10))
walls.append(pygame.Rect(300, 600, 10, 50))
walls.append(pygame.Rect(500, 600, 10, 50))


ir = 0
for i in range(100):
    ir += 1
    food_pheromones.append(pheromone_food.pheromone(100, 600-i*20, ir))

#Adding food pheromoes
for i in range(15):
    ir += 1
    food_pheromones.append(pheromone_food.pheromone(food_cords[0]+(i*20), home[0].y, ir))'''



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((219, 149, 44))

    # Drawing Home
    for i in home:
        pygame.draw.rect(screen, (100, 66, 17), (i.x, i.y, i.size[0], i.size[1]))
        pygame.draw.rect(screen, (100, 66, 17), (i.x, i.y, i.size[0], i.size[1]))

    '''
    # Drawing Walls
    for i in walls:
        pygame.draw.rect(screen, (36, 35, 35), i)'''

    # Drawing Food
    for i in food:
        pygame.draw.rect(screen, (0, 255, 0), i)

    # Drawing home_pheromones
    for i in home_pheromones:
        if i.nest == 0:
            pygame.draw.rect(screen, (0, 0, 255), i.rect)
        else:
            pygame.draw.rect(screen, (0, 0, 112), i.rect)
        i.time -= 1
    home_pheromones = [x for x in home_pheromones if x.time != 0]

    # Drawing food_pheromones
    for i in food_pheromones:
        if i.nest == 0:
            pygame.draw.rect(screen, (6, 117, 2), i.rect)
        else:
            pygame.draw.rect(screen, (2, 109, 117), i.rect)
        i.time -= 1
    food_pheromones = [x for x in food_pheromones if x.time != 0]



    # Ants
    for ant in ants:
        # Drawing Ants
        if ant.nest == 0:
            pygame.draw.rect(screen, (255, 0, 255), ant.ant)
        elif ant.nest == 1:
            pygame.draw.rect(screen, (255, 0, 0), ant.ant)
        else:
            pygame.draw.rect(screen, (255, 255, 255), ant.ant)
        # Moving Ants
        if ant.target[0] > ant.ant.x:
            ant.ant.move_ip(1, 0)
        elif ant.target[0] < ant.ant.x:
            ant.ant.move_ip(-1, 0)
        if ant.target[1] > ant.ant.y:
            ant.ant.move_ip(0, 1)
        elif ant.target[1] < ant.ant.y:
            ant.ant.move_ip(0, -1)

        if ant.target == (ant.ant.x, ant.ant.y):
            ant.target = (random.randint(0, width), random.randint(0, height))

        # increasing distance form nest/food
        ant.distance += 1

        # Testing if Ant collides
        if ant.ant.collidelist(food) != -1 and ant.having_food == 2:
            food.pop(ant.ant.collidelist(food))
            ant.having_food = 1
            ant.sensoring_pheromones(home_pheromones)
            ant.distance = 0
        if ant.ant.colliderect(home[ant.nest]) is True:
            ant.distance = 0
            if ant.having_food == 3:
                ant.having_food = 0
                ant.sensoring_pheromones(food_pheromones)
                home_points[ant.nest] += 1
                ants.append(ant_class.Ant(home[ant.nest].x, home[ant.nest].y, width, height, ant.nest))
                print(f"home{ant.nest}: {home_points[ant.nest]}")

        if ant.ant.x > width or ant.ant.x < 0:
            ant.target = (random.randint(0, width), ant.target[1])
        if ant.ant.y > height or ant.ant.y < 0:
            ant.target = (ant.target[0], random.randint(0, height))
        '''if ant.ant.collidelist(walls) != -1:
            ant.target = (random.randint(0, width), random.randint(0, height))'''


        # spreading pheromones
        if ant.pheromone_time == 0:
            if ant.having_food == 1 or ant.having_food == 3:
                food_pheromones.append(pheromone_food.pheromone(ant.ant.x, ant.ant.y, ant.distance, ant.nest))
            if ant.having_food == 0 or ant.having_food == 2:
                home_pheromones.append(pheromone_home.pheromone(ant.ant.x, ant.ant.y, ant.distance, ant.nest))
            ant.pheromone_time = 29
        ant.pheromone_time -= 1

        # Sensoring pheromones
        if ant.having_food == 0 or ant.having_food == 2:
            ant.sensoring_pheromones(food_pheromones)

        elif ant.having_food == 1:
            ant.sensoring_pheromones(home_pheromones)


        # seeing food
        rect = pygame.Rect(ant.ant.x-50, ant.ant.y-50, 110, 110)
        if rect.collidelist(food) != -1 and (ant.having_food == 0 or ant.having_food == 2):
            ant.having_food = 2
            ant.target = (food[rect.collidelist(food)].x, food[rect.collidelist(food)].y)
        if rect.colliderect(home[ant.nest]) is True and (ant.having_food == 1 or ant.having_food == 3):
            if ant.having_food == 1:
                ant.having_food = 3
                ant.target = (home[ant.nest].x, home[ant.nest].y)

    pygame.display.flip()
pygame.quit()
