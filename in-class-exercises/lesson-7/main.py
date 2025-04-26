print ("nested loop")
for column in range (1, 4): 
    print(f"row {column}: ", end = "")
    for row in range (1, 4): 
        print(column * row, end =" | ")
    print()

print ("nested loop")
for column in range (1, 6): 
    print(f"row {column}: ", end = "")
    for row in range (1, 6): 
        print(column * row, end =" | ")
    print()

print ("nested loop")
size = int(input ("choose the size of the table")) +1
for column in range (1, size): 
    print(f"row {column}: ", end = "")
    for row in range (1, size): 
        print(column * row, end =" | ")
    print()

name = "Amna"
print (f"nested loop for {name}")
size = int(input("Table size: ")) + 1
for column in range (1, size): 
    print (f"row {column}: ", end = "")
    for row in range (1, size): 
        print(column * row, end = " | ")
    print()

name = "Amna"
print (f"nested loop for {name}")
size = int(input("Table size: ")) + 1
for column in range (1, size): 
    print (f"row {column}: ", end = "")
    for row in range (1, size):
        if column * row <= 9:
            print(column * row, end="  | ")
        else:
            print(column * row, end=" | ")
    print()

