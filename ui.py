from tkinter import *
THEME_COLOR = "#375362"

class QuizGUI:

    def __init__(self, current_score, question):
        self.root = Tk()
        self.root.title('QuizApp')
        self.root.config(padx= 20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f'Score: {current_score}', bg=THEME_COLOR, fg='white', font=('Arial', 15, 'italic'))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas.create_text(150, 75, text=question, font=('Arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2)


        false_img = PhotoImage(file='images/false.png')
        self.left_button = Button(image=false_img, highlightthickness=0,)
        self.left_button.grid(row=2, column=0)

        true_img = PhotoImage(file='images/true.png')
        self.right_button = Button(image=true_img, highlightthickness=0,)
        self.right_button.grid(row=2, column=1)
        self.root.mainloop()