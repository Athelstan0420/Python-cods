#Desafio dobro, triplo e raiz




import math

num_entrada = int(input("Digite um número: "))

dobro = num_entrada * 2

triplo = num_entrada * 3

print( "O dobro de {} é {}".format(num_entrada, dobro))
print("O triplo de {} é {}".format(num_entrada,triplo)) 
print("A raiz de {} é {:.2f}".format(num_entrada,
math.sqrt(num_entrada)))