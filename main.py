import turtle, pandas
import turtle as tut
mscr = turtle.Screen()
mscr.title("US States")
mscr.setup(725, 491)
img = "blank_states_img.gif"
mscr.addshape(img)
backg = turtle.shape(img)
raw_states = pandas.read_csv("50_states.csv")
mid_states = raw_states["state"]
states = []
for s in mid_states:
    states.append(s)
print(states)
def raw_guess():
    global mscr
    guess_return = mscr.textinput("Guess a US state", "Enter state")
    upper_guess = guess_return.title()
    return upper_guess

def guess_checker(guess):
    global states
    if guess in states:
        return True
    else:
        return False

game_on = True
while game_on:
    guess = raw_guess()
    xcor = int(raw_states[raw_states.state == guess].x)
    ycor = int(raw_states[raw_states.state == guess].y)
    fact = guess_checker(guess)
    if fact == False:
        print("failed")
        game_on = False
    else:
        moving_word =  turtle.Turtle()
        moving_word.penup()
        moving_word.hideturtle()
        moving_word.color("black")
        moving_word.goto(xcor, ycor)
        moving_word.write(guess)

mscr.exitonclick()