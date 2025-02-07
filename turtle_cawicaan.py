import turtle
t = turtle.Turtle()
ts = turtle.getscreen()
turtle.Screen().bgcolor("#00b6b4")

#head
t.speed(10)
t.color('black','#11ee55')
t.width(2)
t.begin_fill()
t.circle(120,-360)
t.end_fill()
turtle.hideturtle()

#hair
t.penup()
t.goto (-65,220)
t.pendown()
t.right(120)
t.color('black','#11ee55')
t.begin_fill()
t.circle(75,-120)
t.end_fill()

def lefthorn():
    t.penup()
    t.goto (-80,210)
    t.pendown()
    t.color('black','gray')
    t.begin_fill()
    t.fd(20)
    t.rt(40)
    t.bk(35)
    t.end_fill()

def righthorn():
    t.penup()
    t.goto (80,210)
    t.pendown()
    t.color('black','gray')
    t.begin_fill()
    t.fd(20)
    t.lt(31)
    t.bk(40)
    t.end_fill()

def horn():
    lefthorn()
    righthorn()

def sclera():
    t.penup()
    t.goto (65,190)
    t.pendown()
    t.color('black','white')
    t.begin_fill()
    t.circle(70,360)
    t.end_fill()

def iris():
    t.penup()
    t.goto (30,180)
    t.pendown()
    t.color('black','#11ee55')
    t.begin_fill()
    t.circle(35,360)
    t.end_fill()

def pupil():
    t.penup()
    t.goto (15,175)
    t.pendown()
    t.color('black','black')
    t.begin_fill()
    t.circle(20,360)
    t.end_fill()

def white():
    t.penup()
    t.goto (10,170)
    t.pendown()
    t.color('white','white')
    t.begin_fill()
    t.circle(5,360)
    t.end_fill()

def eyes():
    sclera()
    iris()
    pupil()
    white()

def ltdimple():
    t.penup()
    t.goto (-65,95)
    t.pendown()
    t.color('black')
    t.lt(10)
    t.bk(15)

def rtdimple():
    t.penup()
    t.goto (65,95)
    t.pendown()
    t.color('black')
    t.rt(90)
    t.fd(20)
    
def dimples():
    ltdimple()
    rtdimple()
    
horn()
eyes()

#mouth
t.penup()
t.goto (-70,90)
t.pendown()
t.color('black')
t.rt(160)
t.circle(90,100)

#chin
t.penup()
t.goto (-40,40)
t.pendown()
t.color('black')
t.rt(90)
t.circle(50,80)

dimples()
