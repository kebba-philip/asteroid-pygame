import pygame
from player import Player
from asteroid import Asteroid
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from asteroidfield import AsteroidField
import sys
from shot import Shot
from scoreboard import Scoreboard
from gamestate import GameState

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
    scoreboard = Scoreboard()
    game_state = GameState()

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

        scoreboard.draw(screen)
        scoreboard.draw_lives(screen, game_state.lives)


        for asteroid in asteroids:
            if asteroid.collides_with(player) and player.invincible_timer <= 0:
                game_state.lose_life()

                if game_state.is_game_over():
                    print("Game Over!")
                    sys.exit()

                player.respawn()
                break

            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    scoreboard.add_score(10)
                    asteroid.split()

        pygame.display.flip()

        #limits frame rate to 60FPS
        dt = clock.tick(60) / 1000

        if player.update:
            player.timer -= dt


if __name__ == "__main__":
    main()
