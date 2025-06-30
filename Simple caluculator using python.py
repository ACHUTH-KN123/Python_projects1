while True:
    try:
        print("Simple Calculator")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        
        print("Choose an operation:")
        print("Press + for addition")
        print("Press - for subtraction")
        print("Press * for multiplication")
        print("Press / for division")
        
        o = input("Enter operation: ")

        match o:
            case "+":
                print(f"The result is {a + b}")
            case "-":
                print(f"The result is {a - b}")
            case "*":
                print(f"The result is {a * b}")
            case "/":
                if b != 0:
                    print(f"The result is {a / b}")
                else:
                    print("Cannot divide by zero!")
            case _:
                print("Invalid operation!")
                
    except Exception:
        print("Enter valid numeric values for a and b.")
