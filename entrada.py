import main as es

while True:
    print("""

    █▄▄ █▀▀ █▀▄▀█   █░█ █ █▄░█ █▀▄ █▀█ ▄▀ ▄▀█ ▀▄   ▄▀█ █▀█   █░░ █▀▀ █░█ █▀▀ █░░ █
    █▄█ ██▄ █░▀░█   ▀▄▀ █ █░▀█ █▄▀ █▄█ ▀▄ █▀█ ▄▀   █▀█ █▄█   █▄▄ ██▄ ▀▄▀ ██▄ █▄▄ ▄
    """)

    print("Aqui voce pode escolher entre: ")
    print("1 - Registrar entrada; ")
    print("2 - Ver opçoes de jogos; ")
    print("3 - Horarios de funcionamento; ")
    print("4 - Sobre nos. ")

    escolha = int(input("Digite sua escolha aqui: "))



    if escolha == 1:
        nome = input("Digite seu nome: ")
        matricula = int(input("Digite sua matricula: "))
        data = input("Digite a data de hoje: ")

        dados = {
            'Nome': nome,
            'Matricula': matricula,
            'Data': data
        }
        es.cadastrar_entrada(dados)

        print("\n\n\n\nEntrada realizada com sucesso!\n")

    elif escolha == 2:
        print("Deseja ver: ")
        print("1 - Todas as opções de jogos; ")
        print("2 - Ver jogos por categorias. ")

        escolha = int(input("Digite sua escolha aqui: "))
        
        es.opçoes_jogos(escolha)

    elif escolha == 3:
        print("falta")

    elif escolha == 4:
        print("falta")
    
    else:
        print("Escolha indisponível")
        escolha = int(input("Digite sua escolha aqui: "))
