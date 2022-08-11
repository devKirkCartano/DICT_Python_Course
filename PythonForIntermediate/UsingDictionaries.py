# Getting a key
exam_scores = {"Jonathan": 85, "Jane": 95, "John": 75, "Jenny": 85, "Jill": 95}
print(exam_scores["Jonathan"])

check_key = "John"

# To check if key exist
if check_key in exam_scores:
    print(check_key, "took the test")
else:
    print(check_key, "did not take the test")

print(exam_scores.get("Jane"))
print(exam_scores.get("Kirk"))
# .pop() method to remove a key-value pair


done = exam_scores.pop("Jill")
# To get keys without values
y = exam_scores.keys()
print(y)
# To get values without keys
value = exam_scores.values()
print(value)
# To get both keys and values
items = exam_scores.items()
print(items)
