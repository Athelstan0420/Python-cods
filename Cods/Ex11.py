
#Pintando uma Parede:

while True:
    try:
        l = float(input("Largura da parede em m2: "))
        a = float(input("Altura da parede em m2:"))
        area = l * a        
        tinta = area / 4              
    except:
        print("Ops! Eu erro")
    else:
        print("A área dessa parede {} x {} é = {:.2f}m2".
        format(l,a,area))
        print("A quantidade de litros necessários será de {:.2f} litros".format(tinta))
    finally:
        print("Continue Programando..")

