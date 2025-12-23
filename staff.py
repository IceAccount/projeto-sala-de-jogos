import random


print("1 - Cadastrar entrada")
print("2 - Cadastrar saída")
print("3 - Novo funcionário")
escolha = int(input("Digite sua escolha aqui: "))

if escolha == 1:
    arquivo_staff = open("Staff.txt", "a")
    id = input("id: ")
elif escolha == 2:
    arquivo_staff = open("Staff.txt", "a")
    id = input("id: ")
elif escolha == 3:
    print("Hello word")