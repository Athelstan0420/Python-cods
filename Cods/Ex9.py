
#Tabuada:

num = int(input("Digite um número inteiro para ver a tabuada:"))
print("-"*10)
for i in range(1, 11):
    print("{} x {} = {}".format(num, i, num * i))

print("-"*10)