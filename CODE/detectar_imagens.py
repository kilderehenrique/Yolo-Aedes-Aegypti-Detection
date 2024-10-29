import os

import cv2
import pandas as pd
from ultralytics import YOLO


# Descomentar caso for usar modelo

#model = YOLO("best.pt")
#print(model.names)
#limiar_confianca = 0.5

# -------------------------

# Lista de imagens
image_folder = '../images/'
dir_labels = '../labels/'

output_folder = '../images_bb/'  # Pasta para salvar as imagens com bounding boxes
os.makedirs(output_folder, exist_ok=True)  # Criar a pasta se não existir

classes = {
    "0": "Caixa D'Agua", 
    "1": "Piscina"
}

# ------------------

def desenharBbManual(img, classe_id, image_width, image_height, x_center, y_center, w, h):
    # Como calcular centro e normalizar
    # x_center = (xmin + xmax) / 2 / image_width

    # desnormalizando
    x_center *= image_width
    y_center *= image_height
    w *= image_width
    h *= image_height

    x1 = int(x_center - w/2)
    y1 = int(y_center - h/2)
    x2 = int(x_center + w/2)
    y2 = int(y_center + h/2)

    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
    cv2.putText(img, f'Classe: {classes[classe_id]}', (x1, y1 - 10),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

def detectarDesenharBb(img):
    detections = model(img)

    for detection in detections:
        for obj in detection.boxes:
            class_id = int(obj.cls[0])  
            confidence = float(obj.conf[0])
            x1, y1, x2, y2 = map(int, obj.xyxy[0])

            if confidence > limiar_confianca:
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
                cv2.putText(img, f'Classe: {model.names[class_id]}\nConf: {confidence:.2f}', (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

def desenharBbDosLabels(img, img_path):
    img_name = img_path.split("/")[-1]
    img_name = os.path.splitext(img_name)[0]

    altura = len(img)
    largura = len(img[0])

    caminho_do_arquivo = dir_labels+img_name+".txt"

    try:
        with open(caminho_do_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
    except:
        return
    
    conteudo = conteudo.split("\n")

    for linha in conteudo:
        if linha.strip() == "":
            continue

        linha = linha.split(" ")

        if not linha[0] in classes:
            classes.append(linha[0])

        classe_id = linha[0]
        x_center = float(linha[1])
        y_center = float(linha[2])
        w = float(linha[3])
        h = float(linha[4])
    
        desenharBbManual(img, classe_id, largura, altura, x_center, y_center, w, h)

def detectInImages(withModel = False):
    image_list = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(('.jpg', '.png'))]

    for image_path in image_list:
        img = cv2.imread(image_path)
        
        if withModel:
            detectarDesenharBb(img)
        else:
            desenharBbDosLabels(img, image_path)

        # Salvar a imagem com bounding boxes
        output_path = os.path.join(output_folder, os.path.basename(image_path))
        cv2.imwrite(output_path, img)

def usarModeloComWebcam():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Erro ao capturar a imagem da webcam")
            break

        detectarDesenharBb(frame)

        cv2.imshow("Webcam YOLO", frame)

    cap.release()
    cv2.destroyAllWindows()


#usarModeloComWebcam()
#detectInImages(withModel=True)
detectInImages(withModel=False)
