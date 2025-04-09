def greet(name):
    print ("Hello, " + name + "!")
greet ("Amna")

def add(a,b): 
    return a+b 
print(add(4,4))

def is_even(n):
    if n %2 ==0: 
        return (True)
    else: 
        return (False)
print(is_even(5))

def find_max(x,y,z): 
    return max (x, y, z)
    
print(find_max (9,13,13))

def square (n):
    return n*n
print (square(4))

def factorial (n): 
    result =1 
    for i in range (1, n+1): 
        result *= i 
    return result 

print (factorial (4))

def count_vowels(s):
    for vowel in s:
        if vowel == "a" or vowel == "e" or vowel == "o" or vowel =="u" or vowel == "i": 
            return str(len(vowel))
            
        
print (count_vowels ("cneeioel"))