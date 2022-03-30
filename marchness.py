# CPSC 215 Spring 2022 In-class exam 2 : Mad Marchness
# Flesh out the functions provided below to run your tournament and determine the champion!
# ***include names of all contributors here

import random


def play(bracket):
    ''' The incoming bracket is a list that has a matchup (a 2-element dictionary) at each index
        Each matchup dictionary has keys 'home' and 'away'
        Each home/away key is associated with a dictionary containing the string team 'name', the integer 'rank', and an integer 'score' value '''
    # (15 pts) For each dictionary, this function should randomly generate numbers to determine the updated score for each key
    #    the higher ranked team (meaning their rank number is LOWER) should generate a score between 60 and 85
    #    the lower ranked team should generate a score between 50 and 65, so higher rank is likely but not guaranteed to win

    for dic in range(bracket.size()):
        bracket[dic]['home']['score'] = randInt(60,85)
        bracket[dic]['away']['score'] = randInt(50,65)



def generateRound(bracket):
    ''' The incoming bracket is a list that has a matchup (a 2-element dictionary) at each index
        Each matchup dictionary has keys 'home' and 'away'
        Each home/away key is associated with a dictionary containing the string team 'name', the integer 'rank', and an integer 'score' value '''
    # (15 pts) This function should compare the scores of each matchup in each dictionary and then 
    #       pair up the winners with the neighboring winners. So the winner from the dictionary at element 0
    #       will play the winner from the dictionary at element 1, 2 pairs with 3, and so on to the end of the list/array
    #       Once again, the higher ranked team goes to key 'home'


    if one is greater than the other then it would be popped into another array

    if(bracket[])

    for dic in range(bracket.size()):
        if( bracket[dic]['home']['score'] < bracket[dic]['away']['score']):
            del bracket[dic]['home']
            # bracket[dic]['home'] = 'away'
        else:
            del bracket[dic]['away']
            # bracket[dic]['home'] = 'away'

    

    


def displayBracket(bracket):
    ''' The incoming bracket is a list that has a matchup (a 2-element dictionary) at each index
        Each matchup dictionary has keys 'home' and 'away'
        Each home/away key is associated with a dictionary containing the string team 'name', the integer 'rank', and an integer 'score' value '''
    # (15 pts) This function should display for the user the teams and their rankings and which team they are up against in this bracket
    for dic in range(8):
        print(bracket[dic]['home']['name'],bracket[dic]['home']['rank'], 'vs', bracket[dic]['away']['name'],bracket[dic]['away']['rank'])


def marchness():
    ''' Here's the field of competitors (a dictionary) - with some creative license
        The keys are team names and the values are rankings. Lower numbers are 'higher' rankings: '''

    tournament = {'Gonzaga': 1, 'Auburn': 2, 'Arizona': 3, 'Kansas': 4, 'Baylor': 5, 'Kentucky': 6, 'Purdue': 7, 'Duke': 8,
                 'Villanova': 9, 'Texas Tech': 10, 'Tennessee': 11, 'Illinois': 12, 'Wisconsin': 13, 'UCLA': 14, 'Providence': 15, 'St. Marys': 16}    
    # (10 pts) First, fill round (a list or array) with matchups (dictionaries). Each matchup dictionary has keys 'home' and 'away'
    #      and each key is associated with a dictionary containing the string team 'name', the integer 'rank', and an
    #      integer 'score' value that is set to zero   i.e. round = [{'home':{'name':'Zags', 'rank': 1, 'score': 0}, 
    #                                                                 'away':{'name':'St. Marys', 'rank':16, 'score':0},
    #                                                                {'home':...},
    #                                                                 'away':...}...]

    
    round0 = [{'home':{'name': 'Gonzaga', 'rank': 1, 'score': 0}, 'away':{'name': 'Saint Marys', 'rank': 16, 'score': 0}}, 
                {'home':{'name': 'Auburn', 'rank': 2, 'score': 0}, 'away':{'name': 'Providence', 'rank': 15, 'score': 0}},
                {'home':{'name': 'Arizona', 'rank': 3, 'score': 0}, 'away':{'name': 'UCLA', 'rank': 14, 'score': 0}},
                {'home':{'name': 'Kansas', 'rank': 4, 'score': 0}, 'away':{'name': 'Wisco', 'rank': 13, 'score': 0}},
                {'home':{'name': 'Baylor', 'rank': 5, 'score': 0}, 'away':{'name': 'Illinois', 'rank': 12, 'score': 0}},
                {'home':{'name': 'Kentucky', 'rank': 6, 'score': 0}, 'away':{'name': 'Tennessee', 'rank': 11, 'score': 0}},
                {'home':{'name': 'Purdue', 'rank': 7, 'score': 0}, 'away':{'name': 'Texas Tech', 'rank': 10, 'score': 0}},
                {'home':{'name': 'Duke', 'rank': 8, 'score': 0}, 'away':{'name': 'Villanova', 'rank': 9, 'score': 0}}]


    for i in 4:      
        displayBracket(round0)
        play(round0)
        generateRound(round0)



                    

    # The highest rank should match up with the lowest rank, then the next highest with the next lowest, etc.
    # In each pair, the highest ranked team should be used for the 'home' team and the lowest ranked should be the 'away' team
    # (15 pts) Tournament loop:
    #       Display the current matchups using the displayBracket() function 
    #       To play the round, send the round to the play() function
    #       Then send the round to the generateRound() function to generate the next level bracket from the winners
    # You may either customize your play() function to handle every size of round, or add an additional final() function to play the last game




   
def main():
    # This function does not need to be changed
    print('Welcome to Mad Marchness!')
    marchness()

main()