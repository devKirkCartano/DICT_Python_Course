# Basic dictionary
shopping_list = {"weird hat": 150, "purple_rug": 450,
                 "old_books": 200, "stuffed_elephant": 50}
print(shopping_list)

# List in dictionary
basketball_team = {"Crouching_tigers": [
    "Jacob", "Kevin", "Roni", "Joshua", "Isagani"]}
print(basketball_team)

empty_dictionary = {}
print(empty_dictionary)

# Add a new key-value pairs for 1 pair only
shopping_list["cellphone"] = 8700
print(shopping_list)

# Overwrite a key-value pairs
shopping_list["weird hat"] = 200
print(shopping_list)

# Update method to add more key-value pairs
shopping_list.update({"Cap": 200, "Cellphone case": 160})
print(shopping_list)

# zip function combines two or more list into a single list
relative = {"Aunt Mart", "Jeff", "Aunt John", "Veronica"}
age = [54, 14, 55, 19]

print(relative, age)

combined_list = zip(relative, age)
print(list(combined_list))

# dict function turns combined list into a dictionary
relative_age = dict(zip(relative, age))
print(relative_age)

# To get a single value of a key using function
print(shopping_list.get("weird hat"))
# To get a single value of a key using dictionary name and key
print(shopping_list["weird hat"])