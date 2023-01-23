import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

image = turtle.shape(image)
data = pandas.read_csv("50_states.csv")

game_is_on = True
turtle = turtle.Turtle()
turtle.hideturtle()
turtle.penup()
guessed_states = []

all_states = data.state.to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the state",
                                    prompt="What's another state?").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        state_data = data[data.state == answer_state]
        turtle.setpos(state_data.x.item(), state_data.y.item())
        turtle.write(state_data.state.item())
        guessed_states.append(answer_state)

states_to_learn = []
for state in all_states:
    if state not in guessed_states:
        states_to_learn.append(state)

states_to_learn_df = pandas.DataFrame(states_to_learn)

states_to_learn_df.to_csv('states_to_learn.csv')
