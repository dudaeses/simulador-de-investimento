while True:
    print("-------------------------------")
    print("  Seja bem-vindo(a) ao Mybank  ")
    print("   SIMULADOR DE INVESTIMENTO    ")
    print("-------------------------------")

    print("Títulos disponíveis para simulação:")

    print("1 - Tesouro Prefixado 2024")
    print("2 - Tesouro Prefixado 2026")

    cliente = input("Qual simulação gostaria de fazer? 1/2: ")

    if cliente == '1':
        valor_inicial = int(input("Qual valor você gostaria de investir agora?: "))
        valor_mensal = int(input("Qual valor você poderá investir mensalmente?: "))

        valor = (valor_mensal*32) + valor_inicial
        por_ir = (valor*15)/100
        valor_ir = valor - por_ir
        por_b3 = (valor*1.5)/100
        valor_lucro = valor*0.1081
        valor_bruto = valor + valor_lucro


        valor_liquido = valor - (valor_ir + por_b3)

        print("-------------------------------")
        print("   RESULTADO DA SIMULAÇÃO      ")
        print("-------------------------------")
        print("Valor inicial: ", valor_inicial)
        print("Aportes de", valor_mensal,"R$ por 32 meses")
        print("Valor total investido: ",valor)
        print("-------------------------------")
        print("Valor bruto: ", valor_bruto)
        print("I.R.: -", por_ir)
        print("B3: -",por_b3)
        print("-------------------------------")
        opcao = str(input("Deseja realizar outra simulação? s/n: "))

    else:
        valor_inicial = int(input("Qual valor você gostaria de investir agora?: "))
        valor_mensal = int(input("Qual valor você poderá investir mensalmente?: "))

        valor = (valor_mensal*50) + valor_inicial
        por_ir = (valor*15)/100
        valor_ir = valor - por_ir
        por_b3 = (valor*2.5)/100
        valor_lucro = valor*0.1081
        valor_bruto = valor + valor_lucro

        valor_liquido = valor - (valor_ir + por_b3)

        print("-------------------------------")
        print("   RESULTADO DA SIMULAÇÃO      ")
        print("-------------------------------")
        print("Valor inicial: ", valor_inicial)
        print("Aportes de", valor_mensal,"R$ por 50 meses")
        print("Valor total investido: ",valor)
        print("-------------------------------")
        print("Valor bruto: ", valor_bruto)
        print("I.R.: -", por_ir)
        print("B3: -",por_b3)
        print("-------------------------------")
        opcao = str(input("Deseja realizar outra simulação? s/n: "))

        if opcao == 'n':
          break

print("Programa encerrado")