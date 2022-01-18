import pygame

from .base import PygameView


class QuestionView(PygameView):
    def __init__(self, window, question_ins):
        """Constructor - sets variables, inherits window from parent"""
        super().__init__(window)
        self.question_ins = question_ins
        self.start = pygame.time.get_ticks() # start time for current question
        self.end = 10000 + self.start # time that is 10s ahead of start time

    def draw(self):
        """Displays question, answers, and countdown timer"""
        self.window.fill((0,0,0))

        #displays question
        question = self.question_ins.question
        print_q = self.render_text_surface(question, 14)
        self.window.blit(print_q, (0, 40))
        
        #displays countdown timer
        countdown = str(int(round((self.end - pygame.time.get_ticks()) / 1000))) 
        countdown_text = self.render_text_surface(countdown, 24)
        self.window.blit(countdown_text, (500, 550))

        #displays answers
        answers = self.question_ins.answers
        answer_pos = 100
        for index, answer in enumerate(answers):
            print_a = self.render_text_surface(f"{index+1}.   {answer}", 12)
            self.window.blit(print_a, (0, answer_pos))
            answer_pos += 30

    
        

    