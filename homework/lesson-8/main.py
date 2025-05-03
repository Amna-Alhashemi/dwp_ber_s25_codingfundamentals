## 1. Create a dictionary with you personal info: name, age, occupation
## 2. Add your hobby to the dictionary
## 3. Print your occupation (two versions: calling the key and using get() )
## 4. Print your Nationality (two versions: calling the key and using get() with parameter )
## 5. Print your Nationality, if not found print “Unknown”
## 6. Print only the keys of the dictionary
## 7. Print only the values of the dictionary
## 8. Update your occupation
## 9. Remove your age from the dictionary
## 10. Check if the key "Favorite Color" is in the dictionary

personal_info={
    "name": "Amna",
    "age": 30,
    "occupation": "Reasearcher"}
personal_info["hobby"]= ["Dancing, Reading, Traveling"]
personal_info["nationality"]=["Bahraini"]


print(personal_info.get("occupation"))
print(personal_info.get("nationality"))


if "nationality" in personal_info:
    print(personal_info.get("nationality"))
else: 
    print("Unknown")

## 4. Print your Nationality (two versions: calling the key and using get() with parameter )
## 5. Print your Nationality, if not found print “Unknown”
#

## 6. Print only the keys of the dictionary
print(personal_info.keys())
## 7. Print only the values of the dictionary
print(personal_info.values())
## 8. Update your occupation
#personal_info["occupation"]="volunteer"
#personal_info.update({"occupation": "Writing" })
personal_info["hobby"].append("writing")
print(">>>>", personal_info)
## 9. Remove your age from the dictionary
personal_info.pop("age")
print(personal_info)
## 10. Check if the key "Favorite Color" is in the dictionary
if "Favorite Color" in personal_info:
    print(personal_info.get("favorite_color"))
else:
    print("Your favourite color is not available")




