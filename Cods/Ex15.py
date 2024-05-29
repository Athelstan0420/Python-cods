
# Calculando aluguel de carro
try:
    km = float(input("Digite os km percorridos: "))
    dias = int(input("Dias alugados: "))
    vkm = km * 0.15
    vdias = dias * 60
    aluguel = vkm + vdias
except:
    print("Ops...")
else:
    print("O valor a ser pago será de R${:.2f}".format(aluguel))
finally:
    print("Continue programando...")    