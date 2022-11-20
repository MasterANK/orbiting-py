from turtle import *
import math
print("Welcome to Planet Sandbox Simulation")
print("-"*40)

n = int(input("""Enter 1 to run Sample 1
Enter 2 to run Sample 2
Enter 3 to run Sample 3
Enter 4 or anything to run the custom simulation

Enter Input: """))
if n == 1: #Sample 1
    Emass = 59         
    Smass = 1          
    G = 59             
    sdistance = 100     
    total_fx,total_fy = 0,0
    xac,yac = 0,7.68
    print("""Please looks at the turtle window. (check the taskbar if it is not visible)

Variables:
Mass of Earth: 59
Mass of Sattelite: 1
Universal Gravitation Constant: 59
Distance between the bodies: 100
Y-axis Acceleration: 7.69

In this Sample you can observe how distance affects the speed of the orbiting sattelight
""")
elif n == 2: #Sample 2
    Emass = 290         
    Smass = 150          
    G = 50             
    sdistance = 200     
    total_fx,total_fy = 0,0
    xac,yac = 0,7
    print("""Please looks at the turtle window. (check the taskbar if it is not visible)

Variables:
Mass of Earth: 290
Mass of Sattelite: 150
Universal Gravitation Constant: 50
Distance between the bodies: 200
Y-axis Acceleration: 7

In this Sample you can observe fast orbiting sattelight can be.""")
elif n == 3: #Sample 3
    Emass = 100         
    Smass = 50         
    G = 200             
    sdistance = 200     
    total_fx,total_fy = 0,0
    xac,yac = 0,7
    print("""Please looks at the turtle window. (check the taskbar if it is not visible)

Variables:
Mass of Earth: 100
Mass of Sattelite: 50
Universal Gravitation Constant: 200
Distance between the bodies: 200
Y-axis Acceleration: 7

In this Sample you can observe the orbits of orbiting sattelight can move.""")
else:
    print('note: Its a sandbox simulation and so feel free to enter any numeric value you want')
    Emass = int(input("Enter Mass of Earth: "))         
    Smass = int(input("Enter Mass of Sattelite: "))       
    G = int(input("Enter a value for universal gravitation constant: "))          
    sdistance = int(input("Enter the distance between the bodies: "))     
    total_fx,total_fy = 0,0
    yac = int(input("""
In order to get any thing into motion you must give it some acceleration
Enter the value for acceleration in y-axis: """))
    xac = 0

def planet(x,y,col,r,mass):
    t = Turtle()
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.shape("circle")
    t.pencolor(col)
    t.fillcolor(col)
    t.turtlesize(r,r,r)
    return t

def movement(earth,satellite):
    global total_fx, total_fy, xac, yac
    rx = earth.xcor() - satellite.xcor()
    ry = earth.ycor() - satellite.ycor()
    r = math.sqrt(rx**2 + ry**2)
    
    theta = math.atan2(ry,rx)
    f = (G * Emass * Smass)/(r**2)
    
    fx = f*math.cos(theta)
    fy = f*math.sin(theta)
    total_fx = fx ; total_fy = fy
    xac += total_fx/Smass ; yac += total_fy/Smass
    
    xdis = satellite.xcor() + xac
    ydis = satellite.ycor() + yac
    satellite.setpos(xdis,ydis)
# Code by Ankit Aggarwal     
screensize(800,500)
Screen().colormode(255)
Screen().bgcolor("black")

earth = planet(0,0,col="Blue",r=2,mass = Emass)
satellite = planet(sdistance,0,col=(254,252,215),r=0.5,mass = Smass) 
i = True
while i:
    try:
        movement(earth,satellite)
    except:
        i = False

print("success")

#licenced by Ankit Aggarwal(MasterAnk15) 

