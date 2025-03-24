# Lesson 3
# Operators, Conditions and Loops
## 1. Basic Arithmetic Operations
# Write a Python program that takes two numbers as input and prints the results of:

number1 = input("give a number")
number2 = input("give a number")
print (int(number1)+int(number2))
print (int(number1)-int(number2))
print (int(number1)*int(number2))
print (int(number1)/int(number2))

# Bonus! 
print (int(input ("Enter a number")) + int(input ("Enter another number")))

## 2. Modulus and Exponentiation
# Write a Python program that takes a number and prints:
#- The remainder when divided by 3 (using the modulus operator %)
#- The number raised to the power of 2 (using the exponentiation operator \*\*)

for x in range (1,10): 
     if x %3 ==1: 
         print (x)
         number4= x ** 2
         print (number4)

## 3. Odd or Even
# # Write a Python program that checks if a number is odd or even.
# Use the modulus operator and an if statement.
# Example of expected output:

for count in range (1, 10): 
     if count %2 == 0: 
          print ("The number is:", count)
          print ("The number is even.")
     else: 
         print ("The number is:", count)
         print ("The number is odd.")

## 4. Compare Two Numbers
#Write a Python program that takes two numbers and prints whether:
#- The first number is greater than the second
#- The second number is greater than the first
#- The two numbers are equal

number5= int(input("The first number is:")) 
number6= int(input("The second number is:"))
if number5 > number6: 
     print ("The first number is greater than the second.")
elif number6>number5: 
     print ("The second number is greater than the first.")
else: 
     print ("The two numbers are equal") 

## 5. Print Numbers 1 to 10
#Write a Python program that uses a for loop to print the numbers from 1 to 10.
count = [1,2,3,4,5,6,7,8,9,10]
for counting in count: 
    print (counting)
    counting += 1

## 6. Multiplication Table
# Write a Python program that takes a number and prints the multiplication table (from 1 to 10) for that number.
number7 = int(input("write a number"))
number_list = [1,2,3,4,5,6,7,8,9,10]
for number_count in number_list: 
    print (number7 * number_count)

## 7. FizzBuzz
# Write a Python program that prints the numbers from 1 to 20.
# But for multiples of 3, print "Fizz" instead of the number, and for multiples of 5, print "Buzz".
# For numbers which are multiples of both 3 and 5, print "FizzBuzz".

for number in range (1,21): 
    if number %3 == 0 and not number %5 == 0: 
        print ("Fizz")
    elif number %5 == 0 and not number %3 == 0: 
        print ("Buzz")
    elif number %3 == 0 and number %5 == 0: 
        print ("FizzBuzz")
    else: 
        print (number)

## 8. Leap year
#Write a Python program that asks the user to input a year and checks whether it is a leap year or not.
#A year is considered a leap year if it satisfies the following conditions:
#A year is a leap year if it is divisible by 4, except:
#If the year is divisible by 100, then it must also be divisible by 400 to be a leap year.
#In other words:
# A year that is divisible by 400 is always a leap year.
#A year that is divisible by 100 but not by 400 is not a leap year.
#A year that is divisible by 4 but not by 100 is a leap year.
#Any other year is not a leap year.
#Your program should output whether the input year is a leap year or not.

year = int(input ("insert a year"))
if year %4 == 0 and year %100 != 0: 
    print (year, "is a leap year")
elif year %400 == 0:
     print (year, "is a leap year")
elif year %100 == 0 and year %400 != 0: 
       print (year, "is not a leap year")
else: 
    print (year, "is not a leap year")
