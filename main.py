import json
import os


caminho_entrada = "relatorio_entrada/pessoas.json"
caminho_jogos = "Jogos/jogos.json"
caminho_jogoscategoria = "Jogos/jogos-categoria.json"


def cadastrar_entrada(informaçoes):
    if os.path.exists(caminho_entrada):
        e = open(caminho_entrada, "r")
        try:
            info = json.load(e)
        except json.JSONDecodeError:
            info = []
    else:
        info = []
    info.append(informaçoes)
    with open(caminho_entrada, "w") as s:
        json.dump(info, s, indent=4)


def opçoes_jogos(categoria):
    if categoria == 1:
        j = open(caminho_jogos, "r")
        jogos = json.load(j)
        print(jogos)

    elif categoria == 2:
        c = open(caminho_jogoscategoria, "r")
        categorias = json.load(c)
        print(categorias)
    else:
        print("Escolha indisponível")
        escolha = int(input("Digite uma nova escolha aqui: "))