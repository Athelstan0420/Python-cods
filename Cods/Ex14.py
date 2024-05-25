while True:
    try:
        a = int(input("Em que você quer expressar a temperatura; [1] C° ou [2] F° :"))
        if a == 1:
            temp = float(input("Digite a temperatura: "))
            txt = "A temperatura é de {:.2f} C°".format(temp)
        elif a == 2:
            temp = float(input("Digite a temperatura: "))
            f = (temp * 1.8) + 32
            txt = "A temperatura é de {:.2f} F°".format(f)
        else:
            print("="*30)
            print("ERROR devido a tentativa de inserir digito inválido!")   
            print("="*30)   
    except:
        print("Ops...")
    
    else:
        print(txt)
        
    finally:
        print("Continue Programando...")