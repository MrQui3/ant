import math

import pygame
import ant
import home
import pheromone_home
import pheromone_food

# Creating simulation variables
ants = []
FPS = 25
width = 900
height = 900
ant_number = 120
food_cords = (100, 100)
food_number = 100
food = []
walls = []
home_pheromones = []
food_pheromones = []

# Creating pygame variables
pygame.init()
screen = pygame.display.set_mode([width, height], pygame.RESIZABLE)
clock = pygame.time.Clock()

# Creating Ants
for i in range(ant_number):
    ants.append(ant.Ant())

# Creating Walls
for wall in home.walls:
    walls.append(pygame.Rect(wall[0] * 20, wall[1] * 20, 20, 20))
# Adding edges to walls
walls.append(pygame.Rect(0, 0, width, 10))
walls.append(pygame.Rect(0, 0, 10, height))
walls.append(pygame.Rect(width - 10, 0, 10, height))
walls.append(pygame.Rect(0, height - 10, width, 10))

# Creating Food
for i in range(round(math.sqrt(food_number))):
    for i2 in range(round(math.sqrt(food_number))):
        food.append(pygame.Rect(food_cords[0] + i, food_cords[1] + i2, 5, 5))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((219, 149, 44))
    clock.tick(FPS)

    # Drawing Home
    pygame.draw.rect(screen, (100, 66, 17), (home.home.x, home.home.y, home.home.size[0], home.home.size[1]))

    # Drawing Walls
    for wall in walls:
        pygame.draw.rect(screen, (61, 54, 43), wall)

    # Drawing Food
    for i in food:
        pygame.draw.rect(screen, (0, 255, 0), i)

    # home_pheromones
    for i in home_pheromones:
        pygame.draw.rect(screen, (0, 0, 255), i.rect)
        i.time -= 1
    home_pheromones = [x for x in home_pheromones if x.time != 0]

    # food_pheromones
    for i in food_pheromones:
        pygame.draw.rect(screen, (45, 112, 0), i.rect)
        i.time -= 1
    food_pheromones = [x for x in food_pheromones if x.time != 0]

    # Ants
    for ant in ants:
        # Drawing Ants
        pygame.draw.rect(screen, (255, 0, 0), ant.ant)
        # Moving Ants
        if ant.target[0] > 0:
            ant.ant.move_ip(1, 0)
            ant.target = (ant.target[0] - 1, ant.target[1])
        elif ant.target[0] < 0:
            ant.ant.move_ip(-1, 0)
            ant.target = (ant.target[0] + 1, ant.target[1])
        if ant.target[1] > 0:
            ant.ant.move_ip(0, 1)
            ant.target = (ant.target[0], ant.target[1] - 1)
        elif ant.target[1] < 0:
            ant.ant.move_ip(0, -1)
            ant.target = (ant.target[0], ant.target[1] + 1)

        if ant.target == (0, 0):
            ant.new_target()

        # Testing if Ant collides
        if ant.ant.collidelist(walls) != -1:
            ant.target = (-ant.target[0], -ant.target[1])
        if ant.ant.collidelist(food) != -1 and ant.having_food == 2:
            food.pop(ant.ant.collidelist(food))
            ant.having_food = 1
            ant.target = (-ant.target[0], -ant.target[1])
        if ant.ant.colliderect(home.home) is True and ant.having_food == 3:
            ant.having_food = 0
            print(len(food))
            ant.sensoring_pheromones(food_pheromones)

        # spreading pheromones
        if ant.pheromone_time == 0:
            if ant.having_food == 1 or ant.having_food == 3:
                food_pheromones.append(pheromone_food.pheromone(ant.ant.x, ant.ant.y))
            if ant.having_food == 0 or ant.having_food == 2:
                home_pheromones.append(pheromone_home.pheromone(ant.ant.x, ant.ant.y))
            ant.pheromone_time = 5
        ant.pheromone_time -= 1

        # Sensoring pheromones
        if ant.having_food == 0 and ant.dected == 0:
            ant.sensoring_pheromones(food_pheromones)
        elif ant.having_food == 1 and ant.dected == 0:
            ant.sensoring_pheromones(home_pheromones)

        # seeing food
        rect = pygame.Rect(ant.ant.x-20, ant.ant.y-20, 50, 50)
        if rect.collidelist(food) != -1 and (ant.having_food == 0 or ant.having_food == 2):
            ant.having_food = 2
            ant.directionr((food[rect.collidelist(food)].x, food[rect.collidelist(food)].y))
        if rect.colliderect(home.home) is True and (ant.having_food == 1 or ant.having_food == 3):
            ant.having_food = 3
            ant.directionr((home.home.x, home.home.y))


    pygame.display.flip()
pygame.quit()
