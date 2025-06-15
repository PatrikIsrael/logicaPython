lista = [ (5, 7), (11, 13), (17, 19) ]
lista_aux = []
for x in lista:
    for y in x:
        lista_aux.append(y)
        print(lista_aux)