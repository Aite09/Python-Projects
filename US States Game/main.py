import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# code to get the co-ordinates by clicking in the screen
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/ 50 States correct",
                                    prompt="Whats another state's name?").title()

    if answer_state == "Exit":
        # states missed into csv file
        missing_states = []
        for states in all_states:
            if states not in guessed_states:
                missing_states.append(states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Missed States.csv")
        break


    # If answer is one of the states from csv file
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)




