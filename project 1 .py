import turtle
import random
screen = turtle.Screen()
screen.bgcolor("sky blue")

pen = turtle.Turtle()
pen.speed(20)
pen.shape("blank")


def draw_sun(x, y, radius, color):
    
    pen.up()
    pen.goto(x, y - radius)
    pen.down()
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

def draw_sun_beams(x, y, color, outer_radius, beam_length):
    pen.up()
    pen.seth(0)
    pen.goto(x, y)
    
    pen.color(color)
    for _ in range(12): # 12 beams
        pen.forward(outer_radius - beam_length)
        pen.down()
        pen.forward(beam_length)
        pen.up()
        pen.backward(outer_radius)
        pen.left(360/12)


def draw_hut(height,length,width):
  pen.begin_fill()
  pen.color('yellow')
  pen.left(175)
  pen.forward(width)
  pen.right(80)
  pen.forward(height+2)
  pen.left(-90)
  pen.forward(width+8)
  pen.left(-90)
  pen.forward(height+10)
  pen.end_fill()

  pen.begin_fill()
  pen.color('purple')
  pen.right(-85)
  pen.forward(length-20)
  pen.left(90)
  pen.forward(height+9)
  pen.left(90)
  pen.forward(length+10)
  pen.end_fill()

def draw_triangle(width):
  pen.begin_fill()
  pen.color('brown')
  pen.goto(-122,263)
  for i in range (2):
    pen.left(-120)
    pen.forward(width+5)
  pen.end_fill()
  
def draw_roof(length,width):
  pen.begin_fill()
  pen.color('red')
  pen.left(60)
  pen.forward(length)
  pen.left(120)
  pen.forward(width+2)
  pen.left(60)
  pen.forward(length)
  pen.end_fill()

def draw_window(x,y,length, width):
  pen.up()
  pen.goto(x,y)
  pen.down()
  pen.begin_fill()
  pen.color('orange')
  for i in range (2):
    pen.forward(length)
    pen.left(90)
    pen.forward(width)
    pen.left(90) 
  pen.end_fill()

  pen.up()
  pen.goto(x-44,y-46)
  pen.down()
  pen.color('black')
  for i in range (2):
     pen.right(90)
     pen.forward(length)
     pen.right(90)
     pen.forward(width)
 
  pen.up()
  pen.goto(x,y-23)
  pen.down()
  pen.forward(length) 
  
def draw_door(width,height):
    pen.up()
    pen.goto(100,200)
    pen.down()
    pen.begin_fill()
    pen.color('grey')
 
    for i in range (2):
   
      pen.left(90)
      pen.forward(height)
      pen.right(-90)
      pen.forward(width)
    pen.end_fill() 

    pen.up()
    pen.goto(125,140)
    pen.down()
    pen.begin_fill()
    pen.color('black')
    pen.circle(4)
    pen.end_fill()


def draw_clouds(x,y):
    pen.up()
    pen.goto(x,y)
    pen.down()
    pen.begin_fill()
    pen.color('white')
  
    for i in range (6):
         pen.circle(60,180)
         pen.right(120)
     
    pen.end_fill()

def draw_field():
  pen.up()
  pen.goto(-1000,10)
  pen.down()
  pen.begin_fill()
  pen.color('blue')
  for i in range (2):
    pen.forward(3000)
    pen.left(-90)
    pen.forward(12000)
    pen.left(90)   
  pen.end_fill()
  pen.up()
  pen.goto(-950,10)
  pen.down()
  pen.begin_fill()
  pen.color('green')
  pen.forward(11000)
  pen.left(-90)
  pen.forward(5000)
  pen.left(90)  
  pen.end_fill()


def draw_fence(x,y):
  pen.up()
  pen.goto(x,y)
  pen.down()
  pen.begin_fill()
  pen.color('brown')

  for i in range (2):
    pen.forward(9)
    pen.right(-90)
    pen.forward(9)
    pen.right(-90) 

  for i in range (2):
    pen.forward(898)
    pen.right(-90)
    pen.forward(9)
    pen.right(-90)
    
  pen.end_fill()

def draw_line(x,y):
  pen.up()
  pen.goto(x,y)
  pen.down()
  pen.begin_fill()
  pen.color('brown')

  for i in range (2):
    pen.forward(9)
    pen.right(-90)
    pen.forward(100)
    pen.right(-90) 
  pen.end_fill()
 
  # Function to draw a petal
def draw_petal():
      pen.begin_fill()
      pen.circle(40,60)
      pen.left(120)
      pen.circle(40,60)
      pen.end_fill()
      for _ in range(6):
      # Randomly select a color
        colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        pen.color(colors[_ % len(colors)])
        pen.left(60)

def draw_petal(x, y):
    pen.up()
    pen.goto(x, y)
    pen.down()
    
    for _ in range(6):
    # Randomly select a color
      colors = ["red", "orange", "yellow", "brown", "blue", "purple"]
      pen.begin_fill()
      pen.circle(90, 60)
      pen.left(120)
      pen.circle(90, 60)
      pen.color(colors[_ % len(colors)])
      pen.left(60)
      pen.end_fill()

draw_hut(250,300,100)
draw_triangle(100)
draw_roof(305,100)
draw_door(75,180)
draw_window(-40,180,45,45)
draw_window(60,180,45,45)
draw_window(260,180,45,45)
draw_clouds(400,400)
draw_clouds(600,400)
draw_clouds(-375,400)
draw_clouds(-600,400)
draw_sun(-800,500,80,'yellow')
draw_sun_beams( -800, 340, "yellow", 115, 15)
draw_field()
draw_fence(-1000,30)
draw_fence(290,30)
draw_fence(-1000,70)
draw_fence(290,70)
draw_line(-950,10)
draw_line(-600,10)
draw_line(-200,10)
draw_line(300,10)
draw_line(650,10)
draw_line(950,10)
draw_petal(-300,-100)
draw_petal(-500,-100)
draw_petal(-100,-100)
draw_petal(410,-100)
draw_petal(810,-100)
draw_petal(610,-100)

pen.hideturtle()
screen.mainloop()
