# a raiz da soma dos catetos
# elevando-os ao quadrado;

from math import sqrt
try: 
    cateto1 = int(input("Cateto 1: "))
    cateto2 = int(input("Cateto 2 : "))
    raiz1 = cateto1*cateto1 + cateto2*cateto2
    raiz2 = sqrt(raiz1)    
except:
    print("Ops")    
else:
    print(raiz2)
    
    