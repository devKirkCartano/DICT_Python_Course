colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]

things = ["Cars", "Notebook", "Shirt", "Shoes"]

# For Loops
for x in colors:
    print(x)

for x in colors:
    if x == "Yellow":
        continue
    elif x == "Indigo":
        break
    print(x)

x = range(8) 

for y in x:
    print(y)

for x in colors:
    for y in things:
        print(x, y)

# While Loops

i = 1

while i <= 10:
    print(i)
    i += 1
    if i == 8:
        break

while i <= 7:
    print(i)
    i += 1
else:
    print("Done")