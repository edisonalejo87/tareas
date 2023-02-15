

from random import randint
opcion = ["piedra", "papel", "tijera"]

#Opcion de la maquina
computadora = opcion[randint(0,2)]

#Condición del bucle
usuario = True

#Condición del bucle
while usuario == True:
    #Opcion del usuario
    usuario = input("Piedra, Papel o Tijera? o salir :").lower()
    #Logica del juego
    if usuario == computadora:
        print("Empate")
    elif usuario == "piedra":
        if computadora == "papel":
            print("Perdiste! ", computadora, " > ", usuario)
        else:
            print("Ganaste !", usuario, " < ", computadora)
    elif usuario == "papel":
        if computadora == "tijera":
            print("Perdiste! ", computadora, " > ", usuario)
        else:
            print("Ganaste! ", usuario, " < ", computadora)
    elif usuario == "tijera":
        if computadora == "piedra":
            print("Perdiste! ", computadora, " > ", usuario)
        else:
            print("Ganaste! ", usuario, " < ", computadora)
    elif usuario == "salir":
            print("Muchas gracias por tu participación")
            break
    else:
        print("Error - Opción incorrecta, Intenta escribir las opciones como las vez.") 
    usuario = True
    computadora = opcion[randint(0,2)]