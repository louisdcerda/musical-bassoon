### Complete this file to implement the Robot Arena game

''' Developer comment block....who, when, what...'''


# Name: Louis Cerda
# Class: CPSC 215
# Date: 2.17.22
# Assignment: PA4
# Description: Lets two users spar using attack and repair moves and declares the winner
   
from os import system  # for system("clear") or system("cls")
import random
from time import sleep

#declare a global 'constant' for maximum health

MAXHEALTH = 100

# This function accepts no arguments
# It returns the amount of health points to be gained back
def repairDamage():
    # Randomly generate an integer between 2 and 5 
    # Return the number you've generated
    randNum = random.randint(2,5)
    return randNum


# This function accepts the name of the robot who is currently attacking
# It returns the amount of damage the attack does
def attack(robot):
    # prompt the attacking robot (use the name passed into this function) to enter which attack type as a character (e.g. A, B, C..)
    # use an if statement (or other ..) to execute the chosen attack type
    # the amount of damage done should be generated randomly and the range should vary by attack type
    # return the amount of damage done

    attackType = input(robot + 'which attack type would you like to use? (A, B, C) ')
    if (attackType == 'A' or attackType == 'a'):
        randNum = random.randint(5,13)
        return randNum
    elif (attackType == 'B' or attackType == 'a'):
        randNum1 = random.randint(18,21)
        return randNum1
    elif (attackType == 'C' or attackType == 'c'):
        randNum2 = random.randint(13,17)
        return randNum2

    pass


# This function accepts the winning robot's name. No return
def declareWinner(robot):
    # print a message that the robot who was passed into this function is the winner
    print(robot, 'is the winner!')


# This function accepts the number of the player who is choosing their name, 1 or 2
# It returns the chosen name.
def nameRobot(num):
    # prompt the robot whose number was passed in to enter their player name 
    # return the chosen name
    playerName = input('User '+ str(num)+ ' please enter your player name: ')
    return playerName


# This function takes the names of the two robot opponents and controls the main game flow. No return.
def spar(robot1, robot2):
    
    # start both players with the global constant maximum health you defined at the top
    sleep(1)
    print( "\tReady?...", flush = True, end = ' ')
    sleep(1)
    print( "Spar!")
    sleep(1)
    robot1Health = MAXHEALTH
    robot2Health = MAXHEALTH
      
    # WHILE both players have >0 health:
        #display both players' health points
        #give robot 1 a turn
            #robot 1 chooses to attack or repair
            #if they attack, reduce robot 2 health points using the attack() function
            #if they repair, increase robot 1 health points using the repairDamage() function

        #assuming robot2 is not out of points, give robot 2 a turn
            #robot 2 chooses to attack or repair
            #if they attack, reduce robot 1 health points using the attack() function
            #if they repair, increase robot 2 health points using the repairDamage() function

        #if either of the robots is out of points, use the declareWinner() function and exit the loop

    #end spar function

    while (robot1Health and robot2Health > 0):
        print('Health for ',robot1,'is: ', robot1Health,'. Health for ', robot2, ' is: ', robot2Health, '.')
        robot1Turn = input(robot1 + ' would you like to attack or repair? ')
        if(robot1Turn == 'attack'):
            attack1 = attack(robot1)
            robot2Health -= attack1
            # print(robot2, 'health is: ', robot2Health)
        elif(robot1Turn == 'repair'):
            if (robot1Health < MAXHEALTH):
                repair = repairDamage()
                robot1Health += repair
                # print(robot1, ' your health is now: ', robot1Health)
        robot2Turn = input(robot2 + ' would you like to attack or repair? ')
        if(robot2Turn == 'attack'):
            attack2 = attack(robot2)
            robot1Health -= attack2
            # print(robot1, ' your health is now: ', robot1Health)
        elif(robot2Turn == repair):
            repair = repairDamage()
            robot2Health += repair
            # print(robot2, ' your health is now: ', robot2Health)
        if ( robot1Health <= 0):
            declareWinner(robot2)
            break
        elif(robot2Health <= 0):
            declareWinner(robot1)
            break


def main():

    print( "Welcome to Robot Arena!!!\n\n")

    #let both players choosed their robot name
    robot1 = nameRobot(1)
    robot2 = nameRobot(2)
    
    #begin the battle
    spar(robot1, robot2)

main()