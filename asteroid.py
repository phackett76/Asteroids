import pygame, random
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
       super().__init__(x, y, radius)

    def draw(self, screen):
        colour = "white"
        pygame.draw.circle(screen, colour, self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        roid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        roid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        roid_1.velocity = (v1 * 1.2)
        roid_2.velocity = (v2 * 1.2)