
numero_escritorios = int(input("Ingrese la cantidad de escritorios: "))
valor_escritorio = int(650000)
valor_compra = (numero_escritorios*valor_escritorio)

#print(numero_escritorios)
#print(valor_escritorio)
#print(valor_compra)

if numero_escritorios < 5:
    print("El valor a pagar es",valor_compra - (valor_compra * 0.1))
else:
    if numero_escritorios >= 5 and numero_escritorios < 10:
        print("El valor a pagar es",valor_compra - (valor_compra * 0.2))
    else:
        if numero_escritorios >= 10:
            print("El valor a pagar es",valor_compra - (valor_compra * 0.4))

