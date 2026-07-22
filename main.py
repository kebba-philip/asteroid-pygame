from doctest import DocTestFailure

import pygame
import asteroid
import asteroidfield
from player import Player
from asteroid import Asteroid
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, LINE_WIDTH
from logger import log_state, log_event
from asteroidfield import AsteroidField
import sys
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    clock = pygame.time.Clock()
    dt = 0.0

    while True:
        log_state()

        #handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        for obj in asteroids:
            if obj.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            for shot in shots:
                if obj.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    obj.kill()






        pygame.display.flip()

        #limits frame rate to 60FPS
        dt = clock.tick(60) / 1000

        if player.update:
            player.timer -= dt



if __name__ == "__main__":
    main()
