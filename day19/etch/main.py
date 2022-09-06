from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def rotate_clockwise():
    tim.right(5)

def rotate_counter_clockwise():
    tim.left(5)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
def main():
    screen.listen()
    screen.onkey(key="w",fun=move_forwards)
    screen.onkey(key="s",fun=move_backwards)
    screen.onkey(key="d",fun=rotate_clockwise)
    screen.onkey(key="a",fun=rotate_counter_clockwise)
    screen.onkey(key="c",fun=clear)
    screen.exitonclick()

if __name__ == "__main__":
    main()
