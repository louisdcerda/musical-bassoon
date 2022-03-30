## CPSC 215 Spring 2022 exam 1 - 2/11/2022 - Pizza Planet ordering application
## You may work with a partner to write the indicated functions to get this application running 
## In each function, replace 'pass' with the body of the function that you write and add parameters as appropriate
## EACH PERSON SHOULD SUBMIT THEIR OWN COPY OF THE .PY FILE FOR GRADING PURPOSES
## Author #1: Louis Cerda
## Author #2: Hastin

import time
## 10 points - This function prompts the user to enter their first name, last name, and phone num, each stored in a separate variable.
## Input: none
## Return: the user's firstname, lastname, phone as a tuple of strings
def getCustomerInfo():
    name = input('What is your first name?')
    lastName = input('What is your last name?')
    phone = input('What is your phone number?')
    return name, lastName, phone


## 15 points - This function prompts the user to say what topping type they would like added WHILE they haven't reached the total num toppings
## It starts with a base pizza cost of $10 then adds $2.50 for each additional topping
## Input: number of toppings
## Return: total cost of this pizza
def createPizza():
    toppings = True
    totalCost = 10 
    while (toppings):
        added = input('What would you like as toppings? Write in NA for no more.')
        for topping in added:
            totalCost += 2.5
        if (added == 'NA'):
            toppings = False
    return float(totalCost)

## 5 points - This function displays the toppings your store offers
## Input: none
## Return: none
def displayToppingList():
    print('The toppings our store offers are: cheese, bacon, pepperoni, ham and pineapple.')

## 10 points - This function displays the total order cost and a msg that uses the customer's first and last name
## Input: first name, last name, order total amount
## Return: none
def displayOrderTotal(first, last, total):
    print('The total for your order would be: ', float(total), 'for ', str(first), str(last))

## 10 points - This function displays the menu options to the user (see pdf document) and prompts the user for their choice
## Input: none
## Return: user choice number
def displayOrderMenu():
    choice = input('The menu number choices are: 1. Display topping list, 2. Add a pizza to your order 3. Complete order and calculate total.')
    return int(choice)

## 15 points
def main():
    print('Welcome to Pizza Planet!')
    ## Initialize the order total to $0
    orderTotal = 0
    
    ## Get the customer's name and phone info with the getCustomerInfo() function
    ## e.g. first, last, phone = getCustomerInfo()
    
    
    name, lastName, phone = getCustomerInfo()

    ## Show the customer the Order Menu WHILE they haven't selected the 'complete order' option
    

    ## IF they chose 'display topping list' use the displayToppingList() function
    
    selection = displayOrderMenu()
    flag = True
    while (flag):
        if (selection == 1):
            displayToppingList()
            ask = input('Would you like the total? Y/N ')
            if(ask == 'Y'):
                displayOrderTotal(name, lastName, orderTotal)
                flag = False
        elif (selection == 2):
            orderTotal = createPizza()
            ask = input('Would you like the total? Y/N ')
            if(ask == 'Y'):
                displayOrderTotal(name, lastName, orderTotal)
                flag = False
        elif (selection == 3):
            displayOrderTotal(name, lastName, orderTotal)
            flag = False

    ## IF they chose 'add a pizza' , ask them how many toppings and then use the createPizza() function
    ## Be sure to add to their order total each time you use the createPizza() function
    
    ## Once the customer has selected 'complete order', use the displayOrderTotal() function
    

main()