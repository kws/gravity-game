import sys

import pygame
import time

from . import constants as c
from .body import Body

# Initialization
pygame.init()
screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
pygame.display.set_caption("Orbital Mechanics Simulator")
clock = pygame.time.Clock()

text_font = pygame.font.Font(None, 12)  # Default font and size 24

cx, cy = c.WIDTH // 2, c.HEIGHT // 2

bodies = [
    Body(cx, cy, 0, 0, 1e24, 20, c.BLUE),  # Example body
    Body(cx, cy - 100, 200, 0, 1e22, 10, c.RED),  # Example smaller body
    Body(cx, cy - 150, 180, 0, 1e22, 10, c.RED),  # Example smaller body
    Body(cx, cy - 130, 150, 0, 1e22, 10, c.RED),  # Example smaller body
]


# Game loop
def main():
    running = True
    dt = 1 / c.FPS
    scale_factor = 1 / 100_000

    while running:
        loop_start = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        screen.fill(c.WHITE)
        while time.time() - loop_start < dt:
            for body in bodies:
                body.update_velocity(bodies, scale_factor)
            for body in bodies:
                body.update_position(scale_factor)

        for body in bodies:
            body.draw(screen)

        pygame.display.flip()
        # clock.tick(c.FPS)

    pygame.quit()
    sys.exit()
