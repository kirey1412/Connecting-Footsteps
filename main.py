import pgzrun, random
from time import time
TITLE="Footsteps"
WIDTH=450
HEIGHT=400
footsteps=[]
lines=[]
numberoffootsteps=6
countfootsteps=0
starttime=0
totaltime=0

def create_footsteps():
    global starttime
    for i in range(0,numberoffootsteps):
        feet=Actor("feet")
        feet.pos=random.randint(50,WIDTH-80),random.randint(50,HEIGHT-80)
        footsteps.append(feet)
    starttime=time()

def draw():
    global totaltime, starttime
    screen.blit("background",(0,0))
    number=1
    for footstep in footsteps:
        footstep.draw()
        screen.draw.text(str(number),(footstep.pos[0],footstep.pos[1]+20))
        number+=1
    for line in lines:
        screen.draw.line(line[0],line[1],"white")
    if countfootsteps<numberoffootsteps:
        totaltime=time()-starttime
        screen.draw.text(str(round(totaltime)), (20,10), fontsize=30)
    else:
        screen.draw.text(str(round(totaltime)), (10,10), fontsize=30)

def on_mouse_down(pos):
    global countfootsteps,numberoffootsteps,footsteps,lines
    if countfootsteps<numberoffootsteps:
        if footsteps[countfootsteps].collidepoint(pos):
            if countfootsteps:
                lines.append((footsteps[countfootsteps-1].pos, footsteps[countfootsteps].pos))
            countfootsteps+=1
        else:
            lines=[]
            countfootsteps=0

def update():
    pass
create_footsteps()
pgzrun.go()