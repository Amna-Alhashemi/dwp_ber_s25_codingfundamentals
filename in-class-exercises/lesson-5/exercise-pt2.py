'''
EXERCISE 4

Create a simple dice roll simulator where you use the randint function to simulate rolling a six-sided die. Follow these steps:
    1. Import the random module to use the randint function.
    2. Create a function that uses randint function to generate a random integer between 1 and 6, and returns the integer.	
    3. Store the function result in a variable
    4. Print out the variable
'''

# solution for exercise 4 👇🏽
<<<<<<< Updated upstream

from random import randint

def roll_dice():
    return randint(1,6)

roll_result = roll_dice()
print("The roll result is " + str(roll_result))
=======
from random import randint
def generate_a_random_integer (start_number, end_number):
    generated_integer = randint(start_number, end_number)
    return generated_integer

result= generate_a_random_integer(1, 6)
print ("Random number: "+ str(result))

>>>>>>> Stashed changes
