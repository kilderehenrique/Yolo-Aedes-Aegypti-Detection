import os
import cv2


datasets_path = "../datasets"

image_folder = [
    datasets_path + "/BH-WATERTANKS/annotations/",
    datasets_path + "/BH-POOLS/annotations/",
]
txt_dir = [
    datasets_path + "/BH-WATERTANKS/labels/",
    datasets_path + "/BH-POOLS/labels/",
]

for id_grupo in range(2):
    os.makedirs(txt_dir[id_grupo], exist_ok=True)

    image_list = [os.path.join(image_folder[id_grupo], img) for img in os.listdir(image_folder[id_grupo]) if img.endswith(('.jpg', '.png'))]

    for image_path in image_list:
        # Carrega a imagem
        imagem = cv2.imread(image_path)
        imagem_bb = cv2.imread(image_path)

        image_width = len(imagem[0])
        image_height = len(imagem)

        img_name = image_path.split("/")[-1]
        img_name = img_name[:img_name.rindex(".")]

        cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

        # Aplica um limiar para encontrar as áreas brancas
        _, mascara = cv2.threshold(cinza, 240, 255, cv2.THRESH_BINARY)

        # Encontra os contornos das áreas brancas
        contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        yolo_annotations = ""
        
        for contorno in contornos:
            x, y, width, height = cv2.boundingRect(contorno)

            cv2.rectangle(imagem_bb, (x, y), (x + width, y + height), (0, 255, 0), 2)  # Verde com espessura 2

            x_center = x + width/2
            y_center = y + height/2

            # normalizando
            x_center = float(x_center / image_width)
            y_center = float(y_center / image_height)
            width = float(width / image_width)
            height = float(height / image_height)

            yolo_annotations += (f"{id_grupo} {x_center} {y_center} {width} {height}\n")

        # Salvar o arquivo TXT
        txt_file = img_name + '.txt'
        with open(os.path.join(txt_dir[id_grupo], txt_file), 'w') as f:
            f.write(yolo_annotations)
