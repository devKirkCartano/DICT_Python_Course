# raise keyword

n = 5  # if -5 leads to error

if n < 0:
    raise Exception("No negative numbers allowed")

# SyntaxError: invalid syntax

# Assertions, make sure the condition is true
employee_of_the_year = "John"
assert employee_of_the_year == "John"
# assert employee_of_the_year == "Jane" Leads to error

# Zero Division Error, 1/0

# TypeError, occurs when an operation is incorrect or unsupported object type
# Example: 50 ** 2

# Use try and except to handle errors

# finally, allows code no matter what the result of the try and except block

try:
    print(random_num)
except:
    print("Exception alert") # output this statement

try:
    print(x + "macaroons")
except NameError:
    print("Please define your variable")
except IndentationError:
    print("Please be careful when indenting your code")
except:
    print("Unknown error")

try: 
    print(24 + 31)
except:
    print("Wrong operation")
else:
    print("No issues here")

try:
    print(h)
except:
    print("There's something wrong in our program")
finally:
    print("This code will run anyway")