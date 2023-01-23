import math
import pygame
import ant
import pheromone_home
import pheromone_food
import random

# Creating simulation variables
ants = []
FPS = 25
width = 900
height = 900
ant_number = 90
food_cords = (100, 250)
food_number = 200
food = []
home_pheromones = []
food_pheromones = []
home = pygame.Rect(200, 400, 25, 25)

# Creating pygame variables
pygame.init()
screen = pygame.display.set_mode([width, height], pygame.RESIZABLE)
clock = pygame.time.Clock()

# Creating Ants
for i in range(ant_number):
    ants.append(ant.Ant(home.x, home.y, 900, 900))

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
    pygame.draw.rect(screen, (100, 66, 17), (home.x, home.y, home.size[0], home.size[1]))


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
        if ant.target[0] > ant.ant.x:
            ant.ant.move_ip(1, 0)
        elif ant.target[0] < ant.ant.x:
            ant.ant.move_ip(-1, 0)
        if ant.target[1] > ant.ant.y:
            ant.ant.move_ip(0, 1)
        elif ant.target[1] < ant.ant.y:
            ant.ant.move_ip(0, -1)

        if ant.target == (ant.ant.x, ant.ant.y):
            ant.target = (random.randint(0, round(width/2)), random.randint(0, round(height/2)))


        # Testing if Ant collides
        if ant.ant.collidelist(food) != -1 and ant.having_food == 2:
            food.pop(ant.ant.collidelist(food))
            ant.having_food = 1
            ant.sensoring_pheromones(home_pheromones)
        if ant.ant.colliderect(home) is True and ant.having_food == 3:
            ant.having_food = 0
            ant.sensoring_pheromones(food_pheromones)
        if ant.ant.x > width:
            ant.target = (random.randint(-width+10, 0), ant.target[1])
        if ant.ant.x > height:
            ant.target = (ant.target[0], random.randint(-height+10, 0))


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
            ant.dected = 10
            ant.sensoring_pheromones(food_pheromones)
        elif ant.having_food == 1 and ant.dected == 0:
            ant.dected = 10
        ant.dected -= 1


        # seeing food
        rect = pygame.Rect(ant.ant.x-50, ant.ant.y-50, 110, 110)
        if rect.collidelist(food) != -1 and (ant.having_food == 0 or ant.having_food == 2):
            ant.having_food = 2
            ant.target = (food[rect.collidelist(food)].x, food[rect.collidelist(food)].y)
        if rect.colliderect(home) is True and (ant.having_food == 1 or ant.having_food == 3):
            ant.having_food = 3
            ant.target = (home.x, home.y)



    pygame.display.flip()
pygame.quit()
