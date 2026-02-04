def cadastro_usuário(nome, matricula):
    with open ("pessoas.txt", "a") as arquivo_cadastro:
        arquivo_cadastro.write("\n\nNome: {} ; \nMatricula: {} ; \n\n-----//-----".format(nome, matricula))

        
def opçoes_jogo(genero):
    if genero == 1:
        with open ("Jogos.txt", "r") as jogo:
            todos_jogos = jogo.read()
            print(todos_jogos)
            print("\n0 - Caso queira voltar para o menu inicial, Digite 0: ")
            back = int(input(""))
    elif genero == 2:
        with open("Jogos-categoria.txt", "r") as jogos:
            categorias_jogos = jogos.read()
            print(categorias_jogos)
            print("\n0 - Caso queira voltar para o menu inicial, Digite 0: ")
            back = int(input(""))
    else:
        print("\n\n\nEsta opçao eh invalida\n")



while True:
    print("\n\nSeja bem-vindo(a) à sala de jogos! ")
    print("Aqui voce pode escolher entre: ")
    print("1 - Registrar entrada; ")
    print("2 - Ver opçoes de jogos; ")
    print("4 - Empréstimo de jogo; ")
    print("5 - Sobre nos. ")

    escolha = int(input("Digite sua escolha aqui: "))



    if escolha == 1:
        nome = input("Digite seu nome: ")
        matricula = int(input("Digite sua matricula: "))
        cadastro_usuário(nome, matricula)

        print("\n\n\n\nEntrada realizada com sucesso!")

    elif escolha == 2:
        print("Deseja ver: ")
        print("1 - Todas as opções de jogos; ")
        print("2 - Ver jogos por categorias. ")

        escolha = int(input("Digite sua escolha aqui: "))
        opçoes_jogo(escolha)

    elif escolha == 3:
        print("hello word")