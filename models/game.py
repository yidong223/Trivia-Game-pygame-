from html import unescape
import requests

from .question import Question
from controllers import QuestionController
from views import QuestionView


class Game:
    """Game class, runs the game when instantiated"""
    def __init__(self, number_of_questions, difficulty=None, category_id=None, pygame_window=None):
        self.score = 0
        self.questions = list()
        self.difficulty = difficulty
        options = {
            "amount" : number_of_questions,
            "type": "multiple"
        }

        if difficulty in ("easy", "medium", "hard"):
            options.update(difficulty=difficulty)

        if category_id:
            try:
                category_id = int(category_id)
                options.update(category=category_id)
            except TypeError or ValueError:
                pass
    
        response = requests.get("https://opentdb.com/api.php", params=options)

        if number_of_questions == 1 and response.json()["results"] == []:
            pass
        else:
            for num in range(number_of_questions):
                incorrect = []
                question = unescape(response.json()["results"][num]["question"])
                correct = unescape(response.json()["results"][num]["correct_answer"])
                for answer in response.json()["results"][num]["incorrect_answers"]:
                    incorrect.append(unescape(answer))
                self.questions.append(Question(question, correct, incorrect, self.difficulty))

        for question in self.questions: # run each question
            question_view = QuestionView(pygame_window, question)
            question_ctrl = QuestionController(question, question_view)
            question_ctrl.run(stop_after=10) # runs one question
            self.score += question_ctrl.score # adds score from each individual question to overall game score

