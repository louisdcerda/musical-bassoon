/// Complete this file to implement the Robot Arena game

/* Developer comment block....who, when, what....*/

#include <iostream> //flush
#include <stdlib.h> //for system("clear")  or system("cls")
#include <unistd.h> //for sleep(), usleep()
using namespace std;

//declare a global constant for maximum health

const int max_health = 100;

// This function accepts no arguments
// It returns the amount of health points to be gained back
int repairDamage(void){
    // Randomly generate an integer between 2 and 5 
    // Return the number you've generated

    int repair = (rand() % 4) + 2;
    return repair; //this is just here so it compiles...return something meaningful :)
}


// This function accepts the name of the robot who is currently attacking
// It returns the amount of damage the attack does
int attack(string robot){
    
    // prompt the attacking robot (use the name passed into this function) to enter which attack type as a character (e.g. A, B, C..)
    // use a switch statement to execute the chosen attack type
    // the amount of damage done should be generated randomly inside each case
    // return the amount of damage done

    char attack_type;
    cout << robot << " please enter the attack type you want (A,B,C) ";
    cin >> attack_type;

    int attack;
    
    switch (attack_type){
        case 'A': attack = rand() % 10; break;
        case 'B': attack = (rand() % 10) + 5; break;
        case 'C': attack = (rand() % 10) + 10; break;
    }


    return attack; //this is just here so it compiles...return something meaningful :)
}


// This function accepts the winning robot's name. No return
void declareWinner(string robot){
    //print a message that the robot who was passed into this function is the winner
    cout << robot << ", you are the winner." << endl;
}


// This function accepts the number of the player who is choosing their name, 1 or 2
// It returns the chosen name.
string nameRobot(int num){
    //prompt the robot whose number was passed in to enter their player name 
    //return the chosen name
    // return "fluffybunny"; //this is just here so it compiles...return something meaningful :)

    cout << "Robot" << num << ", enter your player name.";
    string name;
    cin >> name;
    return name;
}


// This function takes the names of the two robot opponents and controls the main game flow. No return.
void spar(string robot1, string robot2){
    
    // start both players with the global constant maximum health you defined at the top

    sleep(1);
    cout << "\tReady?..." << flush;
    sleep(1);
    cout <<  "Spar!" << endl;
    sleep(1);
    int robot1_health = max_health;
    int robot2_health = max_health;
    
    // WHILE both players have >0 health:
        //display both players health points
        //give robot 1 a turn
            //robot 1 chooses to attack or repair
            //if they attack, reduce robot 2 health points using the attack() function
            //if they repair, increase robot 1 health points using the repairDamage() function

        //assuming robot2 is not out of points, give robot 2 a turn
            //robot 2 chooses to attack or repair
            //if they attack, reduce robot 1 health points using the attack() function
            //if they repair, increase robot 2 health points using the repairDamage() function

        //if either of the robots is out of points, use the declareWinner() function and exit the loop
    


    while (robot1_health > 0 && robot2_health > 0){
        cout << robot1 << " health is: " << robot1_health << endl;
        cout << robot2 << " health is: " << robot2_health << endl;


        // robot 1 turn
        string turn;
        cout << robot1 << " would you like to attack or repair? ";
        cin >> turn;
        if (turn == "attack"){
            int damage = attack(robot1);
            robot2_health -= damage;
        }else if(turn == "repair"){
            int repairHealth = repairDamage();
            robot1_health += repairHealth;
        }

        // robot 2 turn 
        cout << robot2 << " would you like to attack or repair? ";
        cin >> turn;
        if (turn == "attack"){
            int damage = attack(robot1);
            robot1_health -= damage;
        }else if(turn == "repair"){
            int repairHealth = repairDamage();
        }
        if(robot1_health <= 0){
            declareWinner(robot2);
        }
        if (robot2_health <= 0){
            declareWinner(robot1);
        }
    }
}
int main(){

    srand(time(0));  //seeding the random algorithm 

    cout << "Welcome to Robot Arena!!!\n\n";

    // let both players choose their robot name:
    string robot1 = nameRobot(1);
    string robot2 = nameRobot(2);
   
    // begin the battle:
    spar(robot1, robot2);

    return 0;
}