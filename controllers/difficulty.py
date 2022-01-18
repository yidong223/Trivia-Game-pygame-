import pygame.locals

from .base import PygameController


class DifficultyController(PygameController):
    """Difficulty screen controller"""

    def __init__(self, view):
        """Constructor - sets variables, inherits view from parent"""
        super().__init__(view)
        self.difficulty = None

    def process(self, event):
        """
        Lets user clicks in the shape to choose the difficulty of questions.
        """

        running = super().process(event)

        if running is False:
            return False

        # When user clicks
        if event.type == pygame.locals.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos() # Check the click position, if mouse is within shapes (buttons) then set difficulty
            if self.view.button1.collidepoint(mouse_position):
                self.difficulty = "easy"
                return False
            elif self.view.button2.collidepoint(mouse_position):
                self.difficulty = "medium"
                return False
            elif self.view.button3.collidepoint(mouse_position):
                self.difficulty = "hard"
                return False


        return True