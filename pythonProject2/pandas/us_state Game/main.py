import turtle
import pandas
import tkinter

screen=turtle.Screen()
screen.title("US_state Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_state=[]

while len(guessed_state) < 50:
    answer_text = screen.textinput(title="guess" , prompt="more guess").title()
    if answer_text in all_states:
        guessed_state.append(answer_text)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_text]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_text)

screen.exitonclick()