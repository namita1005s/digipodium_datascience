import pgzrun
from random import randint
# screen size
WIDTH = 1000
HEIGHT = 500

# OBJECTS 
p = Actor('hero')
e = Actor('enemy')
c = Actor('friut')
c.x= randint(50,WIDTH-50)
c.y= randint(50,HEIGHT-50)
p.pos = (WIDTH/2,HEIGHT/2)
e.pos = (-100,HEIGHT/2)
ps =7
es =1
score = 0
 #player control
def player_control():
    if keyboard.left:
        p.x -=ps
    if keyboard.right:
        p.x +=ps
    if keyboard.up:
        p.y -=ps
    if keyboard.down:
        p.y +=ps
    if keyboard.space:
        p.angle +=ps
        # enemy tracking\
def enemy_tracking():
    if p.x > e.x:
        e.x+=es
    if p.x < e.x:
        e.x-=es
    if p.y > e.y:
        e.y+=es
    if p.y < e.y:
        e.y-=es
    print(f'player {p.pos} enemy {e.pos}')    
    if e.colliderect(p):
        exit()
def fruit_eating():
    global score
    if p.colliderect(c):
        c.x = randint(50,WIDTH-50)
        c.y = randint(50,HEIGHT-50)
        score+=10
        sounds.clap.play()

def draw():
    screen.clear()
    p.draw()
    e.draw()
    c.draw()
    screen.draw.text(f'Score {score}',(10,10),color ='white')

def update(dt):
    player_control()
    enemy_tracking()
    fruit_eating()

        # game loop
pgzrun.go()