from question_model import Question  # Import the Question class
from data import question_data  # Import the question data
from quiz_brain import QuizBrain  # Import the QuizBrain class
from ui import QuizInterface  # Import the QuizInterface class

# Create an empty list to store Question objects
question_bank = []

# Iterate through the question data and create Question objects
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Create an instance of the QuizBrain class with the question bank
quiz = QuizBrain(question_bank)

# Create an instance of the QuizInterface class with the QuizBrain instance
quiz_ui = QuizInterface(quiz)

# Uncomment the following lines if you want to run the quiz in console mode
# while quiz.still_has_questions():
#     quiz.next_question()

# Display the final score after completing the quiz
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
