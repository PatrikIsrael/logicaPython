#funçao retorno

lado = float(input("Digite o lado do quadrado em metros: "))

def calcula_area():
    area = lado * lado
    return area

resulado = calcula_area()
print("A área do quadrado de lado ",lado, "m é: ", resulado,"m2")