# To check whether a triangle is right-angled or not

print("RIGHT ANGLED TRIANGLE")

def check(a, b, c):
    if a * a + b * b == c * c:
        print("It is a right-angled triangle")
    else:
        print("It is not a right-angled triangle")


a = int(input("Enter first side:"))
b = int(input("Enter second side:"))
c = int(input("Enter third side:"))

check(a, b, c)
