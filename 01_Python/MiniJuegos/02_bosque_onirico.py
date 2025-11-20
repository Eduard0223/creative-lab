#mod
import time 

#menu
def bosque_onirico():
    # contadores
    exploraciones = 0
    descansos = 0
    guardian_intentos = 0
    while True:
        time.sleep(1.5)
        print(" *** Acciones *** ")
        print("[1] Explorar")
        print("[2] Descansar")
        print("[3] Buscar al Guardián")
        print("[4] Despertar")
     # OPCIÓN EXPLORAR    
        options =  input ("¿Que vas hacer viajero?: ").strip().lower()
        if options == "1" or options == "explorar": 
            exploraciones += 1
            time.sleep(1)
            if exploraciones == 1:
                print("Decides explorar el bosque.. no encuentras nada")
            elif exploraciones == 2:
                print("Empiezas a sentir que algo te observa..")
            elif exploraciones == 3:
                print("Algo se mueve entre los árboles..")
            else:
                print("El bosque te susurra y parece estar vivo, es consciente de que estas aqui.")

     # OPCIÓN DESCANSAR   
        elif options == "2" or options == "descansar":
            descansos += 1
            if descansos == 1:
                print("Te recuperas y sigues tu camino..")
                time.sleep(1.5)
                print("Recuperas energia.. (+10)")
            elif descansos == 2:
                time.sleep(1.5)
                print("Vuelves a descansar.. Pero igual te sientes cansado ¿Qué sucede?")
                time.sleep(1.5)
                print("Recuperas energia.. (+10)")
            elif descansos == 3:
                time.sleep(1.5)
                print("El bosque esta diferente ¿Se esta distorsionando?")
                time.sleep(1.5)
                print("Recuperas energia.. (+10)")
            elif descansos >= 4:
                time.sleep(1.5)
                print(" ¿Realmente estoy en la realidad o es un sueño? Todo esta distorsionado..")
                time.sleep(1.5)
                print("Empiezas a sentirte inquieto..")
                time.sleep(1.5)
                print("Recuperas energia.. (+10)")
            else:
                print("Esto es un sueño, deberia despertar.. No es la realidad")
            # OPCIÓN BUSCAR AL GUARDIAN
        elif options == "3" or options == "buscar al guardian":
            guardian_intentos += 1
            time.sleep(1)
            if guardian_intentos == 1:
                time.sleep(1)
                print("Ves una cueva a lo lejos y decides entrar.. No hay nada, solo oscuridad.")
            elif guardian_intentos == 2:
                time.sleep(1)
                print("Te adentras más y crees ver una figura a lo lejos.. ¿Qué es?")
            elif guardian_intentos == 3:
                time.sleep(1)
                print("La figura esta cada vez mas cerca, tiene una forma inquietante.. Sientes miedo")
            else:
                time.sleep(1)
                print("Frente a ti ves un humanoide con forma extraña, viste armadura, esta armado con una espada y es gigante..")
                time.sleep(1)
                print("Se presenta como el Guardian del Bosque y te pregunta que haces..")
                time.sleep(1)
                print("Decides correr con todas tus fuerzas y escapas.") 
        # OPCIÓN 4 SALIR DEL PROGRAMA O DESPERTAR
        elif options == "4" or options == "despertar":
            
            time.sleep(1)
            print("Decides despertar del sueño.. ¿Realmente era un sueño?.")
            time.sleep(1)
            print("Sigues tu vida normal.")
            break

bosque_onirico()