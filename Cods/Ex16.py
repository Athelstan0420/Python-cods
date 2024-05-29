# Quebrando um número


from math import trunc

try:
    valor = float(input("Digite um valor: "))  
except:
    print("Ops...")
else:
    print("O valor a ser pago será de R${}".format(trunc(valor)))
finally:
    print("Continue programando...")    