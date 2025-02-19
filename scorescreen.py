import pygame
from constants import SCORE_HEIGHT, SCORE_WIDTH, HEALTH_WIDTH, HEALTH_HEIGHT, HEALTH_RADIUS

class ScoreScreen:
    def __init__(self, screen):
        self.screen = screen
        self.score_x, self.score_y = SCORE_WIDTH, SCORE_HEIGHT
        self.health_x, self.health_y = HEALTH_WIDTH, HEALTH_HEIGHT
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
        self.rotation = 0
        self.radius = HEALTH_RADIUS

    def triangle(self, current_hp):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = pygame.Vector2(self.health_x + (current_hp * 10), self.health_y) + forward * self.radius
        b = pygame.Vector2(self.health_x + (current_hp * 10), self.health_y) - forward * self.radius - right
        c = pygame.Vector2(self.health_x + (current_hp * 10), self.health_y) - forward * self.radius + right
        return [a, b, c]

    def draw(self, current_points, current_hp):
        score_text = "SCORE: " + str(current_points)
        score_surface = self.font.render(score_text, True, (255, 255, 255))
        self.screen.blit(score_surface, (self.score_x, self.score_y))

        for i in range(0, current_hp):
            pygame.draw.polygon(self.screen, (255,255,255), self.triangle(i*4), 2)