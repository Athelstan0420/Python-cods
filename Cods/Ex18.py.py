# Trigonometria: {

# Razões Trigonométricas:

# SENO, COSSENO E TANGENTE {
#
# Divisões realizadas entre as medidas de lados de um triângulo RETÂNGULO --> Polígono, com um ângulo reto,
# Hipotenusa = Lado que se opõe ao ângulo reto. MAIOR LADO;

# --> OPOSTO =  está em frente ao ângulo;
# --> ADJACENTE = Lado q n é a hipotenusa e forma o ângulo agudo de 90°;
# 
# --> Objetivo: Relacionar a media dos lados com a medida dos ângulos;
# EXEMPLO DE TRIÂNGULO RETANGULO;
# import webbrowser
# url = "https://s2.static.brasilescola.uol.com.br/img/2017/12/exemplo-de-triangulo-retangulo(1).jpg"
# img = webbrowser.open(url)
# ---------------------------------------------------------------------------------------------------
# Documentação math= https://docs.python.org/3/library/math.html

catopost = int(input("Cateto oposto a: "))
catadj =  int(input("Cateto adjacente b: "))
#Hipotenusa:
from math import sqrt
#Soma do quadrado de cada cateto
raiz1 = (catopost*catopost) + (catadj*catadj)
#Raiz da soma do quadrado de cada cateto
raiz2 = sqrt(raiz1) # <- hipotenusa
# -------------------------------------
#Seno, cosseno, tangente:
seno = (catopost / raiz2)#oposto dividido por hipotenuza;
print("seno: {}".format(seno))
cosseno = (catadj / raiz2)
print("cosseno: {}".format(cosseno))#adjacente div p/ hipotenusa;
print(raiz2)
tang = (catadj / catopost)
print("Tangente: {}".format(tang))

# A gente precisa obter pimeiro a hipotenuza e depois calcular o seno, consseno e tangente;



