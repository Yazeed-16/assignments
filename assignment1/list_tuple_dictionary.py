# Different Operations on list, tuple and dictionary
#List Operations
print("LIST OPERATIONS")
a = [15, 46, 10, 70, 21]
print("Original list:", a)
a.append(60)
print("After append:", a)
a.insert(2, 65)
print("After insert:", a)
a.remove(65)
print("After remove:", a)
a.pop()
print("After pop:", a)
a.sort()
print("After sort:", a)

# Tuple Operations
print("TUPLE OPERATIONS")
x = (10, 20, 30, 20, 40)
print("Original tuple:", x)
print("Count of 20:", x.count(20))
print("Index of 30:", x.index(30))
print("First 3 elements:", x[:3])
y = x + (50, 60)
print("After adding tuple:", y)
z = (1, 2) * 3
print("After repeating tuple:", z)

# Dictionary Operations
print("DICTIONARY OPERATIONS")
d = {"name": "Yazeed","age": 19,"course": "CSE"}
print("Original dictionary:", d)
d["year"] = 1
print("After adding year:", d)
d.update({"age": 20})
print("After update:", d)
print("Name:", d.get("name"))
print("Keys:", d.keys())
print("Values:", d.values())
d.pop("year")
print("After pop:", d)
print("All operations completed.")
