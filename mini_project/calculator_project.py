
def add(a, b):

    """Addition method"""
    return a + b

def sub(a, b):
    """subtraction method"""
    return a - b

def mul(a, b):
    """multiplication method"""
    return a * b

def divide(a, b):
    """ Division method """
    if b == 0:
        return "Error: Cannot divide by Zero!"
    return a / b

while True:
    print("\nCalculator :")
    print("1. Addition ")
    print("2. Subtraction ")
    print("3. Multiplication ")
    print("4. Division is")

    choice = input("Enter your choice from the above option: ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result: ", add(num1, num2))
            break
        elif choice == '2':
            print("Result: ", sub(num1, num2))
            break
        elif choice == '3':
            print("Result: ", mul(num1, num2))
            break
        elif choice == '4':
            print("Result: ", divide(num1, num2))
            break
    
    else:
        print("Invalid input. Please choose a valid option.")

