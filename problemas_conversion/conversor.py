menu = """"
Bienvenido al conversor de monedas

1 - Pesos colombianos
2 - Pesos Mexicanos
3 - Pesos argentinos

Elija una opción: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("¿Cantos pesos colombianos tienes?")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
elif opcion == 2:
    pesos = input("¿Cantos pesos mexicanos tienes?")
    pesos = float(pesos)
    valor_dolar = 19.86
    dolares = pesos / valor_dolar
elif opcion == 3:
    pesos = input("¿Cantos pesos argentinos tienes?")
    pesos = float(pesos)
    valor_dolar = 111.21
    dolares = pesos / valor_dolar
else:
    print("Ingresa una opcion correcta por favor: ")

dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $ " + dolares + " dólares")

