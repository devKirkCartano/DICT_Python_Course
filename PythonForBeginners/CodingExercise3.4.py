class Customers:
    greeting = "Welcome to the Coffee Palace!\n"

c_1 = Customers()

c_1.name = "Samirah"
c_1.beverages = "Iced coffee latte\n"
c_1.food = "Cinnamon roll"
c_1.total = 225

c_2 = Customers()

c_2.name = "Jerry"
c_2.beverages = "Caramel macchiato"
c_2.food = "Glazed doughnut"
c_2.total = 230

print(Customers.greeting)
print(c_1.name)
print(c_1.beverages)
print(c_2.name)
print(c_2.food)

