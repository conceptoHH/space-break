import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(CircleShape):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.cd = 0

        super().__init__(x,y,PLAYER_RADIUS)

        self.rotation = 0

        # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self,screen):
        return pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()


        #MOVING
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        #SHOOTING
        if keys[pygame.K_SPACE]:
            if  self.cd > 0:
                pass
            self.cd = PLAYER_SHOOT_COOLDOWN_SECONDS
            self.shoot()
        self.cd -= dt

    def move(self, dt):
        uv = pygame.Vector2(0,1)
        rotated = uv.rotate(self.rotation)
        rotated_with_speed = rotated * PLAYER_SPEED * dt
        self.position += rotated_with_speed

    def shoot(self):
        s = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        v2 = pygame.Vector2(0,1)
        v2_rotated = v2.rotate(self.rotation)
        v2_rotated_speed = v2_rotated * PLAYER_SHOT_SPEED
        s.velocity = v2_rotated_speed
