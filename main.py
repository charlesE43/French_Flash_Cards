from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("Images/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flash Cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

#creates canvas for card
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="Images/card_front.png")
card_back_image = PhotoImage(file='Images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

#create buttons
right_image = PhotoImage(file='Images/right.png')
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file='Images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()

