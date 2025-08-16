import sys
import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    pygame.init()

    # Set game screen
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0  # delta time

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    player_shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (player_shots, updatable, drawable)

    player_instance = Player(
        x=constants.SCREEN_WIDTH / 2, y=constants.SCREEN_HEIGHT / 2
    )
    asteroid_field = AsteroidField()

    # Add game loop
    while True:
        # Check if user click close window button and kill the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.is_collide(player_instance):
                print("Game Over!")
                sys.exit()

            for player_shot in player_shots:
                if asteroid.is_collide(player_shot):
                    player_shot.kill()
                    asteroid.kill()

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()  # Update render
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
