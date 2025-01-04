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
fireworkLst = []
food =[]
food.append((xaxis-67, -(yaxis-35)))
food.append((xaxis-57, -(yaxis-35)))
food.append((xaxis-47, -(yaxis-35)))
food.append((xaxis-37, -(yaxis-35)))
food.append((xaxis-27, -(yaxis-35)))
food.append((xaxis-17, -(yaxis-35)))

hungry = 10



'''cse423 algo to draw'''
def findzone(x1,y1,x2,y2):#srijon
    dx=x2-x1
    dy=y2-y1
    if abs(dx)>abs(dy):
        if(dx>=0 and dy>=0):
            zone=0
        elif(dx<=0 and dy>=0):
            zone=3
        elif(dx<=0 and dy<=0):
            zone=4
        elif(dx>=0 and dy<=0):
            zone=7
    else:
        if(dx>=0 and dy>=0):
            zone=1
        elif(dx<=0 and dy>=0):
            zone=2
        elif(dx<=0 and dy<=0):
            zone=5
        elif(dx>=0 and dy<=0):
            zone=6
    return zone

def zone0(zone,x,y):#srijon
    if zone==0:
        x1=x
        y1=y
    elif zone==1: 
        x1=y 
        y1=x 
    elif zone==2:    
        x1=y 
        y1=-x    
    elif zone==3: 
        x1=-x
        y1=y
    elif zone==4: 
        x1=-x
        y1=-y
    elif zone==5: 
        x1=-y
        y1=-x
    elif zone==6:    
        x1=-y
        y1=x    
    elif zone==7:     
        x1=x
        y1=-y
    return (x1,y1)

def originalzone(zone,x,y):#srijon

    if zone==0:
        x1=x
        y1=y
    elif zone==1:
        x1=y
        y1=x
    elif zone==2:
        x1=-y
        y1=x
    elif zone==3:
        x1=-x
        y1=y
    elif zone==4:
        x1=-x
        y1=-y
    elif zone==5:
        x1=-y
        y1=-x
    elif zone==6:
        x1=y
        y1=-x
    elif zone==7:
        x1=x
        y1=-y
    return (x1,y1)   

def draw_line(x1,y1,x2,y2): # srijon draw line
    global xaxis,yaxis
    zone=findzone(x1,y1,x2,y2)
    x1,y1=zone0(zone,x1,y1)
    x2,y2=zone0(zone,x2,y2)
    dx=x2 -x1
    dy=y2 -y1
    d= 2*dy -dx
    x=x1
    y=y1
    glBegin(GL_POINTS)
    while x <x2:
        xo,yo= originalzone(zone,x,y)
        glVertex2f(xo/xaxis, yo/yaxis) #
        x +=1
        if d<0:
            d+=2*dy
        else:
            d+=2*(dy- dx)
            y+=1
    glEnd()


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
    
    if width-370<=a<=width-320 and height-370<=b<=height-350: #play logic
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            if play == False:
                if unhappy == False:
                    if sleep==True:
                        print("To play, you need energy. Finish sleeping.")
                    else:
                        play = True
                else:
                    print("To play, you need to eat first.")
            else:
                play = False
                if fishON == True:
                    print("Fishing game Final Score: ", fishgamepoint)
                    fishON = False
                    fishgamepoint = 0
                ballbuttonON = False
    
    if play == True and button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN: #firework logic
       if  -width + 400 <= a <= width - 400 and height-600<=b<=height-400:
            fireworkLst.append([a, b, 3]) #initial radius 3
            if cat_y < 20:
                cat_y+=70
                glutTimerFunc(300, come_down, 0)








#sadman

sleep = True  
firework = True  
sleep = False
firework = False  


def circle(radius, center): #sadman
    d = 1 - radius  #decision var
    x = 0
    y = radius
    circlepoints(x, y, center)
    while x < y:
        if d < 0:
            d += 2 * x + 3
            x += 1
        else:
            d += 2 * x - 2 * y + 5
            x += 1
            y -= 1
        circlepoints(x, y, center)

def circlepoints(x, y, center):
    global xaxis, yaxis
    glBegin(GL_POINTS)
    x0 = x / xaxis
    y0 = y / yaxis
    ax = center[0] / xaxis
    ay = center[1] / yaxis
    glVertex2f(x0 + ax, y0 + ay)
    glVertex2f(y0 + ax, x0 + ay)
    glVertex2f(y0 + ax, -x0 + ay)
    glVertex2f(x0 + ax, -y0 + ay)
    glVertex2f(-x0 + ax, -y0 + ay)
    glVertex2f(-y0 + ax, -x0 + ay)
    glVertex2f(-y0 + ax, x0 + ay)
    glVertex2f(-x0 + ax, y0 + ay)
    glEnd()


def draw_cat():  #sadman
    global cat_x, cat_y, sleep, firework

    glColor3f(0, 0, 0)  #black

    #head
    glPointSize(1.5)
    circle(40, (cat_x, cat_y - 175))  

    # Eyes
    if firework:  
        print("The cat is excited by the fireworks!")
        glPointSize(2)
        draw_line(cat_x + 8, cat_y - 182, cat_x + 13, cat_y - 173)  
        draw_line(cat_x + 13, cat_y - 175, cat_x + 16, cat_y - 183)
        draw_line(cat_x - 8, cat_y - 182, cat_x - 13, cat_y - 173)  
        draw_line(cat_x - 13, cat_y - 173, cat_x - 18, cat_y - 182)

    elif sleep:  
        print("The cat is sleeping... Zzz")  
        glPointSize(2)
        draw_line(cat_x + 8, cat_y - 182, cat_x + 14, cat_y - 182)  
        draw_line(cat_x - 8, cat_y - 182, cat_x - 14, cat_y - 182)  

    else:  
        print("The cat is awake and calm.")  
        glColor3f(1, 1, 1)  
        glPointSize(2)
        circle(6, (cat_x - 15, cat_y - 180))  
        circle(6, (cat_x + 15, cat_y - 180))  

        glColor3f(0, 0, 0)  
        circle(3, (cat_x - 15, cat_y - 180))  
        circle(3, (cat_x + 15, cat_y - 180)) 

        glColor3f(1, 1, 1)  
        circle(1, (cat_x - 13, cat_y - 178)) 
        circle(1, (cat_x + 17, cat_y - 178))  







#basicdraw
def draw_foodpan():  #sadman
    global food_pan_empty, food, play, xaxis, yaxis 

    if play == False:  
        glPointSize(4)
        glColor3f(1, 0.2, 0.2)  #red
        draw_line(xaxis - 80, -(yaxis - 30), xaxis - 6, -(yaxis - 30))  #B
        draw_line(xaxis - 66, -(yaxis - 11), xaxis - 20, -(yaxis - 11))  #T
        draw_line(xaxis - 80, -(yaxis - 30), xaxis - 66, -(yaxis - 11))  #L
        draw_line(xaxis - 20, -(yaxis - 11), xaxis - 6, -(yaxis - 30))  #R

        #food
        glPointSize(3)
        glColor3f(0.26, 0.09, 0.09)  #Brown
        for item in food:
            circle(4, (item[0], item[1]))




def draw_bed():  #sadman
    global play

    if play == False:  
        glPointSize(5)
        glColor3f(0, 0, 0) 
        draw_line(xaxis - 590, yaxis - 580, xaxis - 500, yaxis - 580)  #b
        draw_line(xaxis - 590, yaxis - 550, xaxis - 590, yaxis - 590)  #l
        draw_line(xaxis - 500, yaxis - 580, xaxis - 500, yaxis - 590)  # Right edge

        
        glColor3f(0.4, 0.2, 0.05)  #brown
        draw_line(xaxis - 585, yaxis - 575, xaxis - 500, yaxis - 575)

        #pillow
        glColor3f(0.7, 0.2, 0.05)  #light brown
        glPointSize(3)
        circle(5, (xaxis - 582, yaxis - 567))  #pillow


def draw_window():  #sadman
    global day, play, d2n, n2d

    if play == False:  
        glColor3f(0, 0, 0)  
        glPointSize(2)

        #windowbox
        draw_line(-width + 400, height - 400, width - 600, height - 400)  #t
        draw_line(-width + 400, height - 600, width - 600, height - 600)  #b
        draw_line(-width + 400, height - 400, -width + 400, height - 600)  #l
        draw_line(width - 600, height - 400, width - 600, height - 600)  #r

        #sky
        if day > 0.9:  #day
            glColor3f(0, 0.7, 1)  #blue
        else:  #night
            g = max(0.1, day - 0.4)
            b = max(0.1, day - 0.2)
            glColor3f(0, g, b)  #light to dark gradually
        glPointSize(198)
        draw_line(-width + 500, height - 500, width - 699, height - 500)  #skyfill

        #sunmoon
        if day > 0.4:  #sun
            glColor3f(1, 1, 0)  #yellow
        else:  # moon
            glColor3f(0.8, 0.8, 1)  
        circle(15, (-width + 450, height - 450))  


def windowcross():  # sadman
    if play == False:  
        glColor3f(0, 0, 0)  
        glPointSize(1)

        #y
        draw_line(width - 700, height - 400, width - 700, height - 600)

        #x
        draw_line(-width + 400, height - 500, width - 600, height - 500)


def draw_fish():  # sadman
    global left, fish_x, fish_y
    if play == True and fishON == True:
        glPointSize(2)
        glColor3f(0.0, 0.0, 1.0)  #blue
        draw_line(fish_x - 15, fish_y, fish_x + 15, fish_y)
        draw_line(fish_x - 15, fish_y - 20, fish_x + 15, fish_y - 20)
        draw_line(fish_x - 15, fish_y, fish_x - 27, fish_y - 10)
        draw_line(fish_x - 15, fish_y - 20, fish_x - 27, fish_y - 10)
        draw_line(fish_x + 15, fish_y, fish_x + 40, fish_y - 15)
        draw_line(fish_x + 15, fish_y - 20, fish_x + 40, fish_y - 5)
        draw_line(fish_x + 40, fish_y - 15, fish_x + 40, fish_y - 5)
        #eye
        circle(1, (fish_x - 12, fish_y - 7))



      
def fish_animate(val):  # sadman
    global fish_x, fish_y, fishON, fishgamepoint, left
    if fishON == True:
        if left == False:
            fish_x -= 3  #move to left
        else:
            fish_x += 3  #move to right

        if fish_x > width - 350 or fish_x < width - 850:
            print("Game over")
            print("Final Fishing Score: ", fishgamepoint)
            fishON = False
            fishgamepoint = 0
            fish_x = random.uniform((xaxis / 2) + 100, (-xaxis / 2) - 100)
            if fish_x < 0:
                left = True
            else:
                left = False
            fish_y = -100

    glutTimerFunc(20, fish_animate, 0)
    glutPostRedisplay()


