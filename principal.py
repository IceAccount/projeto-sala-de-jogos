def cadastro_usuário(nome, idade, cpf, telefone):
    with open ("pessoas.txt", "a") as arquivo_cadastro:
        arquivo_cadastro.write("Nome: {} ; \nIdade: {} ; \nCpf: {} ; Telefone: {}. \n\n".format(nome, idade, cpf, telefone))

def escolher_jogo():
    print("hello word")








print("Seja bem-vindo(a) à sala de jogos")
print("Aqui voce pode escolher:")
print("1 - Cadastrar novo usuário;")
print("2 - Atualizar cadastro")
print("3 - Escolher jogo;")
print("4 - Empréstimo de jogo.")
escolha = int(input("Digite aqui sua escolha: "))


if escolha == 1:
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cpf = int(input("Cpf: "))
    telefone = int(input("Telefone: "))
    cadastro_usuário(nome, idade, cpf, telefone)
elif escolha == 2:
    print("hello word")
elif escolha == 3:
    print("hello word")