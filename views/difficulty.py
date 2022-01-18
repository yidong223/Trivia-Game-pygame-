import pygame

from .base import PygameView


class DifficultyView(PygameView):
    """Screen to let user choose difficulty - given 3 buttons/shapes to press"""
    def __init__(self, window):
        """Constructor - sets variables, inherits window from parent"""
        super().__init__(window)

    def draw(self):
        """Draws each shape, shapes saved to view for use in collision detection in controller"""
        self.button1 = pygame.draw.circle(self.window, (0, 255, 0), (150, 100), 50)
        self.button2 = pygame.draw.polygon(self.window,(255,255,0), points=[(100,300), (150,200), (200, 300)])
        self.button3 = pygame.draw.rect(self.window, (255, 0, 0), (100, 350, 100, 100))
        easy = self.render_text_surface("Easy", 20)
        med = self.render_text_surface("Medium", 20)
        hard = self.render_text_surface("Hard", 20)
        self.window.blit(easy, (250, 90))
        self.window.blit(med, (240, 245))
        self.window.blit(hard, (250, 390))

