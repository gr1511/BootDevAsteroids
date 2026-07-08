import pygame
from constants import *
from logger import log_state
from player import *
from asteroid import *
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids with pygame version:" + pygame.version.ver)
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))
    pygame.init() 
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    AsteroidField.containers = (updatable)    
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for i in drawable:
            i.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0


if __name__ == "__main__":
    main()
