def circumference(radius):
    pi = 3.141592653589793
    return 2 * pi * radius



r = float(input("Enter the radius: "))
c = circumference(r)
print("Circumference:", c)