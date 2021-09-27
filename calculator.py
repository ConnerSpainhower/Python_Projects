#Calculator
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

status = input("What do you want to do? Add, Subtract, Multiply, or Divide?")

if status in ("Add", "Subtract", "Multiply", "Divide"):
    first_num = int(input("First Number: "))
    second_num = int(input("Second number: "))

    if status == "Add":
        print (add(first_num, second_num))

    if status == "Subtract":
        print (sub(first_num, second_num))

    if status == "Multiply":
        print (mul(first_num, second_num))

    if status == "Divide":
        print (div(first_num, second_num))

else:
    print("Type Add, Subtract, Multiply or Divide")