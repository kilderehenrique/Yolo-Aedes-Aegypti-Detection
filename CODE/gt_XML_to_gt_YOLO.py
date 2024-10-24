import xml.etree.ElementTree as ET
import os

# 0 -> Caixa D'Agua
# 1 -> Piscina

classes_id = {
    "2": 0,
    "pool": 0,
    "watertank": 0
}

# Diretório onde estão os arquivos XML e onde os arquivos TXT serão salvos
xml_dir = 'labels_xml/'
txt_dir = 'labels/'

os.makedirs(txt_dir, exist_ok=True)  # Criar a pasta se não existir

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

# Percorre os arquivos XML
for xml_file in os.listdir(xml_dir):
    if xml_file.endswith('.xml'):
        annotations = xml_to_yolo(os.path.join(xml_dir, xml_file))

        # Salvar o arquivo TXT
        txt_file = os.path.splitext(xml_file)[0] + '.txt'
        with open(os.path.join(txt_dir, txt_file), 'w') as f:
            for annotation in annotations:
                f.write(annotation + '\n')


print(classes_id)