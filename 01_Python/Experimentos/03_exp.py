# Pedir al usuario edad y país, si tiene 18 o mas y es de chile mostrar "Puedes votar", de no tener 18 aun no, y si no es de chile, 
# no vota

def verificacion_voto():
    edad = int(input("Ingresa tu edad: "))
    pais = input("Ingresa tu país: ")
    # validaciones
    pais = pais.strip().lower()
    # verificaciones
    if edad >= 18 and pais == "chile":
        print("Apto para voto: Cumple edad y País")
    elif edad >= 18 and pais != "chile":
        print("No apto para voto: Eres mayor, pero no Chileno")
    elif edad <= 17 and pais == "chile":
        print("No apto para voto: Menor de edad.")
    else:
        print("No cumple ninguno de los requisitos")

verificacion_voto()


    #elif edad <= 17 and pais != "Chile":
     #   print("No apto para voto: No cumple ambos requisitos")