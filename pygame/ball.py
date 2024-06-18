import turtle
win=turtle.Screen()
win.setup(800,600)
win.bgcolor('black')
win.title("Ball Game")
win.tracer(0)
#Left paddle

l_paddle = turtle.Turtle()
l_paddle.speed(0) # speed 1 to 10  vara kuduthukalam athula animation speed ,slow  ,0 indrathu vanthu constant ah!stable ah irukum
l_paddle.shape("square")
l_paddle.color("white")
l_paddle.shapesize(stretch_wid=5,stretch_len=1)#stretch panni size resize panrom
l_paddle.penup() #antha line varama irukkurathukaga , pen down position la vendam pen up panniko
l_paddle.goto(-380,0) #left side la -380 move pannni vechurukom


#right paddle

r_paddle = turtle.Turtle()
r_paddle.speed(0) # speed 1 to 10  vara kuduthukalam athula animation speed ,slow  ,0 indrathu vanthu constant ah!stable ah irukum
r_paddle.shape("square")
r_paddle.color("white")
r_paddle.shapesize(stretch_wid=5,stretch_len=1)#stretch panni size resize panrom
r_paddle.penup() #antha line varama irukkurathukaga , pen down position la vendam pen up panniko
r_paddle.goto(380,0) #left side la -380 move pannni vechurukom

while True:
    win.update()
    break

ball=turtle.Turtle()
ball.shape('circle')
ball.color('white')

while True:
    win.update()