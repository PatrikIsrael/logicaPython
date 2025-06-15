peso = float(input("Digite o seu peso(kg): "))
altura = int(input("Digite sua altura em cm: "))

altura_metros = altura /100
imc = peso / (altura_metros ** 2)

print("Seu imc é ", imc)
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso normal")
elif 25 <= imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")