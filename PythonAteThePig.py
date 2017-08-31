__author__ = 'Alex'
#imports the random libraries
import random
#global variable that gets a random int from 20 to 100 for the score
win = random.randint(20, 100)

#roll dice method that rolls a 6 sided dice
def roll_dice():
    dice = random.randint(1,6)
    return dice

#player roll method to loop a players turn
def player_roll():
    #two variables that holds the count, and to hold a response
    counter = 0
    response = ""

#while the response is not equal to "HOLD" the loop will loop
    while response != "HOLD":
        #gets the dice roll random int
        #then prints it
        diceRoll = roll_dice()
        print("Dice Roll: ", diceRoll)
        #if the dice is one the count is returned to the player at 0
        if diceRoll == 1:
            counter = 0
            print("Your Total this turn: ", counter)
            return counter

        #else the player can continue to roll, or hold to end turn
        #returns counter if the response is "HOLD"
        else:
            counter += diceRoll
            print("Your Total this turn: ", counter)
            response = input('Type "HOLD" to end turn, type "ROLL" to roll again: ').upper()
            if response == "HOLD":
                return counter

#defines main function
def main():
    #variables to hold player1 total and player2 total
    #another variable to count turns
    player1Total = 0
    player2Total = 0
    turnCounter = 1
    #prints the amount needed to win from the win global variable
    print("To Win You Need ", win, " Points\n GO!!! \n")

    #while the player is less than the win, it will continue to loop
    while player1Total < win or player2Total < win:
        #prints off turn number, and the player scores for each iteration of the loop
        print("Turn ", turnCounter, "___________________________________________________")
        print("Player1 Score: ", player1Total)
        print("Player2 Score: ", player2Total)
        print()

        #prints the player1 roll information
        print("Player1 Rolls...")
        player1 = player_roll()
        player1Total += player1
        #if the player wins, it prints off the scores and posts the winner
        if player1Total >= win:
            print()
            print("Player1: ", player1Total, " WINNER!!!")
            print("Player2: ", player2Total, " FAILURE!!! ")
            break

        print()

        #prints player2 roll information
        print("Player2 Rolls...")
        player2 = player_roll()
        player2Total += player2
        #if the player wins, it prints off the scores and posts the winner
        if player2Total >= win:
            print()
            print("Player2: ", player2Total, " WINNER!!!")
            print("Player1: ", player1Total, " FAILURE!!!")
            break

        print()

        #adds one to the counter, iterates by one each loop/turn
        turnCounter += 1

#calls main function
main()
