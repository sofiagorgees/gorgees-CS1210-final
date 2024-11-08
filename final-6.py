"""
Final Project: Wordle Game
Sofia Gorgees - Katherine Walsh
CS 1210-B
"""
import random
from colorama import Fore, Back

#Constants
#Lists that contain the words based on number of characters
EASY = ["HELLO", "FLASK", "BRAKE", "PLANT", "HUMID", "SHIRT", "HORSE", "HUMAN",
        "WATER", "HATER", "VIDEO", "RODEO", "VOCAL", "PHONE", "CHEEK"]
HARD6 = ["CIRCUS","PEOPLE","RUNNER","FLIGHT","NUMBER", "BEFORE", "SALMON","RACING","STARED","SPREAD"]
HARD7 = ["MIRACLE", "REPLACE","OUTSIDE","GORILLA","TRAFFIC", "PERFECT", "COUNTRY","PICTURE","BATTERY","CAPABLE"]
HARD8 = ["SURROUND", "AIRPLANE", "ABSOLUTE", "MOUNTAIN", "SENTENCE", "PIZZERIA"]
#List for checking if a guess contains numbers
NUMBER=["1","2","3","4","5","6","7","8","9","0"]

###########-Round Function-#############################
def round(w, g, lst):
    w_list = []
    g_list = []
    for i in w:
        w_list.append(i)
    for i in g:
        g_list.append(i)   
    for i, e in enumerate(g_list):
        if e == w_list[i]:
            print(Back.GREEN + f'{e}', end = " ")
        elif (e in w_list):
            print(Back.YELLOW + f'{e}', end = " ")
        else:
            print(Back.RED + f'{e}', end = " ")
            if(e not in lst):
                lst.append(e)
    print(Back.RESET+'\n')
    if w_list == g_list:
        return True
    else:
        return False

##########-Easy Function-###########

def easy():
    word = random.choice(EASY)
    wrong = []
    for x in range(6):
        win = False
        while True:
            print(Fore.RESET)
            print(f'ROUND {x+1}\n-------------------------')
            #lets user know which letters have been used and are not in the word
            print(f'Letters not in word: {wrong}')
            guess = (input("Enter a 5 letter guess: ")).upper()
            #check each letter in the guess and if any letter has a number in
            #it then it prompts the user to enter a new guess
            correct = True
            while correct:
                for let in guess:
                    if let in NUMBER:
                        correct = False
                break      
            if (len(guess) == 5) and correct:
                #function returns true or false
                win = round(word, guess, wrong)
                break
            else:
                print("Must only be only 5 characters and use only letters")
        #if round is true meaning the user got the answer right during the round
        if win:
            print(Back.GREEN + Fore.BLACK +
                  "You got it correct!" + Fore.RESET + Back.RESET)
            break
        #if win is false then the for loop will run again
        #until the number of guesses runs out or the user wins
    if win == False:
        print("YOU LOSE! Better luck next time :(\n")
        print(f"Your word was {word}")

##############-Hard Function-##########################
    
def hard():
    choice = 0
    nums = [6, 7, 8]
    #asks user how many characters they want and validates
    #to make sure the choice is either 6, 7 or 8
    while choice not in nums:
        try:
            choice = int(input("How many characters would you like? (6, 7, 8): "))
        except ValueError:
            print('Please indicate your character preference (6, 7, 8)!')
    #choses a word with choice number of charcters from its respective list
    if choice == 6:
        word = random.choice(HARD6)
    elif choice == 7:
        word = random.choice(HARD7)
    elif choice ==  8:
        word = random.choice(HARD8)
    wrong = []
    #for loop runs for the number of characters in the word 
    for x in range(choice):
        win = False
        while True:
            print(Fore.RESET)
            print(f'ROUND {x+1}\n-------------------------')
            #lets user know which letters have been used and are not in the word
            print(f'Letters not in word: {wrong}')
            guess = (input(f"Enter a {choice} letter guess: ")).upper()
            #check each letter in the guess and if any letter has a number in
            #it then it prompts the user to enter a new guess
            correct = True
            while correct:
                for let in guess:
                    if let in NUMBER:
                        correct = False
                break      
            if (len(guess) == choice) and correct:
                win = round(word, guess , wrong)
                break
            else:
                print(f"Must only be only {choice} characters and use only letters")
        #if round is true meaning the user got the answer right during the round
        if win:
            print(Back.GREEN + Fore.BLACK + "You got it correct!" + Fore.RESET + Back.RESET)
            print(Fore.RESET)
            break
        #if win is false then the for loop will run again
        #until the number of guesses runs out or the user wins
    if win == False:
        print("YOU LOSE! Better luck next time :(\n")
        print(f"Your word was {word}")
    
        
#############################################

if __name__ == '__main__':
    print('----WORDLE----\n\nInstructions:\n\nWelcome to Wordle 2.0.\n -This game functions '
          'similiar to wordle.\nHowever, you will be prompted to choose between easy and hard mode'
          '.\n-Easy mode consists of all 5-character words and 6 attempts to guess the word,\n'
          '-Hard mode is between 6-8 characters in length and the number of attempts '
          '\nis based on the character count.\n'
          '\nGreen: Right letter, Right Location\n'
          'Red: Wrong Letter, Wrong Location\n'
          'Yellow: Right Letter, Wrong Placement\n\n')
    mode = ""
    playAgain = True
    again =""
    #loop to keep game running if the user chooses to play again
    while(playAgain):
        again = ""
        mode = ""
        #prompts user easy or hard mode until answer is correct
        while mode != 'EASY' and mode != 'HARD':
            mode = (input("Easy or Hard Mode? ")).upper()
        if mode == 'EASY':
            easy()
        else:
            hard()
        while(again != "Y" and again !="N"):    
            again = input("Would you like to play again? (y/n): ").upper()
        if(again == "N"):
            print("Thanks for playing!")
            playAgain = False
        
            
            
            
    
    
    
    







