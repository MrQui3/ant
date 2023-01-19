import pygame
import random
import ant
import home
import pheromone_home
import pheromone_food

# Creating pygame variables
pygame.init()
width = 600
height = 600
screen = pygame.display.set_mode([width, height], pygame.RESIZABLE)

# Creating simulation variables
ants = []

# Creating Ants
for i in range(50):
    ants.append(ant.Ant())


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))


    # Drawing Ants
    for i in ants:
        pygame.draw.rect(screen, (255, 0, 0), (i.position[0], i.position[1], i.size[0], i.size[1]))
    # Drawing Home
    pygame.draw.rect(screen, (139, 69, 19), (home.pos[0], home.pos[1], home.size[0], home.size[1]))

    pygame.display.flip()
pygame.quit()
