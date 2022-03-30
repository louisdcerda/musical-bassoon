# Name: Louis Cerda
# Class: CPSC 215
# Date: 3.16.22
# Assignment: PA6
# Description: creating a 2 player game of connect four 


import numpy

def main():
    while not (hasfour()):
        playConnectFour()
    print('Congrats!')
    
boardE = numpy.array(   [['-','-','-','-','-','-','-'],
                            ['-','-','-','-','-','-','-'],
                            ['-','-','-','-','-','-','-'],
                            ['-','-','-','-','-','-','-'],
                            ['-','-','-','-','-','-','-'],
                            ['-','-','-','-','-','-','-']])


#*************************************************************
# Function: playConnectFour()
# Description: This function kick starts the game
# Input parameters: NA
# Returns: NA
#*************************************************************
def playConnectFour():
    displayBoard()
    placeChip()


#*************************************************************
# Function: displayBoard()
# Description: This function displays the playing board
# Input parameters: NA
# Returns: NA
#*************************************************************
def displayBoard():
    print(boardE)
    # displays an empty board




#*************************************************************
# Function: placeChip()
# Description: This function places a chip in the choice of the players column
# Input parameters: NA
# Returns: NA
#*************************************************************
def placeChip():

    colChoiceX = int(input('Player x please enter what col you would like to choose.'))
    colChoiceO = int(input('Player o please enter what col you would like to choose.'))
    
    numX = 0
    numO = 0

    while (boardE[numX,colChoiceX] == '-'):
        numX +1
    boardE[numX,colChoiceX] = 'x'

    while (boardE[numO,colChoiceO] == '-'):
        numO +1
    boardE[numO,colChoiceO] = 'o'




#*************************************************************
# Function: hasfour()
# Description: This function checks to see if any combination of 4 in a row is achieved
# Input parameters: NA
# Returns: boolean; true to signal game has ended, false to signal game to keep going
#*************************************************************
def hasfour():
    passx = 0
    passo = 0
    cols = 0
    rows = 0

    if (passo != 4 and passx != 4):
        while (cols != 7):
            while (rows != 6):
                if (boardE[rows, cols] == 'x'):
                    passx +1
                    rows +1
                else:
                    passx = 0
                if (boardE[rows, cols] == 'o'):
                    passo +1
                    rows +1
                else:
                    passo = 0
            cols +1
    # goes through the board to check for a vert win


    cols, rows = 0
    # resets the passes that are used for searching 

    if (passo != 4 and passx != 4):
       while (rows != 6):
            while (cols != 7):
                if (boardE[rows, cols] == 'x'):
                    passx +1
                    cols +1
                    break
                else:
                    passx = 0
                if (boardE[rows, cols] == 'o'):
                    passo +1
                    cols +1
                    break
                else:
                    passo = 0
            rows +1
    # checks for a horz win



    if (passx == 4):
        print('Player x has won!')
        return true
    # checks to see if player x has won

    if (passo == 4):
        print('Player o has won!')
        return true
    # checks to see if player o has won

    
    flag = true
    while (flag):
        for i in range(6):
            for j in range(7):
                if (boardE[i][j] == '-'):
                    flag = false
                    break
    # checks for gameover board
    

    rowCord = 0
    colCord = 0
    for i in range(6):
        for j in range(7):
            if (boardE == 'x' or boardE == 'o'):
                rowCord = i
                colCord = j
                break
    # gives starting point to check for diagonal wins

    rowCord1X = rowCord
    colCord1X = colCord

    rowCord1O = rowCord
    colCord1O = colCord

    rowCord1OD = rowCord
    colCord1OD = colCord


    passs = 0
    while (boardE[rowCord][colCord] == 'x'):
        passs +1
        rowCord +1
        colCord +1
        if (passs == 4):
            print('Player x has won!')
            return true 
            break
    # checks for diagonal down sloping left win for 'x'

    passs = 0
    while (boardE[rowCord][colCord] == 'o'):
        passs +1
        rowCord1D +1
        colCord1D +1
        if (passs == 4):
            print('Player o has won!')
            return true 
            break
    # checks for diagonal down sloping left win for 'x'


    passs = 0
    while (boardE[rowCord][colCord] == 'x'):
        passs +1
        rowCord1X +1
        colCord1X -1
        if (passs == 4):
            print('Player x has won!')
            return true 
            break
    # checks for diagonal upward sloping right win for 'x'


    passs = 0
    while (boardE[rowCord][colCord] == 'o'):
        passs +1
        rowCord1O +1
        colCord1O -1
        if (passs == 4):
            print('Player o has won!')
            return true 
            break
    # checks for diagonal upward sloping right win for 'o'

                
    return false
    # since there is no four 
    





main()