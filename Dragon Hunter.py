import turtle
import math
import os
import random
import winsound

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("dragon hunter")
wn.bgpic("images/new.gif")
#set score to 0
score=0
#draw score
score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-490,280)
scorestring="Score: %s" %score
score_pen.write(scorestring,False,align="left",font=("Arial",14,"bold"))
score_pen.hideturtle()

#register shapes
turtle.register_shape("images/players.gif")
turtle.register_shape("images/enemy.gif")
turtle.register_shape("images/arrow.gif")

#player
ninja=turtle.Turtle()
ninja.color("white")
ninja.speed(0)
ninja.shape("images/players.gif")
ninja.setheading(90)
ninja.penup()
ninja.setposition(0,-200)
ninjaspeed=40

#no. of enemies
noe=5
enemies=[]

#add enemies to list
for i in range(noe):
    #enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("black")
    enemy.shape("images/enemy.gif")
    enemy.penup()
    enemy.speed(0)
    x=random.randint(-400,400)
    y=random.randint(100,150)
    enemy.setposition(x,y)

enemyspeed=5

#weapon
arrow=turtle.Turtle()
arrow.color("white")
arrow.shape("images/arrow.gif")
arrow.speed(0)
arrow.penup()
arrow.setheading(90)
arrow.shapesize(1,1)
arrow.hideturtle()
arrowspeed=30

#define arrow state
#ready-ready to fire
#released-arrow released
Arrowstate="ready"


#movement
def move_left():
    x = ninja.xcor() - ninjaspeed
    if x < -500:
        x = -500
    ninja.setx(x)

def move_right():
    x = ninja.xcor() + ninjaspeed
    if x >492:
        x = 492
    ninja.setx(x)

def Arrow_released():
    global Arrowstate
    if Arrowstate=="ready":
        Arrowstate="released"
        x=ninja.xcor()-30
        y=ninja.ycor()+10
        arrow.setposition(x,y)
        arrow.showturtle()

def check_collision(t1,t2):
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance<15:
        return True
    else:
        return False
    
        

# Keyboard bindings
wn.onkey(move_left, 'a')
wn.onkey(move_right, 'd')
wn.onkey(Arrow_released,'space')
wn.listen()


#main game loop
while True:
    for enemy in enemies:
        #move the enemy
        x=enemy.xcor()
        x+=enemyspeed
        enemy.setx(x)

        #move the enemy back and down
        if enemy.xcor()>492:
            for e in enemies:
                y=e.ycor()
                y-=10
                e.sety(y)
            enemyspeed*=-1
        if enemy.xcor()<-500:
            for e in enemies:
                y=e.ycor()
                y-=10
                e.sety(y)
            enemyspeed*=-1
        #check arrow collision
        if check_collision(arrow,enemy):
            #reset arrow
            arrow.hideturtle()
            enemy.hideturtle()
            Arrowstate="ready"
            arrow.setposition(0,-400)
            #reset enemy
            enemy.showturtle()
            x=random.randint(-400,400)
            y=random.randint(100,150)
            enemy.setposition(x,y)
            #update score
            score+=100
            score_pen.clear()
            scorestring="Score: %s" %score
            score_pen.write(scorestring,False,align="left",font=("Arial",14,"normal"))
        if check_collision(ninja,enemy):
            ninja.hideturtle()
            enemy.hideturtle()
            w=turtle.Screen()
            w.bgcolor("black")
            w.title("Game Over")
            w.bgpic("Gameover.gif")
            break
            
    #move arrow
    if Arrowstate=="released":
        y=arrow.ycor()
        y+=arrowspeed
        arrow.sety(y)

    #check arrow reach the top or not
    if arrow.ycor()>200:
        Arrowstate="ready"
        arrow.hideturtle()

    
wn.mainloop()
delay=input("press ENTER to exit")

