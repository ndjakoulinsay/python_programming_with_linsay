from email.policy import default


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")
def print_banner():
    print("\n")
    print("+-----------------------------------------+\n")
    print("|   LINSAY FANCY CALCULATOR                             |\n")
    print("+-----------------------------------------+\n")
    print("| 1.power(base^exp)                       |\n")
    print("| 2.square (n^2)                          |\n")
    print("| 3.cube(n^3)                             |\n")
    print("| 4.integer square root(√n)               |\n")
    print("| 5.factorial(n!)                         |\n")
    print("| 6.absolute value(|n|)                   |\n")
    print("| 7.logarithm(log(n))                     |\n")
    print("| 8.quadratic solver                      |\n")
    print("| 9.exit                                  |\n")
    print("+-----------------------------------------+\n")
    
    options = read_int("Please select an option (1-9): ")
    if options == 9:
        print("\n thanks for using linsay calculator,goodbye!")
        return
    elif options in [1, 2, 3, 4, 5, 6, 7, 8]:
        num1 = read_int("Enter the first number: ")
        num2 = read_int("Enter the second number: ")
    else:
        print("Invalid option. Please try again.")

    if options == 1:
        base = read_int("Enter the base: ")
        exp = read_int("Enter the exponent: ")
        if exp < 0:
            print("Exponent should be a non-negative integer.")
            return
        result = base ** exp
        print(f"{base}^{exp} = {result}")
    elif options == 2:
        n = read_int("Enter a number: ")
        result = n ** 2
        print(f"{n}^2 = {result}")
    elif options == 3:
        n = read_int("Enter a number: ")
        result = n ** 3
        print(f"{n}^3 = {result}")
    elif options == 4:
        n = read_int("Enter a number: ")
        if n < 0:
            print("Cannot compute square root of a negative number.")
            return
        answer = int(n ** 0.5)
        if answer == -1:
            print("is not a perfect square.")
            return
        result = int(n ** 0.5)
        print(f"Integer square root of {n} is {result}")
    elif options == 5:
        n = read_int("Enter a non-negative integer: ")
        if n < 0:
            print("Input should be a non-negative integer.")
            if n<0:
                print("factorial is not defined for negative integers.")
            return
        result = 1
        for i in range(1, n + 1):
            result *= i
        print(f"{n}! = {result}") 
        return  
    elif options == 6:
        n = read_int("Enter a number: ")
        result = abs(n)
        print(f"Absolute value of {n} is {result}")
        return
    elif options == 7:
        import math
        n = read_int("Enter a number: ")
        base = read_int("Enter a base: ")
        if result==-1:
            print("logarithm is not defined for non-positive numbers.")
            return
        result = math.log(n, base)
        print(f"log_{base}({n}) = {result}")
    elif options == 8:
        print("Solving quadratic equation ax^2 + bx + c = 0")
        a = read_int("Enter coefficient a(non-zero): ")
        if a == 0:
            print("Coefficient 'a' cannot be zero for a quadratic equation.")
            return
        b = read_int("Enter coefficient b: ")
        c = read_int("Enter coefficient c: ")
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            root1 = (-b + discriminant**0.5) / (2*a)
            root2 = (-b - discriminant**0.5) / (2*a)
            print(f"Two distinct real roots: {root1} and {root2}")
        elif discriminant == 0:
            root = -b / (2*a)
            print(f"One real root: {root}")
        if root==-1 and root2==-1:
            print("the equation has no real roots.")
            return
        else:
            print(f"the roots of the real roots are: {root1} and {root2}")
            return
    default()
    print("please select a valid option from 1-8.\n")
    return  

printResultline = "-----------------------------------------"
    
