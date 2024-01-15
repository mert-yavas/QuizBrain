import html

class QuizBrain:
    """
    A class representing the brain of the quiz application.

    Attributes:
    - question_number (int): The current question number.
    - score (int): The user's score in the quiz.
    - question_list (list): A list containing Question objects.
    - current_question (Question): The current Question object being presented.
    """

    def __init__(self, q_list):
        """
        Initializes a new QuizBrain instance.

        Parameters:
        - q_list (list): A list containing Question objects.
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """
        Checks if there are more questions in the quiz.

        Returns:
        - bool: True if there are more questions, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Retrieves the next question in the quiz.

        Returns:
        - str: The formatted text of the next question.
        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        """
        Checks if the user's answer is correct and updates the score.

        Parameters:
        - user_answer (str): The user's answer to the current question.

        Returns:
        - bool: True if the answer is correct, False otherwise.
        """
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
