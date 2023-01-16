#Scientific calculator using python
import math 

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# This function power two numbers
def power(x, y):
    a = pow(x, y)
    return a


# This function root number
def root(x):
    return(math.sqrt(x))  

# This function sin number
def sin(x):
    return (math.sin(x)) 

# This function cos number
def cos(x):
    return (math.cos(x))   

#Instructions for the calculator
print("-----> Iniciando calculadora...")
print("")
print("Presione (1) para sumar")
print("Presione (2) para restar")
print("Presione (3) para multiplicar")
print("Presione (4) para dividir")
print("Presione (5) para exponente")
print("Presione (6) para raiz")
print("Presione (7) para seno")
print("Presione (8) para coseno")
print("Presione (0) para apagar")
print("")

while True:
    # take input from the user
    choice = input("Selecciona la opción deseada (1/2/3/4/5/6/7/8/0): ")

    # check if choice is one of the nine options
    if choice in ('1', '2', '3', '4', '5'):
        try:
            num1 = float(input("Ingresa primer número: "))
            num2 = float(input("Ingresa segundo número: "))
        except ValueError:
            print("Ingresa una opción valida :) ")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "/", num2, "=", pow(num1, num2))
    
    elif choice in ('6', '7', '8'):
        try:
            num1 = float(input("Ingresa primer número: "))
        except ValueError:
            print("Ingresa una opción valida :) ")
            continue
        if choice == '6':
            print("La raíz de",num1, "es", root(num1))

        elif choice == '7':
            print("El seno de", num1, "es", sin(num1))

        elif choice == '8':
            print("El coseno de", num1, "es", cos(num1))
    elif choice in ('0'):
        if choice == '0':
            quit() 
    # check if user wants another calculation
    # break the while loop if answer is no        
    next_calculation = input("¿Deseas realizar otra operación? (si/no): ")
    if next_calculation == "no":
        break
    else:
        print("Opción incorrecta. Ingrese una opción valida nuevamente")