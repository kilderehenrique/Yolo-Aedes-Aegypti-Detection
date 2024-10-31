import os

dir = '../datasets/BH-WATERTANKS/recortes_labels/'
dir = '../datasets/BH-POOLS/recortes_labels/'

arquivos = os.listdir(dir)

print(len(arquivos), "arquivos")

classes = set([])

count = 0

for file in arquivos:
    path = dir+file

    with open(path, 'r') as arquivo:
        conteudo = arquivo.read()

    conteudo = conteudo.split("\n")

    for linha in conteudo:
        if linha == "":
            conteudo.remove("")

        linha = linha.split(" ")
        classes.add(linha[0])


    count += len(conteudo)


print(count, "objetos anotatos")
print(classes)