# Louis Cerda
# Python Programming course CPSC 215
# 2.7.22
# PA 3
# Description: Generates a random Num and makes the user guess it with hints after each guess. Only 3 hints though.


# libary for random number generation and provides perameters for it (1-20)
import random
randNum1 = random.randint(1,20)

# Function: doubleNum()
# Description: doubles the mystery number
# Input: random number that is generated
# Returns: random number times 2
def doubleNum(inputNum):
    return inputNum * 2

# Function: subNum()
# Description: that substracts 3 from the mystery number
# Input: random number that is generated
# Returns: random number minus 3

def subNum(inputNum):
    return inputNum - 3

# Function: evenCheck()
# Description: Determines if the mystery number is even or odd
# Input: random number that is generated
# Returns: "Even" or "Odd" depending on if the number mod 2 equals 0
def evenCheck(inputNum):
    if (inputNum % 2 == 0): 
        return str('even.')
    else: 
        return str('odd.')
        

# Function: checkToSleep()
# Description: Checks if the mystery number is guessed and if so congragulates the user
# Input: The users guess
# Returns: Print statement if the guess equals the random num generated and quits the program
def checkToSleep (inputNum):
    if (inputNum == randNum1):
        print('Congratulations, the mystery number is: ' + str(randNum1))
        quit()

# Function: main()
# Description: where all the work is done for this program
# Input: None
# Returns: None
def main():
    # first hint
    print ('Here is your first hint, the number minus 3 equals:', int(subNum(randNum1)))
    # print(subNum(randNum1))
    userGuess = input('Enter your guess:')
    checkToSleep(userGuess)

    # second hint
    print('Here is your next hint, the number doubled is:', int (doubleNum(randNum1)))
    # print(doubleNum(randNum1))
    userGuess = input('Enter your guess:')
    checkToSleep(userGuess)

    # last hint
    print('Here is your last hint, the number is:', (evenCheck(randNum1)))
    # evenCheck(randNum1)
    userGuess = input('Enter your guess:')
    checkToSleep(userGuess)

    # message if they did not guess the hint
    print('You did not guess the mystery number. :( ')


main()

