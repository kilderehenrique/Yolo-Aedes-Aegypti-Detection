import os
import random
import shutil

image_folder = ["../datasets/BH-POOLS/images", "../datasets/BH-WATERTANKS/labels"]
labels_folder = ["../datasets/BH-POOLS/images", "../datasets/BH-WATERTANKS/labels"]

train = 0
test = 0
valid = 0

for id_grupo in range(2):
    image_list = [os.path.join(image_folder[id_grupo], img) for img in os.listdir(image_folder[id_grupo]) if img.endswith(('.jpg', '.png'))]

    qtd_img = len(image_list)

    for i in range(qtd_img):
        name = image_list[i].split("/")[-1]
        name = name[:name.rindex(".")]

        image_list[i] = name


    qtd_train = round(qtd_img * 0.8)
    qtd_test = round(qtd_img * 0.1)
    cont = 1

    for i in range(qtd_img):
        if cont <= qtd_train:
            path_destino = "train/"
            train += 1
        elif cont <= qtd_train+qtd_test:
            path_destino = "test/"
            test += 1
        else:
            path_destino = "valid/"
            valid += 1

            
        rd_index = random.randint(0, qtd_img-1)
        name = image_list[rd_index]

        qtd_img -= 1
        image_list.pop(rd_index)
        
        shutil.copy(image_folder+name+".jpg", path_destino+"images/"+name+".jpg")

        try:
            shutil.copy(labels_folder[id_grupo]+name+".txt", path_destino+"labels/"+name+".txt")
        except:
            pass

        cont += 1

    print("Para o grupo", id_grupo, train)
    print("Para o grupo", id_grupo, test)
    print("Para o grupo", id_grupo, valid)
pass