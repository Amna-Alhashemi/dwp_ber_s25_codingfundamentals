# def make_smothie(first_fruit, second_fruit): 
#     print ("Here you go, smoothie of " + first_fruit + " and "+ second_fruit)

# make_smothie("Banana", "Strawberry")

# def make_smoothie_2(first_fruit, second_fruit, liquid = "water"):
#     print ("Here you go, smoothie of " + first_fruit + " and " + second_fruit + " and " + liquid )
# make_smoothie_2 ("Banana", "kiwi", "water")

from random import randint
def generate_a_random_number (start_number, end_number):
    generated_number = randint(start_number, end_number)
    return generated_number

random_number= generate_a_random_number(1, 100)
print ("Random number: "+ str(random_number))