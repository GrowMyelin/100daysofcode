from turtle import Turtle, Screen
import random
colors = ['blue','purple','orange','red','green','yellow','brown']
y_positions = [150,100,50,0,-50,-100,-150]
turtles = []
finished = [False]*len(colors)


def main():
    screen = Screen()
    screen.setup(width=500,height=400)
    user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
    user_bet_idx = colors.index(user_bet.lower())
    for turtle_index in range(len(colors)):
        turt = Turtle(shape='turtle')
        turtles.append(turt)
        turt.color(colors[turtle_index])
        turt.penup()
        turt.goto(x = -250,y=y_positions[turtle_index])
        turt.position()
    while not any(finished):
        for turtle_index in range(len(colors)):
            turtles[turtle_index].forward(random.randint(1,20))
        
        for turtle_index in range(len(colors)):
            if turtles[turtle_index].pos()[0] >= 250:
                finished[turtle_index] = True

    winners = []
    for turtle_index in range(len(colors)):
        if finished[turtle_index]:
            print(f"{colors[turtle_index]} wins!")
            winners.append(turtle_index)
    if user_bet_idx in winners:
        print("You win!")
    else:
        print("You lose.")
    screen.exitonclick()


if __name__ == "__main__":
    main()
