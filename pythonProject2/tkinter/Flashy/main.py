from tkinter import *
import pandas
import random




BACKGROUND_COLOR = "#B1DDC6"


data = pandas.read_csv("./data/french_words.csv")
to_learn = data.to_dict(orient = "records")
current_card = {}

def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_title , text="French" , fill="black")
    canvas.itemconfig(canvas_word, text=current_card["French"] , fill="black")
    canvas.itemconfig(canvas_image1, image=front_image)
    print(current_card)

def flip_card():
    canvas.itemconfig(canvas_image1, image=back_image)
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_word,text = current_card[] ,fill="white")
    print(current_card)












window=Tk()
window.title("Flashy")
window.minsize(width=900,height=626)
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)


canvas = Canvas(width=800 , height=526 )
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
canvas_image1 = canvas.create_image(400,263,image=front_image)
canvas_title = canvas.create_text(400,  150 , text="English", font=("Ariel", 40, "italic") ,fill="black" )
canvas_word = canvas.create_text(400,  263 , text="word", font=("Ariel", 60, "bold") ,fill="black" )

canvas.config(highlightthickness=0 ,bg=BACKGROUND_COLOR)
canvas.grid(column=0 , row=0 , columnspan=2)


tick_image = PhotoImage(file="./images/right.png")
tick_button = Button(image=tick_image , highlightthickness=0 , borderwidth=0 , command=next_card)
tick_button.grid(column=1 , row=1)

cross_image = PhotoImage(file="./images/wrong.png")
cross_button = Button(image=cross_image , highlightthickness=0 , borderwidth=0 , command=flip_card)
cross_button.grid(column=0 , row=1)

window.after(2000 , func=flip_card)










window.mainloop()
