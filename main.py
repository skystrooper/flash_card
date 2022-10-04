import random
from tkinter import *

import pandas
from pandas import *


BACKGROUND_COLOR = "#B1DDC6"

try:
    data = read_csv('yet_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('french_words.csv')
    word_list = original_data.to_dict(orient='records')
else:
    word_list = data.to_dict(orient='records')

correct_answer = []


def update_image():
    canvas.itemconfig(image_update, image=back_side)
    canvas.itemconfig(answer, text=f'{random_word["English"]}')
    canvas.itemconfig(title, text='English')


def next_card():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(word_list)
    canvas.itemconfig(image_update, image=front_side)
    canvas.itemconfig(title, text='French')
    canvas.itemconfig(answer, text=f'{random_word["French"]}')
    flip_timer = window.after(3000, func=update_image)


def right_click_command():
    word_list.remove(random_word)
    data2 = pandas.DataFrame(word_list)
    data2.to_csv("yet_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title('Flash card')
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=update_image)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
back_side = PhotoImage(file='card_back.png')
front_side = PhotoImage(file='card_front.png')
image_update = canvas.create_image(400, 263, image=front_side)
canvas.grid(row=0, column=0, columnspan=3)

random_word = random.choice(word_list)
title = canvas.create_text(400, 150, text='French', fill='black', font=("Ariel", 35, 'italic'))
answer = canvas.create_text(400, 263, text=f'{random_word["French"]}', fill='black', font=("Ariel", 60, 'bold'))


right_image = PhotoImage(file='right.png')
wrong_image = PhotoImage(file='wrong.png')

right_button = Button(image=right_image, highlightthickness=0, command=right_click_command)
right_button.grid(row=3, column=2)

wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=3, column=0)

window.mainloop()
