import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def is_collide(self, another_circle):
        distance = pygame.math.Vector2.distance_to(
            self.position, another_circle.position
        )
        collided = distance < (self.radius + another_circle.radius)
        return collided
