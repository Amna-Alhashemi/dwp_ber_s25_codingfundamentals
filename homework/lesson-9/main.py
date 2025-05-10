# 1. Why does the line below give an error? What can you do to fix it?
age = 26
first_name = "Ada"
print("I am " + first_name + " and I am " + str(age) + " years old")

# 2. What will be the value of x at the end of these calculations?
#    (first try to figure it out without printing it!)
a = 5
b = 10
x = a + b  #x= 15
a = 2 + b  # a = 12
b = (a + 2) * b # b = 14*10 = 140 
x = b  # x=140
print(x)

# 3. What are the problems with this conditional? How can you fix it?
weather = input("What is the weather like?")
if weather == "rainy":
  print("Let's go to the museum!")
elif weather == "snowy":
  print("Let's go skiing!")
elif weather == "sunny":
  print("Let's go to the beach!")
else:  
  print("Let's stay home!")

# 4. We want to print all even numbers from 1 to 100.
# but this loop doesn't print even numbers correctly for some reason.
# Can you find why and fix it?
for n in range(1, 101):
    if n % 2 == 0:
        print(n)
      


# 5. This code below does not execute properly. Try to figure out why.
def multiply(a, b):
  c= a * b
  return c

result = multiply(10, 10)
print(result)

### EXERCISES:


# The code below picks a random number between 1-100,
# and assigns it to the variable called "number". 
# Write code that prints out:
# - "wow it's exactly zero!" if the number is 0
# - "it's a small number" if the number is less than 10
# - "getting bigger" if the number is less than 50
# - "it's a big number" in any other case
import random
number = random.randint(1, 100)
print(number)

if number == 0: 
   print("wow it's exactly zero!")
elif number < 10: 
   print ("it's a small number")
elif number > 10 and number < 50: 
   print ("getting bigger")
else: 
   print("it's a big number")

# For each fruit in the fruits list, display "It's a {fruit}" on the screen.
fruits = ["banana", "apple", "cherry", "pear"]
for fruit in fruits: 
   if len(fruit)<= 5:
     print ("It's a", fruit)
#    print (f"It's a {fruit}")

# Slightly change your code to only print if the fruit length is smaller or equal to 5 characters


# You are given the following string:
magic_word = "abracadabra"

# Loop over each character in the string and print all the 'a's they are in the magic word:
#magic_word_list= ["a", "b", "r", "a", "c", "a", "d", "a", "b", "r", "a"]
for letter in magic_word:
   if letter == "a":
      print(letter)
      
#print(magic_word_list.append(letter))


# You are given the following string:
magic_word = "abracadabra"
# Print the indices of all the 'a's in the magic word:
# Example: "aba" -> 0 and 2 (first and third letter)
magic_word_list= list(magic_word)
# for i in enumerate(magic_word_list): 
#    print (i)
#    print(i [0])
#    print (i [1])

for i, letter in enumerate(magic_word_list):
   if letter == "a":
        print (f"Index {i}: {letter}")

for i, letter in enumerate(magic_word_list, start =1):
   if letter == "a":
        print (f"{i}: {letter}")

# Finds the largest number in the list
numbers = [3,8,1,7,2,9,5,4]

print(max(numbers)) 



# Compute the sum of all elements in the following list:
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(sum(lst))

# Write code that merges the two dictionaries below into one
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Hint: "Google is your best friend"
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}


# For the output dictionary, look over the key and values and print the key/value pairs:

