# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from constants import *
from scorescreen import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    current_score = 0
    current_hp = 3
    score_screen = ScoreScreen(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))
        score_screen.draw(current_score, current_hp)
        for object in drawable:
            object.draw(screen)
        updatable.update(dt)
        for ast in asteroids:
            if ast.check_collision(player):
                if current_hp > 0:
                    current_hp -= 1
                    for object in asteroids:
                        object.kill()
                else:
                    exit("Game over!")
            for sh in shots:
                if sh.check_collision(ast):
                    sh.kill()
                    ast.split()
                    current_score += 100
        pygame.display.flip()
        dt = clock.tick(60.0) / 1000

if __name__ == "__main__":
    main()
