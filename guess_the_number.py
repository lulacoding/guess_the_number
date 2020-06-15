#Guess the Number Game 
#Coded in Python with Visual Studio Code
#By Sam
#imports
import time 
import os
import random
import sys
from time import sleep

#Defines Colors
class color:

   PURPLE = '\033[1;35;48m'
   CYAN = '\033[1;36;48m'
   BOLD = '\033[1;37;48m'
   BLUE = '\033[1;34;48m'
   GREEN = '\033[1;32;48m'
   YELLOW = '\033[1;33;48m'
   RED = '\033[1;31;48m'
   BLACK = '\033[1;30;48m'
   UNDERLINE = '\033[4;37;48m'
   END = '\033[1;37;0m'

#sets the script to menu 0 at the start.
end = False
menu = 0
while not end:

    if menu == 0:
        os.system('cls' if os.name == 'nt' else 'clear')    
        #Main Menu Animation
        time.sleep(.5)
        print('')
        time.sleep(.2)
        print(color.PURPLE +'                             ░██████╗░██╗░░░██╗███████╗░██████╗░██████╗  ████████╗██╗░░██╗███████╗')
        time.sleep(.2)
        print(color.PURPLE +'                             ██╔════╝░██║░░░██║██╔════╝██╔════╝██╔════╝  ╚══██╔══╝██║░░██║██╔════╝')
        time.sleep(.2)
        print(color.PURPLE +'                             ██║░░██╗░██║░░░██║█████╗░░╚█████╗░╚█████╗░  ░░░██║░░░███████║█████╗░░')
        time.sleep(.2)
        print(color.PURPLE +'                             ██║░░╚██╗██║░░░██║██╔══╝░░░╚═══██╗░╚═══██╗  ░░░██║░░░██╔══██║██╔══╝░░')
        time.sleep(.2)
        print(color.PURPLE +'                             ╚██████╔╝╚██████╔╝███████╗██████╔╝██████╔╝  ░░░██║░░░██║░░██║███████╗')
        time.sleep(.2)
        print(color.PURPLE +'                             ░╚═════╝░░╚═════╝░╚══════╝╚═════╝░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝')
        time.sleep(.2)
        print('')
        time.sleep(.2)
        print(color.PURPLE +'                                      ███╗░░██╗██╗░░░██╗███╗░░░███╗██████╗░███████╗██████╗░')
        time.sleep(.2)
        print(color.PURPLE +'                                      ████╗░██║██║░░░██║████╗░████║██╔══██╗██╔════╝██╔══██╗')
        time.sleep(.2)
        print(color.PURPLE +'                                      ██╔██╗██║██║░░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝')
        time.sleep(.2)
        print(color.PURPLE +'                                      ██║╚████║██║░░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗')
        time.sleep(.2)
        print(color.PURPLE +'                                      ██║░╚███║╚██████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║')
        time.sleep(.2)
        print(color.PURPLE +'                                      ╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝')
        time.sleep(.2)
        print('                                               Main Menu / By Sam')
        print(color.END)
        sleep(.2)
        #Show the 2 different Gamemodes
        words = "       (1)   Play Guess The Number Original\n"
        for char in words:
            sleep(0.07)
            sys.stdout.write(char)
            sys.stdout.flush()
        print()
        words = "       (2)   Play Guess The Number With Cheats (5 Guesses)\n"
        for char in words:
            sleep(0.07)
            sys.stdout.write(char)
            sys.stdout.flush()
        print()
        #Menu System
        opt = input("              Select an option (1-2)              ")
        if opt == "1":
            menu = 1
            os.system('cls' if os.name  == 'nt' else 'clear')
        elif opt == "2":
            menu = 2

    #Menu 1 or Guess the number no Cheats/Original
    if menu == 1:
        print('')
        print(color.BLUE +'                             ░██████╗░██╗░░░██╗███████╗░██████╗░██████╗  ████████╗██╗░░██╗███████╗')
        print(color.BLUE +'                             ██╔════╝░██║░░░██║██╔════╝██╔════╝██╔════╝  ╚══██╔══╝██║░░██║██╔════╝')
        print(color.BLUE +'                             ██║░░██╗░██║░░░██║█████╗░░╚█████╗░╚█████╗░  ░░░██║░░░███████║█████╗░░')
        print(color.BLUE +'                             ██║░░╚██╗██║░░░██║██╔══╝░░░╚═══██╗░╚═══██╗  ░░░██║░░░██╔══██║██╔══╝░░')
        print(color.BLUE +'                             ╚██████╔╝╚██████╔╝███████╗██████╔╝██████╔╝  ░░░██║░░░██║░░██║███████╗')
        print(color.BLUE +'                             ░╚═════╝░░╚═════╝░╚══════╝╚═════╝░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝')
        print(color.BLUE)
        print(color.BLUE +'                                      ███╗░░██╗██╗░░░██╗███╗░░░███╗██████╗░███████╗██████╗░')
        print(color.BLUE +'                                      ████╗░██║██║░░░██║████╗░████║██╔══██╗██╔════╝██╔══██╗')
        print(color.BLUE +'                                      ██╔██╗██║██║░░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝')
        print(color.BLUE +'                                      ██║╚████║██║░░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗')
        print(color.BLUE +'                                      ██║░╚███║╚██████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║')
        print(color.BLUE +'                                      ╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝')
        print('                                               Original / By Sam ')
        print(color.END)
         
        hidden = random.randrange(1, 15)
        # print hidden
        time.sleep(.5)
        guess = int(input("         Please enter your guess: Between 1-15 "))
        #If the Number you guessed is right it will run theses Commands        
        if guess == hidden:
            time.sleep(.5)
            print("         You Guessed The Number!")
            time.sleep(.25)
            print('         (1) Play Again.')
            print('         (2) Exit')
            opt = input('           Please select a option between 1-2 ')
            if opt == '1':
                menu = 0
                os.system('cls' if os.name  == 'nt' else 'clear')
                
            if opt == '2':
                exit()
        #if you guess to low it will print these commands    
        elif guess < hidden:
            time.sleep(.5)
            print()
            print("         Your guess is too low, the number was", + hidden)
            time.sleep(.25)
            print()
            print('         (1) Play Again.')
            print('         (2) Exit')
            time.sleep(.5)
            print()
            opt = input('           Please select a option between 1-2 ')
            if opt == '1':
                os.system('cls' if os.name  == 'nt' else 'clear')
                menu = 0
            if opt == '2':
                exit()
        #if you guess to high it will print these commands
        elif guess > hidden:
            time.sleep(.5)
            print()
            print("         Your guess is too high, the number was", + hidden)
            time.sleep(.25)
            print()
            print('         (1) Play Again.')
            print('         (2) Exit')
            time.sleep(.5)
            print()
            opt = input('           Please select a option between 1-2 ')
            if opt == '1':
                os.system('cls' if os.name  == 'nt' else 'clear')
                menu = 0
            if opt == '2':
                exit()
            


    #Menu 2 or Guess the number with Cheats
    if menu == 2:
        os.system('cls' if os.name  == 'nt' else 'clear')
        print()
        print(color.RED +'                             ░██████╗░██╗░░░██╗███████╗░██████╗░██████╗  ████████╗██╗░░██╗███████╗')
        print(color.RED +'                             ██╔════╝░██║░░░██║██╔════╝██╔════╝██╔════╝  ╚══██╔══╝██║░░██║██╔════╝')
        print(color.RED +'                             ██║░░██╗░██║░░░██║█████╗░░╚█████╗░╚█████╗░  ░░░██║░░░███████║█████╗░░')
        print(color.RED +'                             ██║░░╚██╗██║░░░██║██╔══╝░░░╚═══██╗░╚═══██╗  ░░░██║░░░██╔══██║██╔══╝░░')
        print(color.RED +'                             ╚██████╔╝╚██████╔╝███████╗██████╔╝██████╔╝  ░░░██║░░░██║░░██║███████╗')
        print(color.RED +'                             ░╚═════╝░░╚═════╝░╚══════╝╚═════╝░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝')
        print()
        print(color.RED +'                                      ███╗░░██╗██╗░░░██╗███╗░░░███╗██████╗░███████╗██████╗░')
        print(color.RED +'                                      ████╗░██║██║░░░██║████╗░████║██╔══██╗██╔════╝██╔══██╗')
        print(color.RED +'                                      ██╔██╗██║██║░░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝')
        print(color.RED +'                                      ██║╚████║██║░░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗')
        print(color.RED +'                                      ██║░╚███║╚██████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║')
        print(color.RED +'                                      ╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝')
        print('                                               With Cheats / By Sam ')
        print(color.END)
        hidden = random.randrange(1, 15)
        guessestaken = 0
        tries = 5
        # print hidden
        time.sleep(.5)
        guess = int(input("         Please enter your guess: Between 1-15 "))
        guessestaken += 1


        while guess != hidden:
            #if your guess more then 5 times it will print theses commands
            if guessestaken > 5:
                print()
                time.sleep(.5)
                print('         You Are Out of Guesses.')
                time.sleep(.25)
                print()
                print('         (1) Play Again.')
                print('         (2) Exit')
                print()
                opt = input('           Please select a option between 1-2 ')
                if opt == '1':
                    menu = 0
                    os.system('cls' if os.name  == 'nt' else 'clear')
                if opt == '2':
                    exit()
                    time.sleep(.5)
            #if you guess to low it will print these commands
            if guess < hidden:
                time.sleep(.5)
                print("         Your guess is too low, Please Try Again")
                time.sleep(1)

            #if you guess to high it will print these commands
            if guess > hidden:
                time.sleep(.5)
                print("         Your guess is too high, Please try Again")
                time.sleep(1)
            os.system('cls' if os.name  == 'nt' else 'clear')
            print()
            print(color.RED +'                             ░██████╗░██╗░░░██╗███████╗░██████╗░██████╗  ████████╗██╗░░██╗███████╗')
            print(color.RED +'                             ██╔════╝░██║░░░██║██╔════╝██╔════╝██╔════╝  ╚══██╔══╝██║░░██║██╔════╝')
            print(color.RED +'                             ██║░░██╗░██║░░░██║█████╗░░╚█████╗░╚█████╗░  ░░░██║░░░███████║█████╗░░')
            print(color.RED +'                             ██║░░╚██╗██║░░░██║██╔══╝░░░╚═══██╗░╚═══██╗  ░░░██║░░░██╔══██║██╔══╝░░')
            print(color.RED +'                             ╚██████╔╝╚██████╔╝███████╗██████╔╝██████╔╝  ░░░██║░░░██║░░██║███████╗')
            print(color.RED +'                             ░╚═════╝░░╚═════╝░╚══════╝╚═════╝░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝')
            print()
            print(color.RED +'                                      ███╗░░██╗██╗░░░██╗███╗░░░███╗██████╗░███████╗██████╗░')
            print(color.RED +'                                      ████╗░██║██║░░░██║████╗░████║██╔══██╗██╔════╝██╔══██╗')
            print(color.RED +'                                      ██╔██╗██║██║░░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝')
            print(color.RED +'                                      ██║╚████║██║░░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗')
            print(color.RED +'                                      ██║░╚███║╚██████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║')
            print(color.RED +'                                      ╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝')
            print('                                               With Cheats / By Sam ')
            print(color.END)
            time.sleep(.5)
            print()
            guess = int(input('           Guess Again between 1-15 '))
            guessestaken += 1

           
        #If the Number you guessed is right it will run theses Commands        
        if guess == hidden:
            print("You Guessed The Number!")
            print()
            time.sleep(.25)
            print(' (1) Play Again.')
            print(' (2) Exit')
            print()
            opt = input('Please select a option between 1-2 ')
            if opt == '1':
                menu = 0
                os.system('cls' if os.name  == 'nt' else 'clear')
            if opt == '2':
                exit()