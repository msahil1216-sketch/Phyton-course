import turtle #importing turtle
my_wn = turtle.Screen()
my_wn.bgcolor("red") #screen background color
my_wn.title("Turtle")
my_pen = turtle.Turtle()
size = 0
while True: #iterate loop
    for i in range(7):
        my_pen.fd(size+1)
        my_pen.left(90)
        size = size - 7
    size = size + 1