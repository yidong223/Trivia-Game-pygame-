import pygame
import pygame.locals

from .base import PygameController


class QuestionController(PygameController):
    """Question controller: Checks if user answer is correct, calculates score based on how fast user answers"""

    def __init__(self, question_ins, question_view):
        """Constructor - sets variables"""
        super().__init__(question_view)
        self.question_ins = question_ins
        self.start = question_view.start # start time for current question
        self.score = 0

    def process(self, event):
        """Runs game logic - check if answer is correct, calculate score"""
        running = super().process(event)

        if running is False:
            return False

        correct_ans = self.question_ins.answer_id

        if event.type in (pygame.locals.KEYDOWN, pygame.locals.KEYUP):
            
            now = pygame.time.get_ticks() # time when user presses key
            elapsed = (now - self.start) / 1000 # divide by 1000 since milliseconds

            if event.key == pygame.locals.K_1: # check key pressed and compare with correct answer id
                if correct_ans == 1:
                    if elapsed < 10:
                        self.score += round((int(self.question_ins.difficulty) * (2000/elapsed - 19 * elapsed)))
                    else:
                        self.points += 10
                return False
            elif event.key == pygame.locals.K_2: # check key pressed and compared with correct index
                if correct_ans == 2:
                    if elapsed < 10:
                        self.score += round((int(self.question_ins.difficulty) * (2000/elapsed - 19 * elapsed)))
                    else:
                        self.points += 10
                return False
            elif event.key == pygame.locals.K_3: # check key pressed and compared with correct index
                if correct_ans == 3:
                    if elapsed < 10:
                        self.score += round((int(self.question_ins.difficulty) * (2000/elapsed - 19 * elapsed)))
                    else:
                        self.points += 10
                return False
            elif event.key == pygame.locals.K_4: # check key pressed and compared with correct index
                if correct_ans == 4:
                    if elapsed < 10:
                        self.score += round((int(self.question_ins.difficulty) * (2000/elapsed - 19 * elapsed)))
                    else:
                        self.points += 10
                return False

        return True
