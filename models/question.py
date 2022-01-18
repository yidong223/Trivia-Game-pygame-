import random
from html import unescape

class Question:
    """Question class"""
    def __init__(self, question, correct_answer, incorrect_answers, difficulty=None):
        mapping = {
            "easy" : 1,
            "medium" : 2,
            "hard" : 3
        }

        self.question = unescape(question)
        self.correct_answer = unescape(correct_answer)
        if difficulty == None:
            self.difficulty = mapping["easy"]
        else:
            self.difficulty = mapping[difficulty]

        self.answers = [correct_answer]
        for answer in incorrect_answers:
            self.answers.append(answer)

        random.shuffle(self.answers)

        self.answer_id = self.answers.index(self.correct_answer) + 1


    def get_answers(self):
        display = ""
        for index, answer in enumerate(self.answers):
            display += f"{index+1} {answer}\n"
        
        return display

            
                