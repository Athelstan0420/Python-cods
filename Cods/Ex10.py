#Conversor de moedas 

real = float(input("Valor em reais: "))
dolar = float(input("Digite a cotação atual do dolar: "))

convert = real / dolar
print("R${:.2f} reais == ${:.2f} dolares".format(real, convert))