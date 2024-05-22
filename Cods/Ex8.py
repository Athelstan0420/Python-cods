#Conversor de medidaa 

medida = float(input("Medida em metros: "))

km = medida / 1000
hec = medida / 100
dec = medida / 10
dc = medida * 10
cm = medida * 100
mm = medida * 1000

print("Em Kilometros: {}km".format(km))
print("Em Hectometro: {}hec".format(hec))
print("Em Decametro:  {}dec".format(dec))
print("Em Decimetro: {}dc".format(dc))
print("Em Centimetro: {}cm".format(cm))
print("Em Milimetros: {}mm".format(mm))