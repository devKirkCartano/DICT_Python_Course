help("modules")
variable_1 = 0
x = 500

# if x > 100:
# raise Exception("x is greater than 100")

try:
    print(variable_1)
except:
    print("Variable is not defined")
    for i in range(6):
        print("I'am happy")

try:
    print(12 * 6)
except:
    print("Something went wrong")
else:
    print("Operation can't be performed")

best_burger = "Burger King"
number_2_burger = "Burger Shop"

assert best_burger == "Burger King"
assert best_burger == "Burger Shop"
