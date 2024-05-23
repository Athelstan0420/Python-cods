# Aumentos e Descontos:

while True:
    try:
        mod = " "
        valor = float(input("Digite o valor:     R$"))
        desc = float(input("Poentagem de desconto:     %"))
        print("="*30)
        opc = int(input("Aumento[1] -- Desconto[2]:     "))
        print("="*30)
        if opc == 1:
            conto = valor + (valor * desc / 100)
            mod = "Aumento"
        elif opc == 2:
            conto = valor - (valor * desc / 100)
            mod = "Desconto"
    except:
        print("Ops! Algo deu errado! tente novamente")
        
    else:
        print("O valor R${:.2f} com o {} de {:.0f}% fica R${}".format(valor, mod, desc, conto))         
    finally:
        print("="*30)
        print("Continue assim...")
        print("="*30)
