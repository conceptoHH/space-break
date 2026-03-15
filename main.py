import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state,log_event
from player import Player
from asteriods import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #groups
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()


    #containers
    Shot.containers = (shots, drawable, updatable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)

    af = AsteroidField()
    p = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    #gameloop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for a in asteroids:
            if  a.collides_with(p):
                log_event("player_hit")
                print("GAME OVER")
                sys.exit()
            for shot in shots:
                if shot.collides_with(a):
                    log_event("asteroid_shot")
                    a.split()
                    shot.kill()


        screen.fill("black")

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        dt = clock.tick(10) / 1000

if __name__ == "__main__":
    main()
