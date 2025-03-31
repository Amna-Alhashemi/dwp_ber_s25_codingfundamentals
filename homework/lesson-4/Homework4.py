# Exercises on Data Structures (Lists, Sets, Tuples)             

## Exercise 0
## Given the following scores, what is the length of the list?

scores = [5, 6, 6, 13, 6, 16, 2, 4, 6, 15, 3, 7, 20, 3, 24, 24, 1, 23, 3, 3, 3, 21, 7, 2, 12]
print(len(scores))

## Exercise 1:
##Given the same list of scores, write a program that counts the number of 3s in the list
 
count_of_threes = scores.count(3)

print("Number of 3s in the list:", count_of_threes)

## Exercise 2:
# Given the same list of scores, find the maximum in the list
print(max(scores))

## Exercise 3:
# Given the following two lists, write a program that prints the common elements

list_1 = ["foo", 2, "bar", 3, "baz", "spam", 4]
list_2 = ["1", 2, "3", 3, "4", "foo", "pasm", "bar"]

common_elements = set(list_1) & set(list_2)

print("Common elements:", common_elements)

## Exercise 4:
# Given the following list of numbers, write a program
# 1. that goes through each number in the list
# 2. appends it to a new list called `positive_numbers` if the number is positive

all_numbers = [111, 32, -9, -45, -17, 9, 85, -10]

positive_numbers= []
for number in all_numbers: 
    if number > 0: 
        positive_numbers.append(number)

print("Positive numbers are:", positive_numbers)
    

## Exercise 5:
# Print the items of the given list in reverse

reverse_this_list = [10, 20, 30, 40, 50]
reverse_this_list.reverse()
print(reverse_this_list)

## Exercise 6
#Convert the scores list (from Exercise 0) into a set and print its elements
set_scores = set (scores)
print (set_scores)

## Exercise 7
# Create a List of Tuples with 5 country names and their capitals, and print the list
# Each tuple should contain one country and its capital

countries_and_capitals = [("USA", "Washington D.C."),("France", "Paris"),("Japan", "Tokyo"),("Lebanon", "Beirut"),("Germany", "Berlin")]
print(countries_and_capitals)
