from tkinter import *
THEME_COLOR = "#375362"

class QuizGUI:

    def __init__(self, current_score):
        self.root = Tk()
        self.root.title('QuizApp')
        self.root.config(padx= 20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f'Score: {current_score}', bg=THEME_COLOR, fg='white', font=('Arial', 10, 'italic'))
        self.score_label.grid(row=0, column=1)

        self.question_label = Label()
        self.root.mainloop()