import os

dir = '../datasets/BH-POOLS/labels/'
dir = '../datasets/BH-WATERTANKS/labels/'

arquivos = os.listdir(dir)

print(len(arquivos), "arquivos")

count = 0

for file in arquivos:
    path = dir+file

    with open(path, 'r') as arquivo:
        conteudo = arquivo.read()

    conteudo = conteudo.split("\n")

    for linha in conteudo:
        if linha == "":
            conteudo.remove("")

    count += len(conteudo)

print(count, "objetos anotatos")
