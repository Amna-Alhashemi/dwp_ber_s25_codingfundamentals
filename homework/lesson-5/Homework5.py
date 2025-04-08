## HOMEWORK 1: Google time
# By using Google, find a function that gives you current date and time and print the current date and time

from datetime import datetime
print("The current time and date is:", datetime.now())

## HOMEWORK 2
# Do you still remember loops?
#1. Write a function that counts number of letters in a string you input.
#2. The function will have 1 parameter, the string that's letters you want to count.
#3. Try both variants - print the result (number of letters in the inputed string) and also store the result in the memory using return. Try to recall what is the difference between using print and return

# Without defining function:
word = str(input ())
count = 0 
for letter in word: 
    count += 1
print ("The number of letters is:", count)

# Alternative: 
def add_letters (word1=str(input())): 
    for letters in word1: 
        letters =  len (word1) 
        return letters   # stores the value 
  
print ("The number of letters is:", add_letters())  # print displays output, without return we would get the output None

## HOMEWORK 3: Using results of function in another function
# 1. Create a simple function with two parameters that returns their sum.
# 2. Call the function and save the result into a variable (name of the variable is up to you).
# 3. Create another function with one parameter that decides if the parameter can be divided by 3 and prints appropriate messages
# 4. Call the second function and use the variable that you created in the b) part as argument.

def add_numbers (a,b): 
    result = a + b 
    return result

sum= add_numbers (3 ,8)
print (sum)

def divided_by_3 (number): 
    if number %3 ==0 : 
        print ("Can be divided by 3.")
    else:
        print ("Cannot be divided by three.")

divided_by_3(sum)

## (Bonus) HOMEWORK 4: Rock, Paper, Scissors
#Here's what you need to do:
#1. Complete the game logic inside the play_game(user_choice) function. The function should determine the outcome of the game based
#on the user's choice (0 for rock, 1 for paper, and 2 for scissors) and the computer's randomly generated choice.
#2. The possible outcomes are as follows:
#   - If the user's choice is the same as the computer's choice, it's a "Tie."
#   - If the user wins, return "You win."
#   - If the computer wins, return "You lose."
#3. Test the game by calling the function with different user choices and print the results.
#Reminder: 
#- Rock beats Scissors
#- Scissors beats Paper
#- Paper beats Rock

import random 

def play_game(user_choice):
    computer_choice = random.randint (0, 2) # 0 rock, 1=paper, 2 scissors
    print ("You chose:", user_choice)
    print ("The computer chose:", computer_choice)

    if user_choice == computer_choice: 
        return "It's a tie :/"
    elif ((user_choice == 0 and computer_choice== 2) or (user_choice==1 and computer_choice==0) or (user_choice==2 and computer_choice==1)):
        return "You win! :)" 
    else: 
        return "You lose :("

print (play_game(2))

    
    




