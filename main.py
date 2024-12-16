import math
import pygame
from ant_class import Ant
from pheromone import Pheromone
import time


def setting_variables():
    global ants, FPS, width, height, ant_number, food, home_pheromones, food_pheromones, homes, walls, screen, font

    # Creating simulation variables
    ants = []
    FPS = 60
    width = 800
    height = 800
    ant_number = 10
    food = []
    home_pheromones = [[], []]
    food_pheromones = [[], []]
    homes = [[100, 100], [700, 100]]
    walls = []

    # Creating pygame variables
    pygame.init()
    screen = pygame.display.set_mode([width + 5, height + 5], pygame.RESIZABLE)
    pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])
    font = pygame.font.Font(None, 36)  # None for default font, 36 is the font size

    # Creating Ants
    for i in range(round(ant_number / len(homes))):
        ants.append(Ant(homes[0][0], homes[0][1], width, height, 0))
    for i in range(round(ant_number / len(homes))):
        ants.append(Ant(homes[1][0], homes[1][1], width, height, 1))

    # Creating Food
    for i in range(round(math.sqrt(20))):
        for i2 in range(round(math.sqrt(50))):
            food.append([700 + i, 500 + i2])

    for i in range(round(math.sqrt(20))):
        for i2 in range(round(math.sqrt(50))):
            food.append([100 + i, 500 + i2])

    for i in range(round(math.sqrt(50))):
        for i2 in range(round(math.sqrt(100))):
            food.append([400 + i, 700 + i2])

    for i in range(10):
        walls.append([150 + i * 50, 600])


def drawing():
    global home_pheromones, food_pheromones
    screen.fill((219, 149, 44))

    # Drawing Home
    for home in homes:
        pygame.draw.rect(screen, (100, 66, 17), (home[0], home[1], 25, 25))

    # Drawing Walls
    for wall in walls:
        pygame.draw.rect(screen, (36, 35, 35), (wall[0], wall[1], 50, 50))

    # Drawing Food
    for i in food:
        pygame.draw.rect(screen, (0, 255, 0), (i[0], i[1], 5, 5))

    # Drawing home_pheromones
    for i in range(len(home_pheromones)):
        for i2 in home_pheromones[i]:
            if i == 0:
                pygame.draw.rect(screen, (0, 0, 255), i2.rect)
            else:
                pygame.draw.rect(screen, (0, 0, 112), i2.rect)

    # Drawing food_pheromones
    for i in food_pheromones:
        for i2 in i:
            if i == 0:
                pygame.draw.rect(screen, (6, 117, 2), i2.rect)
            else:
                pygame.draw.rect(screen, (2, 109, 117), i2.rect)

    # Drawing Ants
    for ant in ants:
        if ant.nest == 0:
            pygame.draw.rect(screen, (255, 0, 255), (ant.cords[0], ant.cords[1], ant.size[0], ant.size[1]))
        elif ant.nest == 1:
            pygame.draw.rect(screen, (255, 0, 0), (ant.cords[0], ant.cords[1], ant.size[0], ant.size[1]))
        else:
            pygame.draw.rect(screen, (255, 255, 255), (ant.cords[0], ant.cords[1], ant.size[0], ant.size[1]))


def calculating():
    global home_pheromones, food_pheromones

    # Calculating home_pheromones
    for pheromone_types in home_pheromones:
        for pheromone in pheromone_types:
            pheromone.time -= 1
            if pheromone.time == 0:
                pheromone_types.remove(pheromone)

    # Calculating food_pheromones
    for pheromone_types in food_pheromones:
        for pheromone in pheromone_types:
            pheromone.time -= 1
            if pheromone.time == 0:
                pheromone_types.remove(pheromone)

    # Ants
    for ant in ants:

        # testing if ant collides with walls
        is_in_wall = False
        for wall in walls:
            if ant.colliding_objects(wall, [50, 50]):
                ant.target = ant.new_target()
                is_in_wall = True
        if is_in_wall:
            ant.move()
            continue
        ant.move()

        # Testing if Ant sees food_pheromones
        if ant.having_food == 0:
            ant.smelling_pheromones(food_pheromones[ant.nest])

        # Testing if Ant sees home/home_pheromones
        elif ant.having_food == 1:
            if ant.testing_searching(homes[ant.nest]):
                ant.having_food = 3
                ant.target = homes[ant.nest]
            else:
                ant.smelling_pheromones(home_pheromones[ant.nest])

        # Testing if Ant collides/sees with food
        if ant.having_food == 2 or ant.having_food == 0:
            for i in food:
                # Testing if Ant collides with food
                if ant.colliding_objects(i, [5, 5]):
                    food.remove(i)
                    ant.having_food = 1
                    ant.smelling_pheromones(home_pheromones[ant.nest])
                    ant.distance = 0
                    ant.last_pheromone_distance = math.inf
                    break
                # Testing if Ant sees food
                if ant.testing_searching(i):
                    ant.target = i
                    ant.having_food = 2

        # Testing if Ant collides with home
        elif ant.having_food == 3:
            if ant.colliding_objects(homes[ant.nest], [25, 25]):
                ant.distance = 0
                ant.having_food = 0
                ant.last_pheromone_distance = math.inf
                ant.smelling_pheromones(food_pheromones[ant.nest])
                ants.append(Ant(homes[ant.nest][0], homes[ant.nest][1], width, height, ant.nest))

        # spreading pheromones
        if ant.pheromone_time == 0:
            if ant.having_food == 1 or ant.having_food == 3:
                food_pheromones[ant.nest].append(Pheromone(ant.cords, ant.distance))
            if ant.having_food == 0 or ant.having_food == 2:
                home_pheromones[ant.nest].append(Pheromone(ant.cords, ant.distance))
            ant.pheromone_time = 16
            ant.last_pheromone_distance += 0.5
        ant.pheromone_time -= 1
    for i in range(len(home_pheromones)):
        home_pheromones[i].sort(key=lambda x: x.pheromone_distance)
    for i in range(len(food_pheromones)):
        food_pheromones[i].sort(key=lambda x: x.pheromone_distance)


def main():
    setting_variables()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        calculating()
        calculating()
        calculating()
        drawing()
        text = font.render(str(len(ants)), True, (0, 0, 0))
        screen.blit(text, (width / 2 - 30, 50))
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
