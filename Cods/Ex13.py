while True:
    try:
        nome = str(input("Digite o nome do funcionário: "))
        valor = float(input("Digite o valor do pagamento: "))
        a = int(input("[1] [Aumento], [2] [Desconto]: "))
        if a == 1:
            pct = float(input("Digite o aumento em percentagem: %"))
            txt = "Aumento"
            aum = valor + (valor*pct/100)
            valor = aum
        elif a == 2:
            pct = float(input("Digite o desconto em porcentagem: %"))
            desc = valor - (valor*pct/100)
            txt= "Desconto"
            valor = desc
    except:
        print("Ops! Algo deu errado...")
    else:
        print("O valor teve um {} de {:.0f}% , e agora tem o montante de R${} reais ".format(txt, pct, valor))
