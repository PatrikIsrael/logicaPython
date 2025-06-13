valor_compra = float(input("Digite o valor da compra R$: "))
valor_pago = float(input("Digite o valor a ser pago R$: "))
if(valor_pago >= valor_compra):
    troco = valor_pago - valor_compra
    print("Seu troco é: ", troco)
else:
    print("O valor pago é insuficiente para pagar a compra !!")

