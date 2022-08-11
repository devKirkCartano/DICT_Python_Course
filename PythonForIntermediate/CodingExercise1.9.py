flavors = ["vanilla", "chocolate", "strawberry",
           "cookies n' cream", "bubblegum"]
toppings = ["almonds", "banana slices", "chocolate syrup",
            "caramel syrup", "white chocolate chips"]

# combine list

ice_cream = dict(zip(flavors, toppings))
print(ice_cream)

ice_cream["chocolate"] = "blueberries"
print(ice_cream)

ice_cream.update({"matcha": "pistachios", "ube": "mango slices"})
print(ice_cream)
