import turtle
import random


s=turtle.Screen()
s.bgcolor("lightblue")
s.setup(600,600,10,100)
s.title("Shooting a Bird")

s.register_shape("player1.gif")
s.register_shape("b1.gif")
s.register_shape("bird.gif")
s.tracer(0)

gravity=0.1


#Create Bird
bird=turtle.Turtle()
bird.shape("bird.gif")
bird.up()
bird.speed(0)
bird.setpos(-280,150)
bird.dx=2
bird.dy=0
birdstate="flying"



# Create the player turtle
gun = turtle.Turtle()
gun.shape("player1.gif")
gun.penup()
gun.speed(0)
gun.setposition(0,-250)




# Create the player's bullet
bullet = turtle.Turtle()
bullet.shape("b1.gif")
bullet.penup()
bullet.speed(0)
bullet.hideturtle()
bulletstate='ready'

def move_left():
    x = gun.xcor()
    x -= 30
    if x < -280:
        x = -280
    gun.setx(x)
    
def move_right():
    x = gun.xcor()
    x += 30
    if x > 280:
        x = 280
    gun.setx(x)

def shoot():
    global bulletstate
    if bulletstate=='ready':
        bulletstate='fire'
        bullet.setpos(gun.xcor()+10,gun.ycor()+25)
        bullet.showturtle()



def fly():
    global gravity
    fly_list=[2,4,5,6]
    bird.dy=bird.dy-gravity
    if bird.ycor()<100:
        bird.dy=random.choice(fly_list)





    

s.listen()
s.onkeypress(move_left,"Left")
s.onkeypress(move_right,"Right")
s.onkeypress(shoot,"space")

#Main code
try:
    while True:
        s.update()

        #Bullet fired
        if bulletstate == 'fire':
            bullet.sety(bullet.ycor()+30)

        #Bullet gone out of border
        if bullet.ycor()>280:
            bullet.hideturtle()
            bulletstate='ready'

        #Bird fly
        if birdstate=="flying":
            fly()
        x=bird.xcor()+bird.dx
        y=bird.ycor()+bird.dy
        bird.goto(x,y)

        #when bird reach right border come back
        if bird.xcor()>280:
            bird.goto(-280,150)

        #Bird hit by bullet
        if bird.distance(bullet)<20:
            bullet.ht()
            bulletstate="ready"
            bullet.setpos(gun.xcor()+10,gun.ycor()+25)

            bird.dy=-5
            birdstate="falling"

        if bird.ycor()<=-250:
            bird.dy=0
            bird.goto(-280,150)
            birdstate="flying"
            
        



except:
    print()


        
