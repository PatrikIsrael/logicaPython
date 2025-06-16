def le_numero():
    num = float(input("Digite o lado do quadrado: "))
    return num

def calcula_area_quadrado(lado):
    area = lado*lado
    return area

valor = le_numero()
resultado = calcula_area_quadrado(valor)
print("Área do quadrado é: ",resultado)