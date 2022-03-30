# Name: louis cerda
# Class: Python Programming
# Date: 1.22.22
# Assignment: PA 2
# Description: ask the users for their codenames and deicides if they are real

#real codenames that will be compared to later in the program
realCodename = "specialAgent23"
# realCodename2 = "specialAgent0"
 
#asking the agents for their codenames
codename1 = input("What is the codename, agent 1? ")
codename2 = input("What is the codename, agent 2? ")


#compares each input and decides which is true and outputs the appropraite message
if codename1 and codename2 == realCodename:
    print("Both agents are real. You both have been granted access. Welcome.")
elif codename1 == realCodename:
    print("Only agent one is real. Agent two has been de-activated. Headquarters is being alerted.")
elif codename2 == realCodename:
    print("Only agent two is real. Agent one has been de-activated. Headquarters is being alerted.")
else:
    print("None of you are real agents. The system is being shut down. Headquarters is being alerted.")
