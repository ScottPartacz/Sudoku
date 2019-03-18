# Scott Partacz 4/21/2118 ITMD 413 Final Project

import sqlite3
import time
import random
import numpy
import sys
from CheckBoard import * 

    
def createboard () :
    global board
    conn = sqlite3.connect('Valid_Boards.db')
    # x valid sudoku boards to be randomly picked then have the rows mixed up
    cursor = conn.cursor()

    sql = ( "SELECT * FROM Boards;")
    
    cursor.execute(sql)

    temp1 = cursor.fetchall()
    temp2 = []
    for a in range(len(temp1)) :
        temp2.append(temp1[a-1][0].split(","))
    for a in range(len(temp2)) :
        temp2[a-1] = list(map(int, temp2[a-1]))
    
             
    board = numpy.array(list(temp2[random.randint(0,len(temp2)-1)])).reshape(9,9)
    
    numpy.random.shuffle(board)
    
    
    #checks if the board is vaild if not recalls this method to start over
    if(checkboard(board) == False) :
        createboard()
    return (board)

random.seed(time.time())
board = []
a = createboard()

