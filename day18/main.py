from turtle import Turtle,Screen,colormode
import random

def findAngle(sides):
    return (sides-2)*(180/sides)


print(findAngle(3))
def drawPolygon(sides,turt):
    angle = 180 - findAngle(sides)
    for i in range(sides):
        turt.forward(100)
        turt.right(angle)
def main():
    timmy = Turtle()
    timmy.shape('turtle')
    colormode(255)
    timmy.speed('fastest')
    for i in range(0,360,10):
        timmy.home()
        timmy.pencolor(random.randint(1,255),random.randint(1,255),random.randint(1,255))
        timmy.setheading(i)
        timmy.circle(100)
    screen = Screen()
    screen.exitonclick()

"""     for i in range(100):
        timmy.pencolor(random.randint(1,255),random.randint(1,255),random.randint(1,255))
        angle = random.randint(0,360)
        distance = random.randint(0,100)
        timmy.forward(distance)
        timmy.left(angle) """

"""     drawPolygon(3,timmy)
    timmy.pencolor(random.randint(1,255),random.randint(1,255),random.randint(1,255))
    drawPolygon(4,timmy)
    timmy.pencolor(random.randint(1,255),random.randint(1,255),random.randint(1,255))
    drawPolygon(5,timmy)
    timmy.pencolor(random.randint(1,255),random.randint(1,255),random.randint(1,255))
    drawPolygon(6,timmy)
    timmy.pencolor(random.randint(1,255),random.randint(1,255),random.randint(1,255))
    drawPolygon(8,timmy)
    timmy.pencolor(random.randint(1,255),random.randint(1,255),random.randint(1,255))
    drawPolygon(10,timmy) """


if __name__ == "__main__":
    main()