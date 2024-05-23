

#Tratamento de erros e exceções


try: # Tente fazer isso: 
    valor = int(input("Digite um valor: "))

except: #Se houver erros, faça isso:
    print("Ops deu erro")

else: #Se não houver erro, faça isso:
    print(f"O valor digitado foi: {valor}")

finally: # Irá aparecer sempre!
    print("Continue Programando")
    
# No except você pode utilizar o:
# except Exception as erro:
#     print(f"O erro foi {erro.__class__}")

# Você pode utilizar quantos excetpt possíveis especificando cada tipo de erro e exceção