from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizGUI:

    def __init__(self, current_score, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.root = Tk()
        self.root.title('QuizApp')
        self.root.config(padx= 20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f'Score: {current_score}', bg=THEME_COLOR, fg='white', font=('Arial', 15, 'italic'))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=275, text='Question soon', font=('Arial', 18, 'italic'), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        false_img = PhotoImage(file='images/false.png')
        self.left_button = Button(image=false_img, highlightthickness=0, command=self.its_false)
        self.left_button.grid(row=2, column=0)

        true_img = PhotoImage(file='images/true.png')
        self.right_button = Button(image=true_img, highlightthickness=0, command=self.its_true)
        self.right_button.grid(row=2, column=1)

        self.get_question()

        self.root.mainloop()

    def get_question(self):
        self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())

    def its_true(self):
        answer = 'True'
        score = self.quiz.check_answer(answer)

    def its_false(self):
        answer = 'False'
        score = self.quiz.check_answer(answer)
