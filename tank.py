from graph import *
import math
def keyPressed(event):
    global isFlying
    if event.keycode == VK_SPACE:
        if isFlying == False:
            drawBullet()
            isFlying = True
    if event.keycode == VK_LEFT:
        drawGun(angle+5)
    elif event.keycode == VK_RIGHT:
        drawGun(angle-5)
    elif event.keycode == VK_ESCAPE:
        close()
def drawBullet():
    global bullet,z,c
    bullet=circle(z, c, r)
    
def drawGun(angleNew):
  global angle, gun ,z,c
  angle = angleNew
  aRad = angle*math.pi/180
  x1 = x0 + L*math.cos(aRad)
  y1 = y0 - L*math.sin(aRad)
  z=x1
  c=y1
  if gun == None:
    gun = line(x0, y0, x1, y1)
  else:
    changeCoords(gun, [(x0,y0), (x1,y1)] )
def update():
    global isFlying, bullet
    movePlates()
    if isFlying:
        y = coords(bullet)[1]
        x = coords(bullet)[2]
        if y <= -5 or y>=600 or x<=-3 or x>=550:
            isFlying = False                    
        else:
            moveObjectBy(bullet, (z-x0)/u, (c-y0)/u)
            checkCollision()

def createPlates( N ):
  global plates  # глобальный массив
  yPlates = 100  # у всех одна y-координата
  plates = []    # пока массив пустой
  for i in range(N):
    brushColor( randColor() )
    p = circle(randint(0,500), # x центра 
               yPlates,        # y центра
               randint(10,20)) # радиус
    plates.append(p) # добавить в массив
def movePlates():
  global plates  # глобальный массив
  for p in plates: # для каждой тарелки
    moveObjectBy(p, -2, 0) # сдвиг на 2 влево
    x1,y1,x2,y2 = coords(p)
    if x1 < 0: # если вышла за границу...
               # перескочить вправо на ...
      moveObjectBy(p, randint(500,600), 0)
def movePlates():
  global plates  # глобальный массив
  for p in plates: # для каждой тарелки
    moveObjectBy(p, -2, 0) # сдвиг на 2 влево
    x1,y1,x2,y2 = coords(p)
    if x1 < 0: # если вышла за границу...
               # перескочить вправо на ...
      moveObjectBy(p, randint(500,600), 0)
def checkCollision():
    global isFlying, bullet, plates,score
    for p in plates:
        if hit(p):
            score+=1
            lbl["text"] = "Счёт: " + str(score)
            moveObjectBy(p, randint(500,600), 0)
            deleteObject(bullet)           
            isFlying = False  # остановить снаряд
            break # только одну тарелку за раз

def hit(p):
  global bullet
     # координаты снаряда
  x1,y1,x2,y2 = coords(bullet)
  xb = x1 + r # центр снаряда
  yb = y1 + r # координаты тарелки
  x1p,y1p,x2p,y2p = coords(p)
  xp = (x1p + x2p) / 2
  yp = (y1p + y2p) / 2
  Rp = (x2p - x1p) / 2
  d2 = (xb-xp)**2 + (yb-yp)**2
  return d2 <= (Rp+r)**2

H = 60; W = 30; L = 40
x0 = 200; y0 = 400; angle = 90
gun = None
r = 3   # радиус снаряда
u = 3   # скорость снаряда
brushColor("black")
lbl = label("Счёт: 0",10,10,bg="white")
score=0
bullet = None
isFlying = False
brushColor("#6b8e23")
rectangle(x0-W/2, y0-H/2, x0+W/2, y0+H/2)
penSize(5)
drawGun(angle)
penSize(1)
brushColor("#556b2f")
circle(x0, y0, W/2)
onKey(keyPressed)
createPlates( 5 )  
onTimer(update, 30)
run()
