from traceback import print_tb

a = float(input("Digite o valor de a: "))
while (a == 0):
    a = float(input("O valor de a não pode ser zero. Digite novamente: "))
    b = float(input("Digite o valor de b: "))
    c= float(input("Digite o valor de c"))

    delta= b**2 - 4*a*c
    print("Delta", delta)
    if (delta < 0):
        print("Esta equação não possui raízes reais.")
    elif(delta == 0):
        x = -b/(2*a)
        print("x=", x)
    else:
        x1 = (-b +(delta)**(1/2))/(2*a)
        x2 = (-b - (delta) ** (1 / 2)) / (2 * a)

        print("x1=", x1, "x2=",x2)