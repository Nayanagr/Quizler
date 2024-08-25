THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.score: int
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_text = Label(text=f"Score: {self.quiz.score}", fg="white",bg=THEME_COLOR, font=("Arial", 14))
        self.score_text.grid(row=0, column = 1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.q_text = self.canvas.create_text(
            150,
            125,
            text="Some question",
            fill=THEME_COLOR,
            font=("Arial", 20 ,"italic"),
            width=280
        )

        # Canvas Setup
        self.canvas.grid(row=1,column=0, columnspan =2, pady=50)

        # True button
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image,highlightthickness=0,borderwidth=0,command=self.true_press)
        self.true_button.grid(row=2, column=0)

        # False Button
        false_image= PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0,borderwidth=0,command=self.false_press)
        self.false_button.grid(row=2 , column =1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.q_text, fill=THEME_COLOR)
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.q_text, text =f"You have completed the quiz,\nYou got ({self.quiz.score}/{self.quiz.question_number}) Correct.",fill=THEME_COLOR)
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_press(self):
        is_right =  self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_press(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, condition):
        self.score_text.config(text=f"Score: {self.quiz.score}")
        if condition:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.q_text,fill= "white")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.q_text, fill="white")
        self.window.after(1000, func=self.get_next_question)







