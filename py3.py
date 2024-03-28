
def thing():
    num1 = int(input("Input first number"))
    num2 = int(input("Input second number"))

    while True:
        print(num1)
        num1 = num1 + 1
        if num1 == num2:
            print(num2)
            break

thing()
