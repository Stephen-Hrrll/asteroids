import random
import pygame
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt      
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20.0, 50.0)
        right_vector = self.velocity.rotate(angle)
        left_vector = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        self_x = self.position.x
        self_y = self.position.y

        left = Asteroid(self_x, self_y, new_radius)
        left.velocity = left_vector * 1.2
        right = Asteroid(self_x,  self_y, new_radius)
        right.velocity = right_vector

