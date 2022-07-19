groceries = {"chicken" : 8, "apples" : 6, "cucumbers" : 3, "milk" : 2, "oranges" : 4}

remove = groceries.pop("oranges")
print(groceries)

speakers = {"Sir rafael" : 54, "Ms. Joan" : 33, "Ms.Dana" : 67}

names = speakers.keys()
print(names)

swimming_tryout = {"Carl": "passed", "Quentin" : "failed", "Peter" : "failed", "Jorge" : "failed"}

check_key = "Jorge"

print(swimming_tryout.get("Jorge"))