BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
from tkinter import messagebox
import pandas
import random

timer = None
random_data = None

try:
    df = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    df = pandas.read_csv('data/french_words.csv')
finally:
    code_dict = df.to_dict(orient="records")

def show_answer(data):
    canvas.itemconfig(image, image=card_back_image)
    canvas.itemconfig(question, text=data['English'], fill='white')
    canvas.itemconfig(title, text='English', fill='white')
    global timer
    window.after_cancel(timer)

def change_question():
    global random_data
    try:
        random_data = random.choice(code_dict)
    except IndexError:
        messagebox.showinfo(title='Congratulations', message="You learnt all words!")
        exit('Bye')
    canvas.itemconfig(image, image=card_front_image)
    canvas.itemconfig(title, text='French', fill='black')
    canvas.itemconfig(question, text=random_data['French'], fill='black')
    global timer
    timer = window.after(3000, show_answer, random_data)

def next_question_yes():
    code_dict.remove(random_data)
    change_question()

window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
image = canvas.create_image(400, 263, image=card_front_image)
title = canvas.create_text(400, 150, text='', font=('Arial', 40, 'italic'))
question = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'))
change_question()
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=change_question)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=next_question_yes)
right_button.grid(row=1, column=1)


window.mainloop()

df = pandas.DataFrame(code_dict)
df.to_csv('data/words_to_learn.csv')
