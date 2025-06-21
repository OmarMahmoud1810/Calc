def calculator():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == '1':
        result = a + b
    elif choice == '2':
        result = a - b
    elif choice == '3':
        result = a * b
    elif choice == '4':
        if b == 0:
            result = "Error: Division by zero"
        else:
            result = a / b
    else:
        result = "Invalid choice"

    print("Result:", result)

# Call the calculator function
calculator()
