# Name: Louis Cerda
# Class: CPSC 215
# Date: 4.5.22
# Assignment: Programming Assignment 8: Excerpt Analysis
# Description: 


#*************************************************************
# Function: countWords()
# Description: counts the amount of words in each exceprt
# Input parameters: excerpt name
# Returns: the number of words in text
#*************************************************************
def countWords (excert): #counts the amount of words in each expert
    count = 0 
    with open(excert,'r') as file1:
        for line1 in file1: 
            for word in line1.split():
                if word.isalpha():
                    count += 1
    file1.close()
    return count




#*************************************************************
# Function: uniqueWords(excert)
# Description: counts the number of unique words in given exceprt
# Input parameters: excerpt name
# Returns: the number of unique words in given text
#*************************************************************
def uniqueWords (excert):
    set1 = set()
    count = 0

    with open(excert,'r') as file: #opening file
        #reading word by word 
        for line in file:    
            for word in line.split():
                if word not in set1: # checking if word is not in set. making it a unique word
                    if (word.isalpha()):
                        set1.add(word) 
                        count += 1
    # print(set1)
    file.close()
    return count



#*************************************************************
# Function: commonWords()
# Description: counts the number of unique words in given exceprt
# Input parameters: NA
# Returns: the number of unique words in given text
#*************************************************************
def commonWords ():
    count = 0
    set1 = set()

    with open('grisham1.txt','r') as file1: #opening file1
        with open('grisham2.txt','r') as file2: #opening file2
        #reading word by word 
            for line in file1:    
                for word in line.split():
                    if word not in set1:
                        if (word.isalpha()):
                            set1.add(word)

            for line2 in file2:    
                for word2 in line2.split():
                    if word2 in set1:
                        if (word2.isalpha()):
                            count += 1
    file1.close()
    file2.close()
    return count


#*************************************************************
# Function: generalUniqueWordsExcerpt1()
# Description: counts the number of unique words in exceprt 1
# Input parameters: NA
# Returns: the number of unique words that can only be found in excerpt 1
#*************************************************************
def generalUniqueWordsExceprt1 ():
    count = 0
    set1 = set()

    with open('grisham1.txt','r') as file1:
        with open('grisham2.txt','r') as file2:
        
            for line in file1:    
                for word in line.split():
                    if (word.isalpha()):
                        count += 1
                        set1.add(word)

            set2 = set1

            for line1 in file2:    
                for word1 in line1.split():
                    if word1 in set1:
                        if (word1.isalpha()):
                            set2.remove(word1)
                            count -= 1
    # print (set2)
    file1.close()
    file2.close()
    return count


#*************************************************************
# Function: generalUniqueWordsExcerpt2()
# Description: counts the number of unique words in exceprt 2
# Input parameters: NA
# Returns: the number of unique words that can only be found in excerpt 2
#*************************************************************
def generalUniqueWordsExceprt2 ():
    count = 0
    set1 = set()

    with open('grisham2.txt','r') as file1:
        with open('grisham1.txt','r') as file2:
        
            for line in file1:    
                for word in line.split():
                    if (word.isalpha()):
                        count += 1
                        set1.add(word)

            set2 = set1

            for line1 in file2:    
                for word1 in line1.split():
                    if word1 in set1:
                        if (word1.isalpha()):
                            set2.remove(word1)
                            count -= 1
    # print (set2)

    file1.close()
    file2.close()
    return count
    




#*************************************************************
# Function: wordLen (excerpt)
# Description: averages out the length of each word in an excerpt
# Input parameters: exceprt text name
# Returns: the average length of words in an excerpt
#*************************************************************
def wordLen (excerpt):
    count = 0
    set1 = set()

    with open(excerpt,'r') as file:
       
        for line in file:    
            for word in line.split():
                if (word.isalpha()):
                    if word not in set1: 
                        count += 1
                        set1.add(word)
        
        length = 0 
        for word1 in set1:
            if (word1.isalpha()):
                for length1 in word1: 
                    length += 1 

    avgLen = length/count

    file.close()
    return avgLen


def main():
    print("The number of words in grisham1 are: " + str(countWords('grisham1.txt')))
    print("The number of words in grisham2 are: " + str(countWords('grisham2.txt')))

    print("The number of words that are unique in grisham1 are: " + str(uniqueWords('grisham1.txt'))) 
    print("The number of words that are unique in grisham2 are: " + str(uniqueWords('grisham2.txt'))) 
    
    print("The number of words that are common in grisham1 and grisham2 are: " + str(commonWords())) 

    print("The number of words that are common to grisham1 are: " + str(generalUniqueWordsExceprt1())) 
    print("The number of words that are unique to grisham2 are: " + str(generalUniqueWordsExceprt2())) 

    print("The average word length in grisham1: " + str(wordLen('grisham1.txt'))) 
    print("The average word length in grisham2: " + str(wordLen('grisham2.txt'))) 
main()