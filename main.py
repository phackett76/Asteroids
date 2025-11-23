import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from logger import log_state


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    Player_1 = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        Player_1.update(dt)    
        
        screen.fill("black")
        Player_1.draw(screen)
        pygame.display.flip()
        
        # Framerate limiter - 60 FPS
        dt = clock.tick(60) / 1000

# print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
# print(f"Screen width: {SCREEN_WIDTH}")
# print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()

