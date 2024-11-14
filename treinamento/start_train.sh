modelo=yolov8s.pt
sz_img_compress=640

qtd_epocas=50
max_sem_melhoria=5

# considera apenas presença e nao classificacao
#single_cls=True

# usado para transfer learning
#freeze=NUM

yolo train model=$modelo data=data.yaml imgsz=$sz_img_compress epochs=$qtd_epocas patience=$max_sem_melhoria