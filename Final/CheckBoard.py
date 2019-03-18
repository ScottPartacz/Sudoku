# Scott Partacz 4/21/2118 ITMD 413 Final Project

import numpy

#Checks the rwos and columns to see fi there is any dups,
#then is checks each of the 9 sub grids of 3x3 to see if there is any dups
def checkboard (board) :
    sqaurecheck = []
    for row in board :
        if(len(row) != len(set(row))) :
            return False
    for column in board.T :
        if(len(column) != len(set(column))) :
            return False
    squaress = numpy.array(board).reshape(3,3,3,3).transpose((0,2,1,3))
    for squares in squaress :
        for square in squares :
            for a in range(3) :
                sqaurecheck.append(square[a][0])
                sqaurecheck.append(square[a][1])
                sqaurecheck.append(square[a][2])
            if(len(sqaurecheck) != len(set(sqaurecheck))) :
                    return False
            sqaurecheck.clear()
    return True
