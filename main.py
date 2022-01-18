import pygame

from controllers import DifficultyController, EndController
from views import DifficultyView, EndView
from models import Game

def main():
    """Main program"""

    # Initialize pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((600, 600))

    # Initiates difficulty selection
    difficulty_view = DifficultyView(window)
    difficulty_ctrl = DifficultyController(difficulty_view)
    difficulty_ctrl.run()

    # Run the game with 10 questions and selected difficulty
    game = Game(10, difficulty_ctrl.difficulty, pygame_window=window)
    
    # # Create the end view and controller, and run it
    end_view = EndView(window, score=game.score)
    end = EndController(end_view)
    end.run()

if __name__ == "__main__":
    main()
