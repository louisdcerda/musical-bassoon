# Name: Louis Cerda
# Class: CPSC 215
# Date: 3.28.22
# Assignment: PA7
# Description: Encrypts or scrambles a word using command line args

import sys
import random
from random import shuffle

def main (argv):
    action = argv[1]
    r = keyGen()
    if (action == 'scramble'):
        scramble(argv[2])
    elif (action == 'encrypt'):
        encrypt(argv[2], r)



    
#*************************************************************
# Function: keyGen()
# Description: generates a key(random num from 1 to 25)
# Input parameters: NA.
# Returns: a random num 1 through 25
#*************************************************************
def keyGen ():
    randNum = random.randint(1,25)
    return randNum 


#*************************************************************
# Function: scramble()
# Description: scrambles a word)
# Input parameters: a command line arg
# Returns: prints out the scrambled word
#*************************************************************
def scramble (argv):
    word = list(argv)
    random.shuffle(word)
    str2 = ''
    for i in word:
        str1 = i
        str2 = str2 + str1
    print (str2)



#*************************************************************
# Function: encrypt()
# Description: generates a key(random num from 1 to 25)
# Input parameters: command line arg and a num(key)
# Returns: prints out encrypted text that is shifted using 
#           key and ascii table
#*************************************************************
def encrypt (argv, num):
    str2 = ''
    if (argv.isalpha()):
        for i in argv:
            if (i.islower()):
                j = ord(i) - 32
            j = ord(i)
            x = j + num
            if (x > 90):
                x -= 26
            w = chr(x)
            str1 = w
            str2 = str2 + str1 
    print (str2)
            



main(sys.argv)