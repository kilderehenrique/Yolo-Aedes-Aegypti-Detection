import os
import random
import shutil

datasets_path = "../datasets"

datasets = {
    "BH-DATASET": [
        {
            "images": datasets_path+"/BH-POOLS/images/",
            "labels": datasets_path+"/BH-POOLS/labels/"
        },
        {
            "images": datasets_path+"/BH-WATERTANKS/images/",
            "labels": datasets_path+"/BH-WATERTANKS/labels/"
        }
    ],
    "DL-Aedes-Dataset": [
        {
            "images": datasets_path+"/DL-Aedes-Dataset/pool/images/",
            "labels": datasets_path+"/DL-Aedes-Dataset/pool/labels/"
        },
        {
            "images": datasets_path+"/DL-Aedes-Dataset/caixas/images/",
            "labels": datasets_path+"/DL-Aedes-Dataset/caixas/labels/"
        }
    ]
}

# ------------------------------
# Altere o dataset aqui
#use_dataset = "DL-Aedes-Dataset"
#use_dataset = "BH-DATASET"

# ------------------------------


for name in datasets:
    for folder_path in datasets[name]:
        train = 0
        test = 0
        valid = 0
        
        image_list = os.listdir(folder_path["images"])

        qtd_img = len(image_list)

        for i in range(qtd_img):
            name = image_list[i].split("/")[-1]
            name = os.path.splitext(name)[0]

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
            
            shutil.copy(folder_path["images"]+name+".jpg", path_destino+"images/"+name+".jpg")

            try:
                shutil.copy(folder_path["labels"]+name+".txt", path_destino+"labels/"+name+".txt")
            except:
                pass

            cont += 1

        path = folder_path["images"]
        print(f"Para o grupo {path}, {train} imagens de treinamento.")
        print(f"Para o grupo {path}, {test} imagens de teste.")
        print(f"Para o grupo {path}, {valid} imagens de validação.")

pass