from graph import *
import random
def moveSnake (xNew, yNew):
    global x,y,N
    for k in range (len(snake)-1,0,-1):
        newCoord = coords(snake[k-1])
        moveObjectTo(snake[k], newCoord[0], newCoord[1])
    moveObjectTo(snake[0], xNew, yNew)
    x=xNew
    y=yNew
def update():
    for k in range (len(snake)):
        if coords(snake[0])==coords((snake[k])+1):
            death()
    if dx or dy:
        moveSnake(x+dx*a, y+dy*a)
    if x>=490 and y<=580:
        move(0,1)
    if x<=0 and y>=0:
        move(0,-1)
    if y>=590 and x>=10:
        move(-1,0)
    if y<=0 and x<=480:
        move(1,0)
    if x==z and y==c:
        apple(((random.randint(10,480)//10)*10),((random.randint(10,580))//10)*10)
def keyPressed(event):
    global dx,dy
    if event.keycode == VK_LEFT and dx!=1: 
        dx=-1
        dy=0
    elif event.keycode == VK_RIGHT and dx!=-1:
        dx=1
        dy=0
    elif event.keycode == VK_UP and dy!=1:
        dx=0
        dy=-1
    elif event.keycode == VK_DOWN and dy!=-1:
        dx=0
        dy=1
def move(xNew,yNew):
    global dx,dy
    dx=xNew
    dy=yNew
def apple(zNew,cNew):
    global z,c,N
    brushColor("red")
    moveObjectTo(aple,zNew,cNew)
    z=zNew
    c=cNew
    brushColor("green")
    block(N)
def block(N):
    if dx==-1:
        for i in range (N):
            obj = rectangle (((x+10*N+10)+i*a), y, ((x+10*N+10)+i*a+a), y+a)
            snake.append (obj)
            penColor("black")
            brushColor("green")
    if dx==1:
        for i in range (N):
            obj = rectangle (((x-10*N-10)+i*a), y, ((x-10*N-10)+i*a+a), y+a)
            snake.append (obj)
            penColor("black")
            brushColor("green")
    if dy==1:
        for i in range (N):
            obj = rectangle (((x)+i*a), y-10*N-10, ((x)+i*a+a), y+a-10*N-10)
            snake.append (obj)
            penColor("black")
            brushColor("green")
    if dy==-1:
        for i in range (N):
            obj = rectangle (((x)+i*a), y+10*N+10, ((x)+i*a+a), y+a+10*N+10)
            snake.append (obj)
            penColor("black")
            brushColor("green")
def death():
    close()
    print("Game Over")
brushColor("blue")
rectangle(0,0,500,600)
brushColor("red")
z=(random.randint(10,480))//10*10
c=(random.randint(10,580))//10*10
aple=rectangle(z,c,z+10,c+10)
x=100
y=100
dx=0
dy=0
a=10
N=1
brushColor("yellow")
snake=[]
for i in range (4):
            obj = rectangle (((x)+i*a), y, ((x)+i*a+a), y+a)
            snake.append (obj)
            penColor("black")
            brushColor("green")
onKey(keyPressed)
onTimer(update, 50)
run()
