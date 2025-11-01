import time

def guardian_del_templo():
    print("*** Luego de caminar por horas encuentras un templo ***")
    time.sleep(1.5)
    #verificaciones
    decision = input("¿Deseas entrar al templo?: ").lower().strip()
    if decision == "si":
        print("Te adentras dentro del templo oscuro.. ")
        time.sleep(1)
        print("Entre la luz vez una figura aterradora.. ¿Es un guardian?")
        time.sleep(1.5)
        print("Bienvenido humano. Soy el guardian de este Templo.. ¿Que te trae por aqui?")
        time.sleep(1.5)
        print("¡¿QUE HACES ACA HUMANO?! ¡DIME!")
        time.sleep(1)
        print("¡¡¿COMO LLEGASTE ACA HUMANO?!! ¡¡¡DIME!!!")
        respuesta = input("¿Que respondes?: ")
        time.sleep(1.5)
        print("El guardian te observa atentamente.")
        time.sleep(1.5)
        print(f"Entonces tu respuesta es: '{respuesta}' Entiendo.. Responde estas preguntas y dare una respuesta.")
        # *** Preguntas ***
        nombre = input("¿Cual es tu nombre humano?: ")
        time.sleep(1.5)
        #* Edad jugador *
        print(f"Entonces.. {nombre} ¿Cual es tu edad? ")
        edad = int(input("¿Que respondes?: "))
       # respuesta a sabiduria
        print(f"Entonces humano llamado.. {nombre} y de edad humana de {edad}.. Respondeme esta pregunta..")
        time.sleep(2)
        print("Cuentame que es lo que anhela tu corazon ¿Sabiduria o Poder?")
        time.sleep(2)
        pregunta1 = input("¿Qué respondes?: ")
        #Validacion edad y continuidad del minijuego
        if edad >= 18 and pregunta1.lower().strip() == "sabiduria":
            time.sleep(1.5)
            print(f"¡Bienvenido al templo {nombre} tendras la {pregunta1} que buscas!.")

        elif edad >= 18 and pregunta1.lower().strip() == "poder":
            time.sleep(1.5)
            print("El guardian te observa atentamente")
            time.sleep(1.5)
            print(f"Tu corazón es puro lo veo.. puedo concederte el paso al templo, Bienvenido {nombre}.")

        elif edad <= 18 and pregunta1.lower().strip() == "sabiduria":
            time.sleep(1.5)
            print("El guardian observa atentamente y tarda en su respuesta..")
            time.sleep(2)
            print(f"Aún eres joven {nombre} pero buscas sabiduria, te condecere el paso por solo ser tu.")

        elif edad <= 18 and pregunta1.lower().strip() == "poder": 
            time.sleep(1.5)
            print(f"Aún eres muy joven pequeño {nombre}, el verdadero poder llegara al tiempo correcto, paciencia.")
        #camino opcional final diferente.
        elif edad != 18 and pregunta1.lower().strip() == "felicidad":
            print("El guardian te observa atentamente..")
            time.sleep(2)
            print(f"{nombre} La felicidad se encuentra en pequeñas cosas, y se que aún el camino es confuso, pero lo lograras, Bienvenido al templo {nombre} te ayudare.")

        else:
            time.sleep(2)
            print("El guardian desaparece entre las sombras..")

    else:
        print("Decides no entrar al templo y sales huyendo.")
        time.sleep(1.5)
        print("¡¡ENTRA AL TEMPLO PARA ESO HICE EL CODIGO!! ")
    

guardian_del_templo()