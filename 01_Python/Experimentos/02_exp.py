#Pedir al usuario dos numeros y mostrar mayor, menor o si son iguales

def comparacion_simple():
    print(" *** Bienvenido a una comparación simple ***")
    num1 = input("Ingresa un número: ") 
    num2 = input("Ingresa otro número: ") 

    if num1 > num2:
        print(f"{num1} Es mayor que {num2}")
    elif num1 < num2:
        print(f"{num2} Es mayor que {num1}")
    else:
        print("Los numeros son iguales")

comparacion_simple()
        
    