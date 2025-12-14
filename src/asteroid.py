import pygame
import random
from logger import log_event
from src.circleshape import CircleShape
from src.constants import ASTEROID_MIN_RADIUS, ASTEROID_SPLIT_VELOCITY_MULTIPLIER, LINE_WIDTH


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: return

        log_event("asteroid_split")

        angle_value = random.uniform(20, 50)
        angle_one = self.velocity.rotate(angle_value)
        angle_two = self.velocity.rotate(- angle_value)

        radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_one = Asteroid(self.position[0],self.position[1], radius)
        asteroid_one.velocity = angle_one * ASTEROID_SPLIT_VELOCITY_MULTIPLIER

        asteroid_two = Asteroid(self.position[0],self.position[1], radius)
        asteroid_two.velocity = angle_two * ASTEROID_SPLIT_VELOCITY_MULTIPLIER


