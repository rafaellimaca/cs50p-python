expression = input("Insert the expression: ")
x,z,y = expression.split(" ")
x = float (x)
z = float (z)
if y == "+":
    print(round((x + y),1))
elif y == "-":
    print(round((x - y),1))
elif y == "*":
    print(round((x * y),1))
elif y == "/":
    print(round((x / y),1))
