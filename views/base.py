from abc import ABC, abstractmethod

import pygame
import pygame.font


class PygameView(ABC):
    """Abstract class for a basic Pygame view"""

    def __init__(self, window):
        """Constructor receives a window (where everything will be displayed)"""
        self.window = window
        self.start = None

    def render_text_surface(self, text, size):
        """Utility function to render a text surface"""
        arial = pygame.font.SysFont("comicsansms", size) # chose to add in size argument to have different views use different sized fonts
        text_surface = arial.render(text, True, (255, 255, 255))

        return text_surface

    @abstractmethod
    def draw(self):
        """Child classes MUST implement the draw method"""
        raise NotImplementedError

    def update(self):
        """Update the screen"""
        pygame.display.flip()
