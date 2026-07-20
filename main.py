import pygame
import asteroid
from player import Player
from asteroid import Asteroid
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
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

        pygame.display.flip()

        #limits frame rate to 60FPS
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
