import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable) #add player to groups
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        screen.fill("black")

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.in_collision(player):
                print("Game over!")
                sys.exit()

            for bullet in shots:
                if asteroid.in_collision(bullet):
                    asteroid.kill()
                    bullet.kill()

                
        for dr in drawable:
            dr.draw(screen)
        # drawable.draw(screen)


        pygame.display.flip()
        dt  = clock.tick(60) / 1000 #convert from milliseconds to seconds


if __name__ == "__main__":
    main()