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


# Bird sprite
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.counter = 0
        self.index = 0

        for num in range(1, 4):
            self.images.append(size_image(pygame.image.load(f'images/bird{num}.png')))
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    # Updates the bird on each tick/frame
    def update(self):
        self.counter += 1
        flap_cooldown = 5

        # If 5 ticks have passed
        if self.counter > flap_cooldown:
            # Reset count and
            self.counter = 0
            self.index = (self.index + 1) % 3
            self.image = self.images[self.index]


# Although there is one bird, we still create a sprite group
# because it has useful helper functions
bird_group = pygame.sprite.Group()
flappy = Bird(100 * RESIZE_FACTOR, int(screen_height / 2))
bird_group.add(flappy)

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

    # Draw the bird and update
    bird_group.draw(screen)
    bird_group.update()

    # Draw all changes to screen
    pygame.display.update()
    clock.tick(60)
