
# Name: Deepmala Bhomi              Date Assigned: 09/17/2019
#
# Course: 2000-44306                Date Due: 10/24/2019
#
# File name: programmingAssignment5.py
#
# Program Description: This program displays patterns made of circles and rectangles.
#                      This program displays pattern options that user can choose from.
#                      Once the choice is entered it will display the pattern made
#                      from the shape that user chose.
#                      









from graphics import *
#import functions from graphics.py


#defining a fuction which displays a pattern made up of circles.
def circlePattern(window):

    ###initilizing for loops to display circles in repetation.###
    ###radius decreases by 4 units in each repetation###
    
    for r in range(5,80,4):
        
        ###calling function that creates circles###
        
        #coordinates=centre of the output space.
        createCircle(window, 390, 200, r, '', 1, 'black')
        
        
    for r in range(5,80,4):
        
        #x-coordinates decreased by 100.
        #shifts circles 100 units left.
        createCircle(window, 290, 200, r, '', 1, 'blue')
        
        
    for r in range(5,80,4):
        
        #x-coordinates increased by 100.
        #shifts circles 100 units right.
        createCircle(window, 490, 200, r, '', 1, 'red')
        
        
    for r in range(5,80,4):
        
        #y-coordinates increased by 100.
        #shifts circles 100 units up.
        createCircle(window, 390, 300, r, '', 1, 'orange')
        
        
    for r in range(5,80,4):
        
        #y-coordinates decreased by 100.
        #shifts circles 100 units down.
        createCircle(window, 390, 100, r, '', 1, 'green')
        


#defining a fuction which displays a pattern made up of rectangles.        
def rectanglePattern(window):
   
    #declaring the coordinates of the centre rectangle for first loop.
    lowerX=350
    upperX=450
    lowerY=160
    upperY=260
    

    #creating a rectangle at the centre of the output rectangle space.
    #calling funtion that creates rectangles.
    createRectangle(window, lowerX,lowerY, upperX,upperY, "",1 ,"orange")


    ###initilizing for loops to display rectangles in repetation.### 
    for r in range(1,15,1):

        #creates rectangles of 2 colors in one loop.

        if r%2==0:      #executes if the iteration is even.
            
            #calling funtion that creates rectangles.
            createRectangle(window, lowerX,lowerY, upperX,upperY, "",1 ,"orange")
            
            #increasing the coordinates by 10 to create a pattern.
            lowerX+=10
            lowerY+=10
            upperX+=10
            upperY+=10
            
        if r%2!=0:      #executes if the iteration is odd.
            
            #calling funtion that creates rectangles.
            createRectangle(window, lowerX, lowerY, upperX  ,upperY, "",1 ,"aqua")
            
            #increasing the coordinates by 10 to create a pattern.
            lowerX+=10
            lowerY+=10
            upperX+=10
            upperY+=10


    #updating the co-ordinates of centre rectangle for 2nd loop.
    lowerX=350
    upperX=450
    lowerY=160
    upperY=260
            
    for r2 in range(1,15,1):
        
        #creates rectangles of 2 colors in one loop.
        if r2%2==0:     #executes if the iteration is even.
            
            #calling funtion that creates rectangles.
            createRectangle(window, lowerX,lowerY,upperX,upperY, "",1 ,"blue")
            
            #decreasing the coordinates by 10 to create a pattern.
            lowerX-=10
            lowerY-=10
            upperX-=10
            upperY-=10

            
        else:       #executes if the iteration is odd.
            
            #calling funtion that creates rectangles.
            createRectangle(window, lowerX,lowerY,upperX,upperY, "",1 ,"light green")
            
            #decreasing the coordinates by 10 to create a pattern.
            lowerX-=10
            lowerY-=10
            upperX-=10
            upperY-=10

            

    #updating the co-ordinates of centre rectangle for 3rd loop.
    lowerX=350
    upperX=450
    lowerY=160
    upperY=260
    
    for r in range(1,15,1):

        #creates rectangles of 2 colors in one loop.
        if r%2==0:      #executes if the iteration is even.
            
            #calling funtion that creates rectangles.
            createRectangle(window, lowerX,lowerY,upperX,upperY, "",1 ,"red")
            
            #decreasing the x-coordinates by 10 and
            #increasing y-cordinates by 10 to create a pattern.
            lowerX-=10
            lowerY+=10
            upperX-=10
            upperY+=10

            
        else:       #executes if the iteration is odd.
            
            #calling funtion that creates rectangles.
            createRectangle(window, lowerX,lowerY,upperX,upperY, "",1 ,"yellow")
            
            #decreasing the x-coordinates by 10 and
            #increasing y-cordinates by 10 to create a pattern.
            lowerX-=10
            lowerY+=10
            upperX-=10
            upperY+=10

            
    #updating the co-ordinates of centre rectangle for 4th loop.
    lowerX=350
    upperX=450
    lowerY=160
    upperY=260

    for r in range(1,15,1):

        #creates rectangles of 2 colors in one loop.
        if r%2==0:      #executes if the iteration is even.
            
            #calling funtion that creates rectangles.
            createRectangle(window, lowerX,lowerY,upperX,upperY, "",1 ,"purple")
            
            #increasing the x-coordinates by 10 and
            #decreasing y-cordinates by 10 to create a pattern.
            lowerX+=10
            lowerY-=10
            upperX+=10
            upperY-=10

            
        else:       #executes if the iteration is odd.
            
            #calling funtion that creates rectangles.
            createRectangle(window, lowerX,lowerY,upperX,upperY, "",1 ,"pink")
            
            #increasing the x-coordinates by 10 and
            #decreasing y-cordinates by 10 to create a pattern.
            lowerX+=10
            lowerY-=10
            upperX+=10
            upperY-=10

            

    #updating the co-ordinates of centre rectangle for 5th loop.
    lowerX=350
    upperX=450
    lowerY=160
    upperY=260
    

    for r in range(1,15,1):

            #calling funtion that creates rectangles.
            createRectangle(window, lowerX,lowerY,upperX,upperY, "",1 ,"black")
            
            #decreasing the size of the rectangle in each iteration.
            lowerX+=5
            lowerY+=5
            upperX-=5
            upperY-=5
            
            






#defining main function

def main():

    #create a program window
    window = createWindow("Shapes", 800,700, 'light pink')
    
    ###DISPLAY HEADER###

    #create box
    createRectangle(window, 250,630,550,680, "black",5 ,"orange")

    #create text for header
    createText(window, 400,655,"Pattern Creator", 20, 'bold')
    
    #create table to display types of pattern options that user can chose from.
    createTable(window, "light green",1,600,16,'bold'
                ,("Patterns","1. Circles   ","2. Rectangles"))

    ###GET USER INPUT###
    #ask user for their choice pattern option.
    userChoice= createInputBox(window, "Enter pattern choice (1 or 2): ",
                               450, "light blue", 14,"bold")

    #create rectangle space to display output pattern. 
    createRectangle(window, 10, 10, 790, 410, 'white',  1, 'black')

    
    ###determining which pattern to create depending on user input.###

    #if user inputs 1 it will display pattern created from circle.
    if userChoice=="1":

        #calling function which creates circle pattern.
        circlePattern(window)

    #if user inputs 2 it will display pattern created from rectangle.
    elif userChoice=="2":

        #calling function which creates rectangle pattern.
        rectanglePattern(window)

#calling main function       
main()

