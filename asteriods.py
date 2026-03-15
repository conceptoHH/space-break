import pygame
import random
from constants import *
from logger import log_event
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self,screen):
        return pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self,dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rdm_ang = random.uniform(20,50)
        a1 = self.velocity.rotate(rdm_ang)
        a2 = self.velocity.rotate(-rdm_ang)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        ast1 = Asteroid(self.position.x,self.position.y, new_radius)
        ast2 = Asteroid(self.position.x,self.position.y, new_radius)

        ast1.velocity = a1 * 1.2
        ast2.velocity = a2 * 1.2
