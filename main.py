import pygame, sys
from constants import * # SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_state, log_event


def main():
    # Initialisation
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Setup Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    
    # Create Player
    player_1 = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    # Create Asteroid Field
    asteroid_field = AsteroidField()
    
    # Main game loop
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        for roid in asteroids:
            for shot in shots:
                if roid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    roid.split()

        for roid in asteroids:
            if roid.collides_with(player_1):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        
        # Framerate limiter - 60 FPS
        dt = clock.tick(60) / 1000

# print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
# print(f"Screen width: {SCREEN_WIDTH}")
# print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()

