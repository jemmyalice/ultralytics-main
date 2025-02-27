import warnings

from mpmath import fraction

from ultralytics import YOLO
warnings.filterwarnings('ignore')

if __name__=='__main__':
    model = YOLO(r'F:\pytroch\ultralytics-main\ultralytics\cfg\models\11\yolo11.yaml')

    model.train(data=r"F:\pytroch\ultralytics-main\data\data.yaml",
        cache=False,
        imgsz=640,
        epochs=1,
        single_cls=False,  # 是否是单类别检测
        batch=8,
        close_mosaic=0,
        workers=0,
        fraction = 0.1,
        device='cpu',
        optimizer='SGD',  # using SGD 优化器 默认为auto建议大家使用固定的.
        amp=True,  # 如果出现训练损失为Nan可以关闭amp
        project='runs/train',
        name='exp',
    )
