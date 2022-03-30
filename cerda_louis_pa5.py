# Name: Louis Cerda
# Class: CPSC 215
# Date: 2.18.22
# Assignment: PA5
# Description: mad lib generator that takes input from user and tells a story based on the template provided


def main():
    print('Welcome to Mad Lib Generator')

    ## function that does all the work in asking user questions
    readStory()

    print('Here is your Mad Lib:')

    ## opens the output file and reads out content (completed story)
    file_contents = open('lib_output.txt', 'r')
    contents = file_contents.read()
    print(contents)
    
    file_contents.close()



# Function: readStory()
# Description: opens input and output file and reads line by line determining if the question was asked and then outputting the appropriate answer
# Input: NA
# Returns: NA
def readStory():
    infile = open('lib_input.txt', 'r')
    outfile = open('lib_output.txt', 'w')


    # variables to check if the questions was asked if it was then 1 is added so the program knows not to ask again
    person1 = 0
    person2 = 0
    animal = 0
    noun = 0
    adverb = 0 
    length = 0 
    speed = 0
    verb = 0 
    adjEr = 0 
    adjective = 0 
    number = 0
    dist = 0 
    place = 0 
    typeAni = 0  


    # reading line by line from infile and checking for specific key words so the story flows
    for line in infile:
        
        if 'PERSON 1' in line:
            if (person1 == 0):
                story1 = input('What name would you like for person 1? ')
            outfile.write(story1)
            person1 += 1
        elif 'PERSON 2' in line:
            if (person2 == 0):
                story2 = input('What name would you like for person 2? ')
            outfile.write(story2)
            person2 += 1
        elif 'ANIMAL' in line:
            if (animal == 0):
                story3 = input('What animal would you like? ')
            outfile.write(story3)
            animal +=1
        elif 'NOUN' in line:
            if (noun == 0):
                story4 = input('What noun would you like? ')
            outfile.write(story4)
            noun += 1
        elif 'VERB' in line:
            if (verb == 0):
                story5 = input('What verb would you like? ')
            outfile.write(story5)
            verb += 1
        elif 'SPEED' in line:
            if (speed == 0):
                story6 = input('What speed with units would you like? ')
            outfile.write(story6)
            speed += 1
        elif 'ADVERB' in line:
            if (adverb == 0):
                story7 = input('What adverb would you like? ')
            outfile.write(story7)
            adverb += 1
        elif 'ADJECTIVE ENDING IN' in line:
            if (adjEr == 0):
                story8 = input('What adjective ending in er would you like? ')
            outfile.write(story8)
            adjEr += 1
        elif 'ADJECTIVE' in line:
            if (adjective == 0):
                story9 = input('What adjective would you like? ')
            outfile.write(story9)
            adjective += 1
        elif 'NUMBER' in line:
            if (number == 0):
                story10 = input('What number would you like? ')
            number += 1
            outfile.write(story10)
        elif 'DISTANCE' in line:
            if (dist == 0):
                story11 = input('What distance with units would you like? ')
            outfile.write(story11)
            dist += 1
        elif 'LENGTH' in line:
            if (length == 0):
                story12 = input('What length with units would you like? ')
            outfile.write(story12)
            length += 1
        elif 'PLACE' in line:
            if (place == 0):
                story13 = input('What place would you like? ')
            outfile.write(story13)
            place += 1
        elif 'TYPE OF ANIMAL' in line:
            if (typeAni == 0):
                story14 = input('What type of animal would you like? ')
            outfile.write(story14)
            typeAni +=1
        else:
            outfile.write(line) # if key word is not found then the line alone is outputted

    # conventional closing of files after use
    infile.close()
    outfile.close()

main()