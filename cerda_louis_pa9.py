# Name: Louis Cerda
# Class: CPSC 215
# Date: 4.25.22
# Assignment: Programming Assignment 9: Rover Map
# Description: rover map program that allows the user to move around the map and collect samples until water is found or the rover runs out of battery.



## Mars Rover map generator function

from operator import ge


def generateMap(seedrow, seedcol):
    #generate an empty map (all rust values are zero)
    map = [[0] * 20, [0] * 20, [0] * 20, [0] * 20, [0] * 20,
           [0] * 20, [0] * 20, [0] * 20, [0] * 20, [0] * 20,
           [0] * 20, [0] * 20, [0] * 20, [0] * 20, [0] * 20,
           [0] * 20, [0] * 20, [0] * 20, [0] * 20, [0] * 20]
    map[seedrow][seedcol] = 99  #value 99 is water
    for i in range(1, 6):
        for j in range(seedrow - i, seedrow + i + 1):
            for k in range(seedcol - i, seedcol + i + 1):
                if(j >= 0 and j < 20 and k >= 0 and k < 20):
                    if(map[j][k] == 0):
                        map[j][k] = 2**(5-i)
    return map


# calling the function this way will produce a map with the water located at coords 5,5 and
# rust levels decreasing outward to zero from that location:        






# classes required for this are rover and sample
# roverBot: takeSample(), move forward(), rotateRight(), rotateLeft(), charge()
class roverBot: # controls physical robot actions 
    def __init__(self):
        self.map1 = generateMap(5,5)
        self.currentMapCoordinates = [10,10]
        self.facing = 'N'
        self.battery = 10
        self.maxBattery = 15
        self.cargo = 0
        self.maxCargo = 7



#*************************************************************
# Function: takeSample(self,Sampler, bot)
# Description: takes a sample from the Sampler and adds it to the rover's cargo
# Input parameters: sampler object, rover object
# Returns: cargo
#*************************************************************
    def takeSample(self, Sampler, bot):
        #take a sample from the map
        #if the sample is rust, add to the rover's cargo
        #if the sample is water, do nothing
        #if the sample is empty, do nothing
        #return the sample's value
        if (self.currentMapCoordinates[0] >= 0 and self.currentMapCoordinates[0] < 20 and self.currentMapCoordinates[1] >= 0 and self.currentMapCoordinates[1] < 20):
            if (self.map1[self.currentMapCoordinates[0]][self.currentMapCoordinates[1]] == 99):
                self.cargo += 1
                Sampler.collect(Sampler,bot)
            elif (self.map1[self.currentMapCoordinates[0]][self.currentMapCoordinates[1]] == 0):
                pass
            elif (self.map1[self.currentMapCoordinates[0]][self.currentMapCoordinates[1]] > 0 and self.cargo < self.maxCargo):
                self.cargo += 1
                Sampler.collect(Sampler,bot)
        self.battery -= 1
        return self.cargo

#*************************************************************
# Function: moveForward(self)
# Description: moves forward one unit in the direction the rover is facing
# Input parameters: NA
# Returns: na
#*************************************************************
    def moveForward(self):
        #move the rover forward one space
        #if the rover is at the edge of the map, do nothing
        #return the new rover's position

        if (self.facing == 'N'):
            if (self.currentMapCoordinates[0] > 0):
                self.currentMapCoordinates = (self.currentMapCoordinates[0] - 1, self.currentMapCoordinates[1])
        elif (self.facing == 'S'):
            if (self.currentMapCoordinates[0] < 20):
                self.currentMapCoordinates = (self.currentMapCoordinates[0] + 1, self.currentMapCoordinates[1])
        elif (self.facing == 'E'):
            if (self.currentMapCoordinates[1] < 20):
                self.currentMapCoordinates = (self.currentMapCoordinates[0], self.currentMapCoordinates[1] + 1)
        elif (self.facing == 'W'):
            if (self.currentMapCoordinates[1] > 0):
                self.currentMapCoordinates = (self.currentMapCoordinates[0], self.currentMapCoordinates[1] - 1)
        self.battery -= 2
        # return self.currentMapCoordinates


#*************************************************************
# Function: rotateRight(self)
# Description: rotates the rover 90 degrees to the right
# Input parameters: NA
# Returns: side facing
#*************************************************************
    def rotateRight(self):
        #rotate the rover 90 degrees to the right
        #if the rover is at the edge of the map, do nothing
        #return the new rover's position
        if (self.facing == 'N'):
            self.facing = 'E'
        elif (self.facing == 'S'):
            self.facing = 'W'
        elif (self.facing == 'E'):
            self.facing = 'S'
        elif (self.facing == 'W'):
            self.facing = 'N'
        self.battery -= 1
        return self.facing


#*************************************************************
# Function: rotateLeft(self)
# Description: rotates the rover 90 degrees to the left
# Input parameters: NA
# Returns: side facing
#*************************************************************
    def rotateLeft(self):
        #rotate the rover 90 degrees to the left
        #if the rover is at the edge of the map, do nothing
        #return the new rover's position
        if (self.facing == 'N'):
            self.facing = 'W'
        elif (self.facing == 'S'):
            self.facing = 'E'
        elif (self.facing == 'E'):
            self.facing = 'N'
        elif (self.facing == 'W'):
            self.facing = 'S'
        self.battery -= 1
        return self.facing
        
#*************************************************************
# Function: charge(self)
# Description: charges the rover's battery one unit
# Input parameters: NA
# Returns: battery
#*************************************************************
    def charge(self):
        #charge the rover's battery
        #if the rover's battery is full, do nothing
        if(self.battery < self.maxBattery):
            self.battery += 1
        elif (self.battery == self.maxBattery):
            self.battery = self.maxBattery
        return self.battery
        

    






# roverSample: collect()
class roverSampler: # controls robot sampler actions
    def __init__(self):
        self.sampleSlots = 0
        self.maxSampleSlots = 7

        self.value = []

        self.cordsCollected1 = []
        self.cordsCollected2 = []
        self.cordsCollected3 = []
        self.cordsCollected4 = []
        self.cordsCollected5 = []
        self.cordsCollected6 = []
        self.cordsCollected7 = []
        


#*************************************************************
# Function: colelct(self, sampler, bot)
# Description: collects rust value and stores it and the cords at which they were at
# Input parameters: sampler object, rover object
# Returns: NA
#*************************************************************
    def collect(self, Sampler, bot):
        #collect a sample from the map
        if (self.sampleSlots < self.maxSampleSlots):
            if (self.sampleSlots == 0):
                self.cordsCollected1.append(bot.currentMapCoordinates)
                self.value.append(bot.takeSample(Sampler, bot))
                self.sampleSlots += 1
            elif (self.sampleSlots == 1):
                self.cordsCollected2.append(bot.currentMapCoordinates)
                self.value.append(bot.takeSample(Sampler, bot))
                self.sampleSlots += 1
            elif (self.sampleSlots == 2):
                self.cordsCollected3.append(bot.currentMapCoordinates)
                self.value.append(bot.takeSample(Sampler, bot))
                self.sampleSlots += 1
            elif (self.sampleSlots == 3):
                self.cordsCollected4.append(bot.currentMapCoordinates)
                self.value.append(bot.takeSample(Sampler, bot))
                self.sampleSlots += 1
            elif (self.sampleSlots == 4):
                self.cordsCollected5.append(bot.currentMapCoordinates)
                self.value.append(bot.takeSample(Sampler, bot))
                self.sampleSlots += 1
            elif (self.sampleSlots == 5):
                self.cordsCollected6.append(bot.currentMapCoordinates)
                self.value.append(bot.takeSample(Sampler, bot))
                self.sampleSlots += 1
            elif (self.sampleSlots == 6):
                self.cordsCollected7.append(bot.currentMapCoordinates)
                self.value.append(bot.takeSample(Sampler, bot))
                self.sampleSlots += 1
        else:
            pass


#*************************************************************
# Function: waterFound(self)
# Description: checks if water was found in the values collected
# Input parameters: NA
# Returns: boolean
#*************************************************************
    def waterFound (self):
        #check if the rover has collected a water sample
        if (self.value):
            if (self.value[0] == 99):
                return True
            else:
                return False



        








        



def main():
    print("Welcome to the Mars Rover Simulator!")
    print("This program will simulate a rover on Mars.")
    print("The rover will be able to move forward, rotate left, rotate right, collect a sample, and charge itself.")
    print("You are currently in a 20x20 map. The rover will start at the center of the map facing North.")
    print("The rover will have a battery of 10 units and have a max of 15 units.")
    print("The rover will have a maximum of 7 samples.")

    print("")
    print("")
    print("")

    rover = roverBot()
    Sampler = roverSampler()

    waterFound = False
    slotsFull = False

    while (waterFound == False and slotsFull == False):
        print("Please select what you would like to do:")
        print("Collect a sample: 1")
        print("Move forward one unit: 2")
        print("Rotate left and move forward: 3")
        print("Rotate right and move forward: 4")
        print("Charge rover one unit: 5")

        userInput = int(input("Please enter a number: "))

        if (userInput == 1):
            rover.takeSample(Sampler, rover)
            print("You have collected a sample.")
            print("You now have " + str(rover.cargo) + " samples.")
            print("You now have " + str(rover.battery) + " battery.")
            print("You are currently at " + str(rover.currentMapCoordinates) + ".")
            print("You are facing " + str(rover.facing) + ".")
        if (userInput == 2):
            rover.moveForward()
            print("You have moved forward.")
            print("You now have " + str(rover.cargo) + " samples.")
            print("You now have " + str(rover.battery) + " battery.")
            print("You are currently at " + str(rover.currentMapCoordinates) + ".")
            print("You are facing " + str(rover.facing) + ".")
        if (userInput == 3):
            rover.rotateLeft()
            rover.moveForward()
            print("You have rotated left and moved forward.")
            print("You now have " + str(rover.cargo) + " samples.")
            print("You now have " + str(rover.battery) + " battery.")
            print("You are currently at " + str(rover.currentMapCoordinates) + ".")
            print("You are facing " + str(rover.facing) + ".")
        if (userInput == 4):
            rover.rotateRight()
            rover.moveForward()
            print("You have rotated right and moved forward.")
            print("You now have " + str(rover.cargo) + " samples.")
            print("You now have " + str(rover.battery) + " battery.")
            print("You are currently at " + str(rover.currentMapCoordinates) + ".")
            print("You are facing " + str(rover.facing) + ".")
        if (userInput == 5):
            rover.charge()
            print("You have charged.")
            print("You now have " + str(rover.cargo) + " samples.")
            print("You now have " + str(rover.battery) + " battery.")
            print("You are currently at " + str(rover.currentMapCoordinates) + ".")
            print("You are facing " + str(rover.facing) + ".")
        if (Sampler.waterFound() == True):
            print("You have collected a water sample.")
            waterFound = True
        if (rover.cargo == rover.maxCargo):
            slotsFull = True

        if (rover.battery == 0):
            print("You have run out of battery.")
            print("You have lost the mission.")
            break


    





    

    return 0


main()