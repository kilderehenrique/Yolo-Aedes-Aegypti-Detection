import xml.etree.ElementTree as ET
import os

# 0 -> Caixa D'Agua
# 1 -> Piscina

classes_id = {
    "watertank": 0,
    "pool": 1
}

datasets_path = "../datasets"

dirs = [
    {
        "annotations": datasets_path + "/DL-Aedes-Dataset/pool/annotations/",
        "labels": datasets_path + "/DL-Aedes-Dataset/pool/labels/"
    },
    {
        "annotations": datasets_path + "/DL-Aedes-Dataset/caixas/annotations/",
        "labels": datasets_path + "/DL-Aedes-Dataset/caixas/labels/"
    }
]

def xml_to_yolo(xml_file, image_width=None, image_height=None):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    yolo_annotations = []

    image_width = float(root.find('size/width').text)
    image_height = float(root.find('size/height').text)

    for obj in root.findall('object'):
        class_name = obj.find('name').text  # Obtenha o nome da classe
        class_id = classes_id[class_name]  # Obtenha o id da classe

        xmin = float(obj.find('bndbox/xmin').text)
        ymin = float(obj.find('bndbox/ymin').text)
        xmax = float(obj.find('bndbox/xmax').text)
        ymax = float(obj.find('bndbox/ymax').text)

        # Cálculo das coordenadas normalizadas
        width = xmax - xmin
        height = ymax - ymin
        x_center = xmin + width/2
        y_center = ymin + height/2

        # Normalizando
        x_center = x_center / image_width
        y_center = y_center / image_height
        width = width / image_width
        height = height / image_height

        # Formatação da linha para YOLO
        yolo_annotations.append(f"{class_id} {x_center} {y_center} {width} {height}")

    return yolo_annotations

for dir in dirs:
    # Criar a pasta se não existir
    os.makedirs(dir["labels"], exist_ok=True)  

    # Percorre os arquivos XML
    for xml_file in os.listdir(dir["annotations"]):
        if xml_file.endswith('.xml'):
            annotations = xml_to_yolo(os.path.join(dir["annotations"], xml_file))

            # Salvar o arquivo TXT
            txt_file = os.path.splitext(xml_file)[0] + '.txt'
            with open(os.path.join(dir["labels"], txt_file), 'w') as f:
                for annotation in annotations:
                    f.write(annotation + '\n')
