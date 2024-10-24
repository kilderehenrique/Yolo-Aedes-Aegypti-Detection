import os

dir = 'labels/'

arquivos = os.listdir(dir)

print(len(arquivos), "arquivos")

count = 0

for file in arquivos:
    path = dir+file

    with open(path, 'r') as arquivo:
        conteudo = arquivo.read()

    conteudo = conteudo.split("\n")

    count += len(conteudo)

print(count, "objetos anotatos")
