# Ambiente

[Instale o Anaconda ou Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) e crie um ambiente virtual.

Instale a biblioteca Ultralytics e suas dependencias.<br>
<code>
conda install -c conda-forge ultralytics
</code>

<br><br>

Caso possua GPU para usar na execução do treinamento instale as dependencias do CUDA.<br>
<code>
conda install -c conda-forge ultralytics pytorch torchvision pytorch-cuda=11.8 -c pytorch -c nvidia
</code>

# Treinamento

O treinamento pode ser feito com implementação [usando Python](https://docs.ultralytics.com/usage/python/) ou [usando o YOLO CLI](https://docs.ultralytics.com/usage/cli/). Aqui usaremos o CLI!<br>
<code>
yolo [TASK] [MODE] [ARGS]<br>
yolo train data=data.yaml model=yolov8n.pt epochs=30
</code>

Parametro | Obrigatório | Valores
---|---|---
TASK | Não | detect, segment, classify, pose, obb
MODE | Sim | train, val, predict, export, track, benchmark
ARGS | Não | [Todos argumentos possiveis](https://docs.ultralytics.com/usage/cfg/)


Todos os argumento exceto o "mode" possuem um valor padrao.