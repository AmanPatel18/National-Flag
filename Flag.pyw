# importing time and turtle module

import time
from turtle import Turtle,Screen


# defining screen properties

win=Screen()
win.title("Vande Matram")
win.bgcolor("black")
win.bgpic("flag1.gif")

# defining drawing pen properties

pen=Turtle()
pen.pensize(4)
pen.speed(1)

pen.up()
pen.goto(-150,200)
pen.down()


# saffron ribbon

pen.begin_fill()
pen.fillcolor("#FF9933")
pen.fd(300)
pen.setheading(270)
pen.fd(66.7)
pen.setheading(180)
pen.fd(300)
pen.setheading(90)
pen.fd(66.7)
pen.end_fill()

# white ribbon

pen.begin_fill()
pen.fillcolor("white")
pen.bk(66.7)
pen.setheading(0)
pen.fd(300)
pen.setheading(270)
pen.fd(66.7)
pen.setheading(180)
pen.fd(300)
pen.setheading(90)
pen.fd(66.7)
pen.end_fill()

# green ribbon

pen.begin_fill()
pen.fillcolor("#128807")
pen.bk(66.7)
pen.setheading(0)
pen.fd(300)
pen.setheading(270)
pen.fd(66.7)
pen.setheading(180)
pen.fd(300)
pen.setheading(90)
pen.fd(66.7)
pen.end_fill()

# blue ring

pen.fd(66.7)
pen.setheading(0)
pen.fd(150)
pen.pensize(4)
pen.circle(-32)
pen.setheading(270)
pen.pensize(2)
pen.color("#000088")
pen.fd(32)
for i in range(24):
    pen.fd(32)
    pen.bk(32)
    pen.left(15)

# Text 'Vande'

pen.up()
pen.goto(-120,-100)
pen.color("#f7880b")
pen.write("Vande",font=('Times New Roman',50,'bold'))

#Text 'Matram'

pen.goto(0,-160)
pen.color("#128807")
pen.write("Matram",font=('Times New Roman',40,'bold'))

# Hiding Turtle 

pen.hideturtle()

# End Credits

time.sleep(2)
win.bgpic("")
win.bgcolor("black")
pen.reset()
pen.hideturtle()
pen.color('red')
pen.up()
pen.goto(-50,0)
pen.write("Programmed By:",align='center',font=('Comic Sans MS',35,'bold'))
pen.goto(50,0)
pen.goto(0,-70)
pen.write("\tAman Patel",align='center',font=('Comic Sans MS',40,'bold'))     

win.mainloop()
