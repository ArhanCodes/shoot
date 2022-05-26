import turtle
import random




s=turtle.Screen()
s.bgcolor("lightblue")
s.setup(600,600,10,100)
s.title("ShootFlappyBirdLOL")


s.register_shape("b1.gif")
s.register_shape("player1.gif")
s.register_shape("bird.gif")
##s.tracer(1)

gravity=0.2
score=0
missedbird=0
GameOver=False


#Create Bird
bird= turtle.Turtle()
bird.shape("bird.gif")
bird.up()
bird.speed(0)
bird.setpos(-280,150)
bird.dx=2
bird.dy=0
birdstate="flying"


#Create a score board
pen=turtle.Turtle()
pen.up()
pen.goto(-280,270)
pen.ht()
pen.write("Score:0",font=("Courier",20,"bold"))


#Missed bird count
c=turtle.Turtle()
c.up()
c.goto(50,270)
c.ht()
c.write("Missed Bird:0",font=("Courier",20,"bold"))

#Creating Player Gun
gun = turtle.Turtle()
gun.shape("player1.gif")
gun.speed(0)
gun.up()
gun.goto(0,-260)

#Creating the Bullet
b=turtle.Turtle()
b.shape("b1.gif")
b.speed(0)
b.up()
bstate="ready"
b.ht()


#Move left and right

def move_left():
    x=gun.xcor()
    x=x-25
    gun.setx(x)


def move_right():
    x=gun.xcor()
    x=x+25
    gun.setx(x)

#Shoot the bullet
def shoot_the_bullet():
    global bstate
    if bstate == "ready":
        bstate = "fire"
        b.setpos(gun.xcor()+10,gun.ycor()+10)
        b.showturtle()

def fly():
    global gravity
    fly_list=[4,2,3]
    bird.dy=bird.dy-gravity
    if bird.ycor()<100:
        bird.dy=random.choice(fly_list)
        

s.listen()
s.onkey(move_left,"a")
s.onkey(move_right,"d")
s.onkey(shoot_the_bullet,"space")




try:
    while True:
        s.update()

        if bstate == 'fire':
            b.sety(b.ycor()+30)


        if b.ycor()>280:
            b.hideturtle()
            bstate='ready'


        #Bird fly
        if birdstate=="flying":
            fly()
        x=bird.xcor()+bird.dx
        y=bird.ycor()+bird.dy
        bird.goto(x,y)

        #When the bird reaches the right border it comes back
        #how many birds 
        if bird.xcor()>280 and GameOver==False :
            bird.goto(-280,150)
            missedbird=missedbird+1

            c.clear()
            c.write("Missedbird={}".format(missedbird),font=("Courier",20,"bold"))



            if missedbird == 3:
                GameOver=True

        if GameOver==True:
            s.bgpic("end.gif")
            break






        #Bird hit by bullet
        if bird.distance(b)<20:
            b.ht()
            bstate="ready"
            b.setpos(gun.xcor()+10,gun.ycor()+10)

            bird.dy=-3
            birdstate="falling"

            score=score+10
            pen.clear()
            pen.write("Score:{}".format(score),font=("Courier",20,"bold"))


        if bird.ycor()<=-250:
            bird.dy=0
            bird.goto(-280,150)
            birdstate="flying"
        
            





except:
    print("Game Over")






















