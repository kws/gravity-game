import math

import pygame

from .constants import G


class Body:
    def __init__(self, x, y, vx, vy, mass, radius, color):
        self.x = x
        self.y = y
        self.vx = vx  # velocity in x-direction
        self.vy = vy  # velocity in y-direction
        self.mass = mass
        self.radius = radius
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def update_velocity(self, bodies, dt):
        for body in bodies:
            if body == self:
                continue

            dx = body.x - self.x
            dy = body.y - self.y

            distance = math.sqrt(dx**2 + dy**2)

            force_mag = G * self.mass * body.mass / distance**2
            force_mag = min(force_mag, 10e22)  # Limit the force to prevent instability

            force_x = force_mag * dx / distance
            force_y = force_mag * dy / distance

            self.vx += force_x / self.mass * dt
            self.vy += force_y / self.mass * dt

    def update_position(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
