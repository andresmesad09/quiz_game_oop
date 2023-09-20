# TODO: Asking questions
# TODO: Checking if the answer is correct
# TODO: Checking if we're at the end of the quiz

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.questions_list = question_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.questions_list):
            return True
        return False

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False)")
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score: {self.score}/{self.question_number}")
        print("\n")

    def close_quiz(self):
        text = f"""
        You've completed the quiz.
        Your final score is {self.score}/{self.question_number}
        """
        print(text)