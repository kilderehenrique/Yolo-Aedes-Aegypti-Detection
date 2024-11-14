import os
import shutil

dir_images = '../datasets/BH-POOLS/recortes_images/'
dir_labels = '../datasets/BH-POOLS/recortes_labels/'

dir_images = '../datasets/BH-WATERTANKS/recortes_images/'
dir_labels = '../datasets/BH-WATERTANKS/recortes_labels/'

#dir_images = '../datasets/DL-Aedes-Dataset/caixas/images/'
#dir_labels = '../datasets/DL-Aedes-Dataset/caixas/labels/'
#
#dir_images = '../datasets/DL-Aedes-Dataset/pool/images/'
#dir_labels = '../datasets/DL-Aedes-Dataset/pool/labels/'

dir_images = '../treinamento/train/images/'
dir_labels = '../treinamento/train/labels/'

#dir_images = '../treinamento/valid/images/'
#dir_labels = '../treinamento/valid/labels/'

labels = os.listdir(dir_labels)
images = os.listdir(dir_images)

count = 0

new_dir_images = dir_images+"../background_imgs/"
os.makedirs(new_dir_images, exist_ok=True)

for file in images:
    path_img = dir_images+file
    new_path_img = new_dir_images+file
    
    img_name = os.path.splitext(file)[0]
    path_label = dir_labels+img_name+".txt"

    if not os.path.exists(path_label):
        count += 1
        shutil.copy(path_img, new_path_img)

print(count, "imagens sem objetos anotatos")