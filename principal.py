def cadastro_usuário(nome, idade, matricula, telefone):
    with open ("pessoas.txt", "a") as arquivo_cadastro:
        arquivo_cadastro.write("Nome: {} ; \nIdade: {} ; \nMatricula: {} ; Telefone: {}. \n\n".format(nome, idade, matricula, telefone))

def atualizar_dado(nome):
    with open ("pessoas.txt", "a") as arquivo_cadastro:
        if nome in arquivo_cadastro:
            return nome, idade, matricula, telefone
        
def escolher_jogo(jogo):
    with open ("relatorios/Jogos.txt", "r") as jogo:
        opções = jogo.read()
        escolher = int(input("Digite aqui o numero referente ao jogo na lista acima: "))
        
        








print("Seja bem-vindo(a) à sala de jogos")
print("Aqui voce pode escolher:")
print("1 - Cadastrar novo usuário;")
print("2 - Atualizar cadastro")
print("3 - Escolher jogo;")
print("4 - Empréstimo de jogo.")
escolha = int(input("Digite aqui sua escolha: "))


if escolha == 1:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    matricula = int(input("Digite sua matricula: "))
    telefone = int(input("Digite seu telefone: "))
    cadastro_usuário(nome, idade, matricula, telefone)
elif escolha == 2:
    digitarnome = input("Digite seu nome: ")
    dados = atualizar_dado(digitarnome)
    print(dados)
elif escolha == 3:
    print("hello word")