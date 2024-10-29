Instale o Conda
Crie um ambiente virtual com o Conda

Instale a lib Ultralytics e suas dependencias
<code>
conda install -c conda-forge ultralytics
conda install -c conda-forge ultralytics pytorch torchvision pytorch-cuda=11.8 -c pytorch -c nvidia
</code>


yolo train data=data.yaml model=yolov8n.pt epochs=10

'optimizer=auto' found, ignoring 'lr0=0.01' and 'momentum=0.937' and determining best 'optimizer', 'lr0' and 'momentum' automatically.