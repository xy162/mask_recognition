yolov5口罩识别

一.训练部分

1.

将口罩数据集中图片放入

VOCdevkit\images\train

标注数据放入

VOCdevkit\labels\train

2.

运行preparedata.py对训练集和验证集进行划分

3.

运行train.py开始训练

4,

准备推理样本，修改detect.py中推理样本和模型位置，实现口罩识别。