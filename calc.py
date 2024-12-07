first = float(input("Enter the first number => "))
sceond = float(input("Enter the second number => "))
opr = str(input("Enter an Operator (+ , - , * , /) => "))

if opr == "+":
    total = first + sceond
elif opr == "-":
    total = first - sceond
elif opr == "*":
    total = first * sceond
elif opr == "/":
    total = first / sceond
else:
    total = str("Please Enter a Valid operator")

print(total)
    