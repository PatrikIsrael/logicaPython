#exercício contador dias

contador_semana = 1 #conta qual dia da semana está

for dia in range(1, 32):
    if contador_semana == 1:
        print("Dia semana: ",dia, "- Domingo")

    elif contador_semana == 2:
        print("Dia semana: ",dia, "- Segunda-Feira")

    elif contador_semana == 3:
        print("Dia semana: ",dia, "- Terça-Feira")

    elif contador_semana == 4:
        print("Dia semana: ",dia, "- Quarta-Feira")

    elif contador_semana == 5:
        print("Dia semana: ",dia, "- Quinta-Feira")

    elif contador_semana == 6:
        print("Dia semana: ",dia, "- Sexta-Feira")

    elif contador_semana == 7:
        print("Dia semana: ",dia, "- Sábado")

#Contagem no contador
    if contador_semana == 7: #Quando o contador chegar no sábado, caso no 7 ele começara a contagem no dia 1 que é domingo.
        contador_semana = 1

    else: contador_semana += 1