# Ambiente

Instale o [Anaconda](https://www.anaconda.com/download) ou [Miniconda](https://docs.anaconda.com/miniconda/).<br>

Crie um ambiente virtual, pode seguir as instruções da [Ultralytics para Conda](https://docs.ultralytics.com/guides/conda-quickstart/).<br> <br>
<code>
conda create --name ultralytics-env<br>
conda activate ultralytics-env
</code>

Instale a biblioteca Ultralytics e suas dependencias.<br>
<code>
conda install -c conda-forge ultralytics
</code>
<br>

Caso possua GPU para usar na execução do treinamento instale as dependencias do CUDA.<br>
<code>
conda install -c conda-forge ultralytics pytorch torchvision pytorch-cuda=11.8 -c pytorch -c nvidia
</code>

# Treinamento

O treinamento pode ser feito com implementação [usando Python](https://docs.ultralytics.com/usage/python/) ou [usando o YOLO CLI](https://docs.ultralytics.com/usage/cli/).<br>
Aqui usaremos o CLI!<br><br>
Todos os argumento exceto o "mode" possuem um valor padrao.<br>
<code>
yolo [TASK] [MODE] [ARGS]<br>
yolo train data=data.yaml model=yolov8n.pt epochs=30
</code>

Parametro | Obrigatório | Valores
---|---|---
TASK | Não | detect, segment, classify, pose, obb
MODE | Sim | train, val, predict, export, track, benchmark
ARGS | Não | [Todos argumentos possiveis](https://docs.ultralytics.com/usage/cfg/)