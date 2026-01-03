def add(x, y):
    """Return the sum of x and y"""
    return x + y

def subtract(x, y):
    """Return the difference of x and y"""
    return x - y

def multiply(x, y):
    """Return the product of x and y"""
    return x * y

def divide(x, y):
    """Return the quotient of x and y"""
    if y == 0:
        return "Error: Division by zero is not allowed"
    return x / y

def calculator():
    """Main calculator function"""
    print("=" * 30)  
    print("Welcome to Simple Calculator")
    print("=" * 30)
    
    # Display operation menu
    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Get user choice
    while True:
        choice = input("\nEnter choice (1/2/3/4): ")
        
        if choice in ['1', '2', '3', '4']:
            break
        else:
            print("Invalid input! Please enter 1, 2, 3, or 4.")
    
    # Get numbers from user
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
    
    # Perform calculation based on choice
    if choice == '1':
        result = add(num1, num2)
        operation = "+"
    elif choice == '2':
        result = subtract(num1, num2)
        operation = "-"
    elif choice == '3':
        result = multiply(num1, num2)
        operation = "*"
    elif choice == '4':
        result = divide(num1, num2)
        operation = "/"
    
    # Display result
    print("\n" + "=" * 40)
    if isinstance(result, str):  # Error message
        print(result)
    else:
        print(f"{num1} {operation} {num2} = {result}")
    print("=" * 40)
    
    # Ask if user wants to continue
    again = input("\nDo you want to perform another calculation? (yes/no): ")
    if again.lower() == 'yes':
        print("\n")
        calculator()
    else:
        print("Thank you for using the calculator!")

# Run the calculator
if __name__ == "__main__":
    calculator()