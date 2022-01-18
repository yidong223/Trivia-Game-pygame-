from .base import PygameView


class EndView(PygameView):
    """View when the game is over"""

    def __init__(self, window, score):
        """Constructor - sets variables, inherits window from parent"""
        super().__init__(window)
        self.score = score

    def draw(self):
        """Displays score and exit information"""
        self.window.fill((0,0,0))
        text = self.render_text_surface("Game ended.", 24)
        self.window.blit(text, (225, 40))
       
        score_display = self.render_text_surface(f"Your score is: {self.score}", 24)
        self.window.blit(score_display, (175, 400))

        quit_display = self.render_text_surface(f"Please press ESC or close this window.", 24)
        self.window.blit(quit_display, (100, 500))
