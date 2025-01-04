from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math

width, height = 600, 600

#center
xaxis = width/2
yaxis = height/2
fish_x = random.uniform((xaxis/2)+100, (-xaxis/2)-100) #width-850
if fish_x < 0: #to determine which way the fish should move
    left = True
else:
    left = False
fish_y = -100
fish_xbutton = width -350 #upperrightfish
fish_ybutton = 170

ballx=-280
ballbutton = -280 #upperrightball
ballbuttonON = False
fishON = False
fishgamepoint = 0
ballgamepoint = 0
goal=True
rightgoalpost= True #the goalpost is on right or left

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



def playbutton(): #anit
    global play, fish_xbutton, fish_ybutton
    glColor3f(0,0.4,1)
    glPointSize(2)
    #box
    draw_line(width - 320, height - 350, width - 370, height- 350)
    draw_line(width - 320, height - 370, width - 370, height- 370)
    draw_line(width - 315, height - 365, width-315, height-355)
    draw_line(width - 375, height - 365, width-375, height-355)

    draw_line(width - 370, height - 350, width-375, height-355)
    draw_line(width - 370, height- 370, width-375, height-365)
    draw_line(width - 320, height - 350, width-315, height-355)
    draw_line(width - 320, height - 370, width - 315, height - 365)
    
    #play
    glPointSize(2)
    if play == False:
        #P
        draw_line(width - 365, height - 365, width-365, height-355)
        draw_line(width - 361, height - 361, width-361, height-356)
        draw_line(width - 365, height - 355,width - 361, height - 356)
        draw_line(width - 361, height - 361, width-365, height-361)
        #L
        draw_line(width - 353, height - 365, width-353, height-355)
        draw_line(width - 353, height - 365, width-348, height - 365)
        #A
        draw_line(width - 337, height - 365, width-340, height-355) #\
        draw_line(width - 343, height - 365, width-340, height-354) #/
        draw_line(width - 337, height-362, width-342,height-362)
        #Y
        draw_line(width - 330, height - 362, width-333, height-355) #-10
        draw_line(width - 330, height - 362, width-327, height-355)
        draw_line(width - 330, height - 362, width-330, height-366)
    else:
        #stop
        # S
        draw_line(width - 365, height - 355, width - 360, height-355)
        draw_line(width - 365, height - 360, width - 360, height-360)
        draw_line(width - 365, height - 365, width - 360, height-365)
        draw_line(width - 365, height - 355, width - 365, height-360)
        draw_line(width - 360, height-360, width - 360, height-365)
        #T
        draw_line(width - 357, height - 355, width - 350, height-355)
        draw_line(width - 354, height - 355, width - 354, height-365)
        #O
        circle(4.3, (width-343, height-360))
        #P
        draw_line(width - 335, height - 365, width-335, height-355)
        draw_line(width - 331, height - 361, width-331, height-356)
        draw_line(width - 335, height - 355,width - 331, height - 356)
        draw_line(width - 331, height - 361, width-335, height-361)

        #ballbutton
        if ballbuttonON == False:
            glPointSize(4)
            glColor3f(1,0,0)
            circle(16,(-ballbutton-30,200))
            glColor3f(1,0,1)
            circle(11,(-ballbutton-30,200))
            glColor3f(1,0,0)
            circle(7,(-ballbutton-30,200))
            circle(4,(-ballbutton-30,200))
        if ballbuttonON == True:
            glPointSize(8)
            glColor3f(1,0,0)
            circle(16,(-ballbutton-30,200))
            circle(12,(-ballbutton-30,200))
            circle(8,(-ballbutton-30,200))
            circle(5,(-ballbutton-30,200))
        #fishbutton
        if fishON == False:
            glPointSize(2)
            glColor3f(0.0, 0.0, 1.0)  # Set color to blue
            draw_line(fish_xbutton - 15, fish_ybutton, fish_xbutton + 15, fish_ybutton)
            draw_line(fish_xbutton - 15, fish_ybutton-20, fish_xbutton + 15, fish_ybutton-20)
            draw_line(fish_xbutton - 15, fish_ybutton, fish_xbutton - 27, fish_ybutton - 10)
            draw_line(fish_xbutton - 15, fish_ybutton-20, fish_xbutton - 27, fish_ybutton - 10)
            draw_line(fish_xbutton + 15, fish_ybutton, fish_xbutton + 40, fish_ybutton - 15)
            draw_line(fish_xbutton + 15, fish_ybutton-20, fish_xbutton + 40, fish_ybutton-5)
            draw_line(fish_xbutton + 40, fish_ybutton - 15, fish_xbutton + 40, fish_ybutton-5)
            #eye
            circle(1, (fish_xbutton - 12, fish_ybutton -7))
        if fishON == True:
            glPointSize(8)
            glColor3f(1,0,0)
            circle(16,(-ballbutton-30,150))
            circle(12,(-ballbutton-30,150))
            circle(8,(-ballbutton-30,150))
            circle(5,(-ballbutton-30,150))

def playroomtoys(): #anit
    global rightgoalpost
    #ball
    if ballbuttonON == True:
        glPointSize(4)
        glColor3f(1,0,0)
        circle(16,(ballx,-275))
        glColor3f(1,0,1)
        circle(11,(ballx,-275))
        glColor3f(1,0,0)
        circle(7,(ballx,-275))
        circle(4,(ballx,-275))
        #goalpost
        if goal==True:
            rightgoalpost = True
            glColor3f(0,0,0)
            draw_line(290,-290,290,-220)
            draw_line(250,-280,250,-210)
            draw_line(290,-220,250,-210)
        else:
            rightgoalpost = False
            glColor3f(0,0,0)
            draw_line(-290,-290,-290,-220)
            draw_line(-250,-280,-250,-210)
            draw_line(-290,-220,-250,-210)

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



def mouseFunc(button, state, x, y):#srijon
    global fishgamepoint, ballgamepoint, fish_x, fish_y, fishON, ballbuttonON, ballbutton, firework, fireworksCircleSpeed, fireworkCircleRadius, play, food_pan_empty, food, eating, cat_x,cat_y, nose, hungry, health, unhappy, sleep, day
    
    nose=(cat_x,cat_y-195)
    a = x-(600/2) #translate it to game cordinate
    b = (600 /2)-y
    zzz = False
    if play == True and width-370<=a<=width-320 and height-410<=b<=height-390: #ball game on off by button range
        if fishON == False and button == GLUT_LEFT_BUTTON and state == GLUT_DOWN and ballbuttonON == False:
            ballbuttonON = True
        elif fishON == False and button == GLUT_LEFT_BUTTON and state == GLUT_DOWN and ballbuttonON == True:
            ballbuttonON = False
            print("Ball Game Final Score: ",ballgamepoint)
            ballgamepoint=0
    if play == True and width-370<=a<=width-320 and height-460<=b<=height-420: #fish game by button range
        if fishON == False and button == GLUT_LEFT_BUTTON and state == GLUT_DOWN and ballbuttonON == False:
            fishON = True
        elif fishON == True and button == GLUT_LEFT_BUTTON and state == GLUT_DOWN and ballbuttonON == False:
            fishON = False
            print("Fishing Game Final Score: ",fishgamepoint)
            fishgamepoint = 0

 #eat or not eat xaxis = 300, yaxis = 300
    if play == False and (xaxis-80) <= a <= (xaxis-6) and -(yaxis-11) <= b <= -(yaxis-30)  and 170<=cat_x<=230: # food pan logic
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            if not food_pan_empty:
                if len(food) > 1 and hungry != 0:
                    eating=True
                    food.pop()
                    hungry=max(0,hungry-1)
                    health+=1
                    health=min(health,4)
                    if hungry==0:
                        health=5
                elif len(food) > 1 and hungry == 0: #moiukh
                    print("I am not hungry anymore.")
                elif len(food)==1:
                    food.pop()
                    hungry=max(0,hungry-1)
                    print("Oh no! Refill food")
                    food_pan_empty = True
                    eating=False
                elif len(food)==0:
                    food_pan_empty = True
                    eating=False
            else:#refil food
                food_pan_empty = False
                food.append((xaxis-67, -(yaxis-35)))
                food.append((xaxis-57, -(yaxis-35)))
                food.append((xaxis-47, -(yaxis-35)))
                food.append((xaxis-37, -(yaxis-35)))
                food.append((xaxis-27, -(yaxis-35)))
                food.append((xaxis-17, -(yaxis-35)))  
                food.append((xaxis-63, -(yaxis-45)))
                food.append((xaxis-53, -(yaxis-45)))
                food.append((xaxis-43, -(yaxis-45)))
                food.append((xaxis-33, -(yaxis-45)))
                food.append((xaxis-23, -(yaxis-45)))

    else:
        eating=False    

    if play == False and 0<=x<=100 and height-40<=y<=height and -xaxis+60 <=cat_x<-xaxis+160: # sleep logic
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            if day >= 0.4 and sleep == False:
                print("It's still day! You should playy!")
            elif unhappy == True:
                print("Eat first.")
            else:
                zzz = True
        if zzz == True and button == GLUT_LEFT_BUTTON and state == GLUT_DOWN and sleep == False:
            sleep = True
            cat_y += 20
            cat_x = -230
        elif sleep == True and button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            sleep = False
            cat_y -= 20
            if day <= 0.4:
                print('Sleep some more.')
    
   