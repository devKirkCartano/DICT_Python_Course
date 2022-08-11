employee_1 = {"Name": "Frank", "Position": "Sales Representative",
              "Email Address": "frank@company.com"}
# Looping through a dictionary
for key, value in employee_1.items():
    print(key)
    print(value)

for key in employee_1.keys():
    print(key)

for values in employee_1.values():
    print(values)

# Nested Dictionaries
cat = {1: {"Name": "Sweetie", "age": "12", "color": "white"},
       2: {"Name": "Mr. Whiskers", "age": "12", "color": "orange"}}
print(cat[2]["age"])
print(cat[1]["Name"])
print(cat[2]["color"])

cat[3] = {}
cat[3]["name"] = "Tuna"
cat[3]["age"] = "5"
cat[3]["color"] = "black"
cat[3]["personality"] = "friendly"


cat[4] = {"Name": "Bubbles", "age": "7",
          "color": "gray", "personality": "grumpy"}
print(cat[1])
print(cat[2])
print(cat[3])
print(cat[4])
