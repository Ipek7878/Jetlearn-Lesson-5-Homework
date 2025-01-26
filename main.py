import pgzrun
import random


TITLE="Pikachu Game"

WIDTH=700
HEIGHT=500

pikachu=Actor('pikachu')
pikachu.pos=100,100

ash=Actor('ash')
ash.pos=200,200

score=0
game_over= False

def draw():
    screen.clear()
    screen.blit("background",(0,0))

    pikachu.draw()
    ash.draw()
    screen.draw.text("score="+str(score),topleft=(20,10),fontsize=30,color="black")

    if game_over:
        screen.blit("background2",(0,0))
        screen.draw.text("Time's up! Your score is"+str(score),midtop=(200,10),fontsize=30,color="black")
    
def pikachu_pos():
    pikachu.x=random.randint(50,650)
    pikachu.y=random.randint(50,450)
    

def update():
    global score
    if keyboard.left:
        ash.x=ash.x-2
    if keyboard.right:
        ash.x=ash.x+2
    if keyboard.up:
        ash.y=ash.y-2
    if keyboard.down:
        ash.y=ash.y+2
    if ash.colliderect(pikachu):
        score=score+10
        pikachu_pos()
    
def time_up():
    global game_over
    game_over=True

clock.schedule(time_up,30.0)   


pikachu_pos()
pgzrun.go()