dolares = input("¿Cantos dolares colombianos tienes?")
dolares = float(dolares)
valor_pesos = 3875
pesos =  valor_pesos * dolares
pesos = round(pesos, 2)
pesos = str(pesos)
print("Tienes $ " + pesos + " pesos")