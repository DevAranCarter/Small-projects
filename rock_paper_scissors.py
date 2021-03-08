#Rock, Paper, Scissors game
import random
import time

#Start game
#Asks for the users input.
def startGame():
    global usersChoice
    usersChoice = input('''Welcome to Rock, Paper, Scissors!
      \nPlease enter \'Rock\',\'Paper\' or \'Scissors\'.\n''').title()
#A random function
def r_p_c():
    global computerResult
    computerResult = random.choice(['Rock', 'Paper', 'Scissors'])

#Valid function
#User loses
def userLoses():
    if usersChoice == 'Rock' and computerResult == 'Paper':
        print("Sorry! Paper beats rock.")
        
    elif usersChoice == 'Paper' and computerResult == 'Scissors':
        print("Sorry! Scissors beats paper.")

    elif usersChoice == 'Scissors' and computerResult == 'Rock':
        print("Sorry! Rock beats Scissors.")

    elif usersChoice == computerResult:
        print("Its a tie!")
        

    else:
        print('You win! ' + usersChoice + ' beats ' + computerResult)
        global scoreKeeper
        scoreKeeper += 1


#Result function
def leaveGame():
    leave = input('Press \'q\' to quit the game or \'p\' to play again!\n')
    if leave == 'p':
        startGame()
        r_p_c()
        userLoses()
        print(computerResult)
        leaveGame()
    elif leave == 'q':
        print('Your final score is ' + str(scoreKeeper))
        time.sleep(5)
        quit()
        


#Scorekeeper
name = input('What\'s your name?\n')
letsGo = input('Hi ' + name.title() + ' press the spacebar and enter to play\n')
if letsGo == ' ':       #If space is pressed start the game.
    global scoreKeeper
    scoreKeeper = 0
    startGame()
    r_p_c()
    userLoses()
    print(computerResult)
    leaveGame()
    
else:
    print("Thank you come back soon!")



    
