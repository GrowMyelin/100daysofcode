from mimetypes import init


class QuizBrain:
    def __init__(self,q_list) -> None:
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        ans = input(f"Q.{self.question_number + 1} {current_question.text} (True/False?) ")
        if ans == current_question.answer:
            print('Correct!')
            self.score += 1
        else:
            print('Incorrect.')
        self.question_number += 1
        print(f"Current score is {self.score} / {self.question_number}.")
    
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
