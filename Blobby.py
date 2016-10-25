import Myro
from Myro import *
from Graphics import *
from random import *

width = 500
height = 500
sim = Simulation("Maze World", width, height, Color("gray"))

#outside walls
sim.addWall((10, 10), (490, 20), Color("black"))
sim.addWall((10, 10), (20, 490), Color("black"))
sim.addWall((480, 10), (490, 490), Color("black"))
sim.addWall((10, 480), (490, 490), Color("black"))

#blue spot
poly = Circle((50, 50), 45)
poly.bodyType = "static"
poly.color = Color("blue")
poly.outline = Color("black")
sim.addShape(poly)

#red spot
poly = Circle((450, 50), 45)
poly.bodyType = "static"
poly.color = Color("red")
poly.outline = Color("black")
sim.addShape(poly)

#green spot
poly = Circle((50, 450), 45)
poly.bodyType = "static"
poly.color = Color("green")
poly.outline = Color("black")
sim.addShape(poly)

#yellow spot
poly = Circle((450, 450), 45)
poly.bodyType = "static"
poly.color = Color("yellow")
poly.outline = Color("black")
sim.addShape(poly)

#purple spot
poly = Circle((250, 450), 45)
poly.bodyType = "static"
poly.color = Color("purple")
poly.outline = Color("black")
sim.addShape(poly)

#pink spot
poly = Circle((250, 50), 45)
poly.bodyType = "static"
poly.color = Color("pink")
poly.outline = Color("black")
sim.addShape(poly)

#white spot
poly = Circle((50, 250), 45)
poly.bodyType = "static"
poly.color = Color("white")
poly.outline = Color("black")
sim.addShape(poly)

#orange spot
poly = Circle((450, 250), 45)
poly.bodyType = "static"
poly.color = Color("orange")
poly.outline = Color("black")
sim.addShape(poly)

#begin simulation and sets robot's position
makeRobot("SimScribbler", sim)
sim.setPose(0, width/2, height/2, 0)

sim.setup()

# 1-RED
# 2-GREEN
# 3-BLUE
# 4-YELLOW

#The following is a helper function 
#Inputs: A picture and a color represented by the list above
#Returns the average x location of the color in the picture or -1 if the robot has found the color spot

def findColorSpot(picture, color):
    xPixelSum = 0
    totalPixelNum = 0
    averageXPixel = 0

    show(picture)

    for pixel in getPixels(picture):
        if(color == 1 and getRed(pixel) > 150 and getGreen(pixel) < 50 and getBlue(pixel) < 50):
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 2 and getRed(pixel) < 50 and getGreen(pixel) > 80 and getBlue(pixel) < 50):
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 3 and getRed(pixel) < 50 and getGreen(pixel) < 50  and getBlue(pixel) > 150):
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 4 and 254 > getRed(pixel) > 200 and 254> getGreen(pixel) > 200 and getBlue(pixel) == 0): 
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 5 and getRed(pixel) > 100 and getGreen(pixel) < 50 and getBlue(pixel) > 100): 
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 6 and getRed(pixel) > 200 and getGreen(pixel) > 100 and getBlue(pixel) > 150): 
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 7 and 270 > getRed(pixel) > 200 and 270> getGreen(pixel) > 200 and getBlue(pixel) > 200): 
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 8 and 250 > getRed(pixel) > 200 and 170 > getGreen(pixel) > 100 and getBlue(pixel) < 50): 
            xPixelSum += getX(pixel)
            totalPixelNum += 1
    if(totalPixelNum != 0):
        averageXPixel = xPixelSum/totalPixelNum

    #Handles the case where robot has found the spot if it is near it
    #If necessary adjust the value
    if(totalPixelNum/(getWidth(picture)*getHeight(picture)) > 0.21):
        averageXPixel = -1

    return averageXPixel


# Use the following integers for colors:
# 1-RED
# 2-GREEN
# 3-BLUE
# 4-YELLOW

######################Code Starts Here##################################
# Make sure to drag the picture window up so that you can see what Scribby has to say in the output!
NotherBlob = 1
import sys
while True:
    color=input("What color blob should I find?")
    y=color
    if color=="blue":
        color=int(3)
    if color=="red":
        color=int(1)
    if color=="green":
        color=int(2)
    if color=="yellow":
        color=int(4)
    if color=="purple":
        color=int(5)
    if color=="pink":
        color=int(6)
    if color=="white":
        color=int(7)
    if color=="orange":
        color=int(8)
    toTheRight=randrange(-15,-5)
    toTheLeft=randrange(5,15)
    turnBy(randrange(-30,90))
    def check():
        pic=takePicture()
        x=findColorSpot(pic,color)
        return x
    x=check()
    while x > -1:
        while 0 <= x < 96 or x > 160:
            if x==0:
                turnBy(randrange(-30,90))
                x=check()
            elif x < 96:
                turnBy(toTheLeft)
                x=check()
            elif x > 160:
                turnBy(toTheRight)
                x=check()
        while 96 <= x <= 160:
            forward (1,1)
            x=check()
    if x == -1:
        print("I have found the " + y + " blob! Blobby is a free elf!")
        NotherBlob = 0
        Blob=input("Shall I find another one? [Y/N]")
        if Blob=="Y":
            backward(1.5,2)
            continue
        if Blob== "N":
            NotherBlob = 0
            sys.exit()
            
             
            
       
        
    
    
    






