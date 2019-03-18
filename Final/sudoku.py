# Scott Partacz 4/20/2018 ITMD 413 Final Project

import time
import os
from tkinter import *
from board import *
from win import *
import numpy
import random

def exit () :
    #Name,Date,time
    print (" ")
    print ("Scott Partacz")
    print ("Date:",time.strftime("%x"))
    print ("Current time:",time.strftime("%X"))
    os._exit(1)
    
def EasyLvl () :
    global start
    global board
    global root
    counter = 0
    board = createboard()
    start = numpy.array(board).reshape(81)
    while(counter < 46) :
        b = random.randint(0,80)
        if(start[b] != 0) :
            start[b] = 0
            counter = counter + 1
    root.destroy()
    root = buildFrame()
    #print(board) #for testing
    
def HardLvl () :
    global start
    global board
    global root
    counter = 0
    board = createboard()
    start = numpy.array(board).reshape(81)
    while(counter < 56) :
        b = random.randint(0,80)
        if(start[b] != 0) :
            start[b] = 0
            counter = counter + 1
    root.destroy()
    root = buildFrame()
    #print(board) for testing

def key(event) :
    global Key_pressed
    #checks to see if the key pressed is a number or a space (space is to erase a numebr from the baord)
    if((str.isdigit(event.keysym) and event.keysym != "0") or event.keysym == "space") :
        Key_pressed = event.keysym
        if(event.keysym == "space") :
           Key_pressed = " "
        print("you have selected: ",Key_pressed)
    
def callback(event):
    global Button_pressed
    global board
    global start
    btn = ""
    root.focus_set()
    Button_pressed = event.widget
    for i in str(Button_pressed) :
        if(i.isdigit()) :
           btn = btn + i
    if(btn == "") :
        btn = 1
    board = numpy.array(board).reshape(81)
    #checks for the right number
    if(Key_pressed == str(board[int(btn)-1])) :
        Button_pressed["text"] = Key_pressed
        start[int(btn)-1] = Key_pressed
    else :
        print("Incorrect spot")
        #checks to see if you solved the board
    if(CheckWin(start)) :
        print("!!!!You Have Solved The Board!!!!")
    
def buttonCommand(event):
    return None
        
def buildFrame () :
    global btn
    root = Tk()

    v = IntVar()
    
    root.title("Sudoku")

    #menu
    menu=Menu(root)
    file=Menu(menu)
    
    file.add_command(label="Easy Level", command=EasyLvl)
    file.add_command(label="Hard Level", command=HardLvl)
    file.add_command(label="Exit", command=exit)

    menu.add_cascade(label="Choose Difficulty", menu=file)
    root.config(menu=menu)

    #makes the buttons different colors to tell the differance in lines
    for rowindex in range (9):
        for colindex in range (9):
            if (rowindex in (0,1,2,6,7,8) and colindex in (3,4,5) or \
                (rowindex in (3,4,5) and colindex in (0,1,2,6,7,8))):
                    colour="light blue"
            else:
                colour="white"
                
            #builds the grid of buttons 9x9
            global i
            x = start[i]
            i = i+1
            if i == 81 :
                i = 0
            if(x == 0) :
                x = " "
            btn=Button(root, width=8, height=4, bg=colour, text=x, fg="black", command = buttonCommand(x))  
            btn.grid(row=rowindex+1, column=colindex+1, sticky=N+S+E+W)
            root.bind("<Key>", key)
            root.bind("<Button-1>", callback)

    return root

#start screen message
start=[" "," ","C","H","O","S","E"," "," ",
       " "," ","E","A","S","Y"," "," "," ",
       " "," ","O","R"," "," "," "," "," ",
       " "," ","H","A","R","D"," "," "," ",
       " "," ","T","O"," "," "," "," "," ",
       " "," ","G","E","T"," "," "," "," ",
       " "," ","S","T","A","R","T","E","D",
       " ",""," "," "," "," "," "," "," ",
       "B","Y",":","S","C","O","T","T"," ",]

#randomize the random seed
random.seed(time.time())
board = []
#for the grid of buttons
i = 0
Button_pressed = 0
Key_pressed = " "
root = buildFrame()

root.mainloop()




#Name,Date,time
print (" ")
print ("Scott Partacz")
print ("Date:",time.strftime("%x"))
print ("Current time:",time.strftime("%X"))
