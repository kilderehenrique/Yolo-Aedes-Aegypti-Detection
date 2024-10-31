from PIL import Image
import os

datasets_path = "../datasets"
pasta_recortes = "recortes_annotations"

img_paths = [
    datasets_path+"/BH-POOLS/annotations"
]

num_colunas = 6
num_linhas = 4


def recortar_imagem(path, file_name, num_colunas, num_linhas):
    image_path = path+"/"+file_name
    image_name = os.path.splitext(file_name)[0]

    # Abre a imagem
    imagem = Image.open(image_path)
    largura, altura = imagem.size

    # Calcula o tamanho de cada recorte
    largura_recorte = largura // num_colunas
    altura_recorte = altura // num_linhas

    # Cria uma pasta para os recortes, se não existir
    path_recortes = path+"/../"+pasta_recortes
    os.makedirs(path_recortes, exist_ok=True)

    cont = 1
    # Recorta e salva as imagens
    for i in range(num_colunas):
        for j in range(num_linhas):
            left = i * largura_recorte
            upper = j * altura_recorte
            right = left + largura_recorte
            lower = upper + altura_recorte

            # Faz o recorte
            recorte = imagem.crop((left, upper, right, lower))

            # Salva o recorte
            nome_recorte = f"{path_recortes}/{image_name}_{cont}.png"
            cont += 1
            recorte.save(nome_recorte)
            


for path in img_paths:
    cont = 1
    for file_name in os.listdir(path):
        recortar_imagem(path, file_name, num_colunas, num_linhas)
        print(file_name, cont)
        cont += 1


print(f"Recortes salvos na pasta '{pasta_recortes}'.")