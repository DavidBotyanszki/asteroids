# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import *
from asteroid import *
from asteroidfield import *
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))
        for object in drawable:
            object.draw(screen)
        updatable.update(dt)
        for ast in asteroids:
            if ast.check_collision(player):
                exit("Game over!")
        pygame.display.flip()
        dt = clock.tick(60.0) / 1000

if __name__ == "__main__":
    main()
