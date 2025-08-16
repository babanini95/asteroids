import circleshape
import pygame


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, radius=self.radius, width=2, center=self.position, color="white"
        )

    def update(self, dt):
        self.position += self.velocity * dt
