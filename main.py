import pygame
import random
import ant
import home
import pheromone_home
import pheromone_food


# Creating simulation variables
ants = []
FPS = 30
width = 600
height = 600


# Creating pygame variables
pygame.init()
screen = pygame.display.set_mode([width, height], pygame.RESIZABLE)
clock = pygame.time.Clock()

# Creating Ants
for i in range(1):
    ants.append(ant.Ant(screen))


rect = pygame.Rect(400, 400, 5, 10)
# define a surface (RECTANGLE)
image_orig = pygame.Surface((100 , 100))
# for making transparent background while rotating an image
image_orig.set_colorkey((0, 0, 0))
# fill the rectangle / surface with green color
image_orig.fill((0, 255, 0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    clock.tick(FPS)

    # making a copy of the old center of the rectangle
    old_center = rect.center
    # defining angle of the rotation
    rot = (0 + 20) % 360
    # rotating the orignal image
    new_image = pygame.transform.rotate(image_orig, rot)
    rect = new_image.get_rect()
    # set the rotated rectangle to the old center
    rect.center = old_center
    # drawing the rotated rectangle to the screen
    screen.blit(new_image, rect)

    # Drawing Ants
    for ant in ants:
        pygame.draw.rect(screen, ant.color, (ant.position[0], ant.position[1], ant.size[0], ant.size[1]))
    # Drawing Home
    pygame.draw.rect(screen, (139, 69, 19), (home.pos[0], home.pos[1], home.size[0], home.size[1]))

    pygame.display.flip()
pygame.quit()
