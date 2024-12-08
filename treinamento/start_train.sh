modelo=yolo11s.pt
#modelo=BH_robo.pt
#modelo=runs/detect/train/weights/best.pt

sz_img_compress=640

qtd_epocas=50
max_sem_melhoria=5

# considera apenas presença e nao classificacao
#single_cls=True

# usado para transfer learning
#freeze=NUM

yolo train model=$modelo data=data.yaml imgsz=$sz_img_compress epochs=$qtd_epocas 
#freeze=23
#classes=1
#patience=$max_sem_melhoria
#yolo train resume model=runs/detect/train2/weights/last.pt