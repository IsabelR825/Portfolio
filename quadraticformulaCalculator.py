import math

a = float(input("Enter A: "))
b = float(input("Enter B: "))
c = float(input("Enter C: "))

def form(a, b, c):
    x = b**2 + (-4*a*c)
    if x >= 0:
        formula = math.sqrt(x)
        print("X = " + str(formula))
    else: 
        print("No Real Solution")
    

form(a, b, c)
