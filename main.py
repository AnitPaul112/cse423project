from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math

width, height = 600, 600

#center
xaxis = width/2
yaxis = height/2


cat_x = 0.0 #cat will be show from center
cat_y = -50 #below change if needed

food =[]
food.append((xaxis-67, -(yaxis-35)))
food.append((xaxis-57, -(yaxis-35)))
food.append((xaxis-47, -(yaxis-35)))
food.append((xaxis-37, -(yaxis-35)))
food.append((xaxis-27, -(yaxis-35)))
food.append((xaxis-17, -(yaxis-35)))

hungry = 10




def come_down(val):#srijon
    global cat_y, hungry 
    if cat_y > -50:
        cat_y-=70
    hungry += 0.5
    glutPostRedisplay() 

def specialKeyListener(key,x, y):#srijon fish game logic + move logic
    global left, sleep, cat_x, cat_y, fish_x, fish_y, fishON, fishgamepoint

    if key== GLUT_KEY_LEFT and cat_x >= -xaxis+62 and sleep == False:
        cat_x -= 10.0
    if key== GLUT_KEY_RIGHT and cat_x <= xaxis-62 and sleep == False:
        cat_x += 10.0
    if sleep == False and key == GLUT_KEY_UP:
        if cat_y < 20:
            cat_y+=70
        glutTimerFunc(300, come_down, 0)
    if fishON == True:
        if fish_x-50<=cat_x<=fish_x+50: # x axis below the fish 100 
            if cat_y-127 >=fish_y-20: # caches the fish moving y axis
                fishgamepoint += 1
                print("point: ", fishgamepoint)
                fish_x = random.uniform((xaxis/2)+100, (-xaxis/2)-100) # generate new fish point
                if fish_x < 0:
                    left = True
                else:
                    left = False
                fish_y = -100


    glutPostRedisplay() 
