class Guest:
    def __init__(self,first,last,interest,phone):
        self.first = first
        self.last = last
        self.interest = interest
        self.phone = phone

g_1 = Guest("Eve", "Dela Cruz", "Anime", 12345)
g_2 = Guest("Adam", "Perez", "Russian Literature", 87654)
g_3 = Guest("Mike", "Lim", "Movies", 59821)
g_4 = Guest("Katie", "Lopez", "Sports", 81901)
g_5 = Guest("Berth", "Smith", "Cooking", 19027)

print(g_1.last)
print(g_2.phone)
print(g_3.phone)
print(g_4.interest)
print(g_5.last)
