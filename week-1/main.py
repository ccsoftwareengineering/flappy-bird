import sys
import pygame
from pygame.locals import *

RESIZE_FACTOR = 0.8


# Compatability with smaller screens
def size_image(image: pygame.Surface):
    global RESIZE_FACTOR
    return pygame.transform.scale(image, (image.get_width() * RESIZE_FACTOR, image.get_height() * RESIZE_FACTOR))


pygame.init()

# Downsize or upsize screen based on resize factor
screen_width = 864 * RESIZE_FACTOR
screen_height = 936 * RESIZE_FACTOR

# Initialize screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

# Clock to cap FPS
clock = pygame.time.Clock()

# Define game variables
ground_scroll = 0
scroll_speed = 4 * RESIZE_FACTOR

# Load images
background = size_image(pygame.image.load('images/background.png'))
ground = size_image(pygame.image.load('images/ground.png'))

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw background and ground
    screen.blit(background, (0, 0))
    screen.blit(ground, (ground_scroll, screen_height - ground.get_height()))

    # Make ground scroll left
    ground_scroll -= scroll_speed

    # If ground scroll too far left move right, so it appears to keep moving left
    if ground_scroll < -35 * RESIZE_FACTOR:
        ground_scroll = 0

    # Draw all changes to screen
    pygame.display.update()
    clock.tick(60)
