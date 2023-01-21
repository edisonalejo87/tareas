#useropcion = input("Ingrese puedra papel o tijera ")
computer = "piedra"
useropcion= "tijera"
# if useropcion == computer:
#     print("empate")
# elif useropcion == "tijera":
#     if computer == "Piedra":
#         print("computer gana")
#     else:
#         print("Usuario gana")
computer = "tijera"
useropcion= "papel"
if computer == "piedra" and computer =="papel":
    print("Gano,papel a piedra ")
elif computer == "papel" and useropcion == "tijera":
    print("Gano,tijera a papel ")
elif computer == "tijera" and useropcion == "piedra":
    print("Gano,piedra a tijera ")
if computer =="papel" and useropcion =="piedra":
    print("perdiste,La computadora gana papel a piedra ")
elif computer == "tijera" and useropcion == "papel":
    print("perdiste,la computadora gana tijera a papel ")
elif computer == "piedra" and useropcion == "tijera":
    print("perdiste,computadora gana piedra a tijera")
elif computer == useropcion:
    print("empate nadie gana ")
