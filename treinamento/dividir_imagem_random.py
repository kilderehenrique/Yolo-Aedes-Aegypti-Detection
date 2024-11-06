import os
import random
import shutil

datasets_path = "../datasets"

trainPer = 0.8
validPer = 0.2

datasets = {
    "BH-DATASET": [
        {
            "images": datasets_path+"/BH-POOLS/recortes_images/",
            "labels": datasets_path+"/BH-POOLS/recortes_labels/"
        },
        {
            "images": datasets_path+"/BH-WATERTANKS/recortes_images/",
            "labels": datasets_path+"/BH-WATERTANKS/recortes_labels/"
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


for image_name in datasets:
    for folder_path in datasets[image_name]:
        train = 0
        valid = 0
        test = 0
        
        image_list = os.listdir(folder_path["images"])

        qtd_img = len(image_list)
        qtd_train = round(qtd_img * trainPer)
        qtd_valid = round(qtd_img * validPer)
        cont = 1

        for i in range(qtd_img):
            if cont <= qtd_train:
                path_destino = "train/"
                train += 1
            elif cont <= qtd_train+qtd_valid:
                path_destino = "valid/"
                valid += 1
            else:
                path_destino = "test/"
                test += 1

                
            rd_index = random.randint(0, qtd_img-1)
            file_name = image_list[rd_index]
            image_name = os.path.splitext(file_name)[0]

            qtd_img -= 1
            image_list.pop(rd_index)
            
            shutil.copy(folder_path["images"]+file_name, path_destino+"images/"+file_name)

            try:
                shutil.copy(folder_path["labels"]+image_name+".txt", path_destino+"labels/"+image_name+".txt")
            except:
                pass

            cont += 1

        path = folder_path["images"]
        print(f"Para o grupo {path}, {train} imagens de treinamento.")
        print(f"Para o grupo {path}, {valid} imagens de validação.")
        print(f"Para o grupo {path}, {test} imagens de teste.")

pass