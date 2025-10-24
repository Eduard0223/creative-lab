import time 


    
def historia_principal():

    historia =["Te despiertas de un extraño sueño que te deja aturdido", "Exploras el bosque y escuchas sonidos extraños","Exploras el lago", "Exploras la cueva y nuevamente escuchas ruidos extraños."]
    
    acciones = ["Abres los ojos y ves que tu alrededor es un bosque misterioso", "Encuentras un sendero lleno de flores brillantes"
                , "Sigues el camino del sendero de flores cristalinas, llegando a un lago aun más cristalino","Decides seguir explorando el bosque, encuentrandote con una cueva oscura","Observas tu reflejo en el agua, ¡y ves una figura misteriosa detras de ti!"]
    
    finales = ["Sientes miedo, pero enfrentas a la figura, pero es mas fuerte que tú. Despiertas.","Despiertas del sueño asustado por lo vivido","Decides correr sin parar y entras a una extraña cueva oscura, despiertas y no sabes que sucedio","Exploras la cueva oscura y algo te ataca, despiertas del sueño asustado"]
    
    #Comienzo de la historia
    print(historia[0])
    time.sleep(1.5)
    print(acciones[0])
    time.sleep(1.5)
    print(historia[1])
    time.sleep(1.5)
    print(acciones[1])
    time.sleep(1.5)
    camino_eleccion =  input("¿Quieres tomar este camino? [Si/No]: ")
    if camino_eleccion.lower() == "si":
        time.sleep(1.5)
        print(acciones[2])
        time.sleep(1.5)
        print(acciones[4])
        time.sleep(1.5)
        print(finales[0])
    elif camino_eleccion.lower() == "no":
        time.sleep(1.5)
        print(acciones[3])
        time.sleep(1.5)
        print(finales[3])
    


historia_principal()

