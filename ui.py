from tkinter import *
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.number_question_answered = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, highlightthickness=0, bg="white")
        self.question = self.canvas.create_text(
            150,
            125,
            width=280,
            text="text goes here",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        check_mark_img = PhotoImage(file="images/true.png")
        x_mark_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=check_mark_img, command=self.true_pressed)
        self.false_button = Button(image=x_mark_img, command=self.false_pressed)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.get_next()

        self.window.mainloop()

    def get_next(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)
            self.canvas.itemconfig(self.question, text=f"End of the quiz, your score is {self.quiz.score}/10")
            self.window.after(2000, self.window.destroy)

    def true_pressed(self):
        self.number_question_answered += 1
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        self.number_question_answered += 1
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}/{self.number_question_answered}")
        else:
            self.canvas.config(bg="red")
            self.score_label.config(text=f"Score: {self.quiz.score}/{self.number_question_answered}")
        self.window.after(1000, self.get_next)
