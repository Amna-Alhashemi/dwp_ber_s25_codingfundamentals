# # Homework L7: Shopping List
# ## WHAT YOU'RE BUILDING
# Create a program that:

# 1. Asks users to enter items for their shopping list
# 2. Keeps asking for items until they type 'done'
# 3. Shows the complete list at the end



# ### Input handling:
# 1. Ignore empty inputs (just ask again)
# 2. Remove extra spaces before and after items
# 3. Don't add 'done' to the shopping list

# ## TESTING YOUR PROGRAM
# Test your program with these scenarios:

# 1. Normal items: milk, bread, eggs
# 2. Items with spaces: " milk  " (extra spaces)
# 3. Empty inputs: (just press Enter)
# 4. Different cases of 'done': DONE, Done, done
# 5. Single item then done
# 6. Directly typing 'done' (empty list)

shopping_list = []
while True:
    item= input ("Enter an item ('done' to finish): ").strip()
    if item.lower() == "done":
        break
    elif item == "":
        continue
    else:
        shopping_list.append(item)
print (shopping_list)

print("Your shopping list: ")
count = 1
for item in shopping_list:
    print(f"{count}. {item}")
    count +=1

total_items= len (shopping_list)
print ("Total items:", total_items)

## BONUS CHALLENGES (OPTIONAL)
#After completing the basic requirements, try these:

# 1. Don't allow duplicate items
# 2. Sort the list alphabetically before displaying

shopping_set = set()
while True:
    item= input ("Enter an item ('done' to finish): ").strip()
    if item.lower() == "done":
        break
    elif item == "":
        continue
    shopping_set.add(item.lower())

shopping_list2= sorted (shopping_set)
print(shopping_list2)

print("Your shopping list: ")
count = 1
for item in shopping_list2:
    print(f"{count}. {item}")
    count +=1

total_items= len (shopping_list2)
print ("Total items:", total_items)