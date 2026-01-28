import random

def novo_staff(nome, matricula, idade, cpf, telefone, funçao):
    with open ("relatorios/Staff.txt", "a") as arquivo_cadastro:
        arquivo_cadastro.write("Nome: {} ; \nMatricula: {} ; \nIdade: {} ; \nCpf: ; \nTelefone: {} ; \nFunçao: {} \nID: {}. \n\n".format(nome, matricula, idade, cpf, telefone, funçao))

print("1 - Cadastrar entrada")
print("2 - Cadastrar saída")
print("3 - Novo Staffer")
escolha = int(input("Digite sua escolha aqui: "))

if escolha == 1:
    arquivo_staff = open("Staff.txt", "a")
    id = input("id: ")
elif escolha == 2:
    arquivo_staff = open("Staff.txt", "a")
    id = input("id: ")
elif escolha == 3:
    print("Hello word")