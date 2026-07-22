from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white",(self.position.x , self.position.y), self.radius, LINE_WIDTH)

    def update(self, dt):
       self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            move = random.uniform(20, 50)
            asteroid1_direction = self.velocity.rotate(move)
            asteroid2_direction = self.velocity.rotate(-move)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid1.velocity = asteroid1_direction * 1.2
            asteroid2.velocity = asteroid2_direction * 1.2
