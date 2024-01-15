from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    """
    A class representing the user interface for the quiz application.

    Attributes:
    - quiz (QuizBrain): An instance of the QuizBrain class.
    - window (Tk): The main window of the application.
    - score_label (Label): A label displaying the user's score.
    - canvas (Canvas): A canvas for displaying quiz questions.
    - question_text (int): The text object on the canvas for displaying questions.
    - true_button (Button): A button for selecting the 'True' answer.
    - false_button (Button): A button for selecting the 'False' answer.
    """

    def __init__(self, quiz_brain: QuizBrain):
        """
        Initializes a new QuizInterface instance.

        Parameters:
        - quiz_brain (QuizBrain): An instance of the QuizBrain class.
        """
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(
            text=f"Score: 0",
            fg="white",
            bg=THEME_COLOR,
            font=("Arial", 20, "bold")
        )
        self.score_label.grid(row=0, column=1, sticky="E")

        self.canvas = Canvas(width=500, height=400, bg="white")
        self.question_text = self.canvas.create_text(
            250,
            200,
            width=480,
            text="question:",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1, sticky="S")
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """
        Retrieves the next question from the QuizBrain and updates the user interface.
        """
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        """
        Handles the 'True' button press and provides feedback.
        """
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        """
        Handles the 'False' button press and provides feedback.
        """
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        """
        Provides visual feedback based on the correctness of the answer.

        Parameters:
        - is_right (bool): True if the answer is correct, False otherwise.
        """
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
