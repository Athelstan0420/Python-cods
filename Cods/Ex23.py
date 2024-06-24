try:
    cidade = str(input("Em que cidade você nasceu? ")).upper()
    if "SANTO" in cidade:
        aux = True
    else:
        aux = False
except:
    print("Ops..")
else:
    print(aux)