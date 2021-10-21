
print("-------------------------------")
print("  Seja bem-vindo(a) ao Mybank  ")
print("   SIMULADOR DE INVESTIMENTO    ")
print("-------------------------------")

print("Títulos disponíveis para simulação:")

print("1 - Tesouro Prefixado 2024")
print("2 - Tesouro Prefixado 2027")

cliente = int(input("Qual simulação gostaria de fazer? 1/2: "))

if cliente == '1':
    valor_inicial = int(input("Qual valor você gostaria de investir agora?: "))
    valor_mensal = int(input("Qual valor você poderá investir mensalmente?: "))

    valor_bruto = (valor_mensal*34) + valor_inicial

    por_ir = (valor_bruto*15)/100
    valor_ir = valor_bruto - por_ir
    por_b3 = (valor_bruto*0.75)/100

    valor_liquido = valor_ir - por_b3

    print("-------------------------------")
    print("   RESULTADO DA SIMULAÇÃO      ")
    print("-------------------------------")
    print("Valor inicial: ", valor_inicial)
    print("Aportes de", valor_mensal,"R$ por 34 meses")
    print("Valor total investido: ",valor_liquido)
    print("-------------------------------")
    print("Valor bruto: ", valor_bruto)
    print("I.R.: ", por_ir)
    print("B3: ",por_b3)
    print("-------------------------------")
    opcao = str(input("Deseja realizar outra simulação? s/n: "))

    if opcao == 'n':
        print("Programa encerrado")


else:
    valor_inicial = int(input("Qual valor você gostaria de investir agora?: "))
    valor_mensal = int(input("Qual valor você poderá investir mensalmente?: "))

    valor_bruto = (valor_mensal*64) + valor_inicial

    por_ir = (valor_bruto*15)/100
    valor_ir = valor_bruto - por_ir
    por_b3 = (valor_bruto*1)/100

    valor_liquido = valor_ir - por_b3


    print("-------------------------------")
    print("   RESULTADO DA SIMULAÇÃO      ")
    print("-------------------------------")
    print("Valor inicial: ", valor_inicial)
    print("Aportes de", valor_mensal,"R$ por 64 meses")
    print("Valor total investido: ",valor_liquido)
    print("-------------------------------")
    print("Valor bruto: ", valor_bruto)
    print("I.R.: ", por_ir)
    print("B3: ",por_b3)
    print("-------------------------------")
    opcao = str(input("Deseja realizar outra simulação? s/n: "))

    if opcao == 'n':
        print("Programa encerrado")