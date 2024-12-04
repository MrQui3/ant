import pygame

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Set up font
font = pygame.font.Font(None, 36)  # None for default font, 36 is the font size

# Integer to display
integer_to_display = 123

# Render the text
text = font.render(str(integer_to_display), True, (255, 255, 255))  # White color

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (black)
    screen.fill((0, 0, 0))

    # Blit the text onto the screen
    screen.blit(text, (50, 50))  # Position (50, 50)

    # Update the display
    pygame.display.flip()

# Quit Pygame