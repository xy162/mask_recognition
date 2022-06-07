# ------------      -------    --------    -----------    -----------
# @File       :preparedata.py    
# @Modify Time:2022/5/18 17:36
# @Author     :董海斌
# ------------      -------    --------    -----------    -----------
import os, random, shutil


def moveFile(fileDir, tarDir):
    pathDir = os.listdir(fileDir)  # 取图片的原始路径
    filenumber = len(pathDir)
    rate = 0.2  # 自定义抽取图片的比例，比方说100张抽10张，那就是0.1
    picknumber = int(filenumber * rate)  # 按照rate比例从文件夹中取一定数量图片
    sample = random.sample(pathDir, picknumber)  # 随机选取picknumber数量的样本图片
    print(sample)
    for name in sample:
        shutil.move(fileDir + name, tarDir + "\\" + name)
    return

if __name__ == '__main__':
    fileDir = r"./VOCdevkit/images/train" + "\\"  # 源图片文件夹路径
    tarDir = r'./VOCdevkit/images/val'  # 移动到新的文件夹路径
    #moveFile(fileDir, tarDir)
    """
    效果：
    实现取出labels/train文件夹中,与images/val文件夹图片中相同名字的txt文件，作为验证集的标签放到labels下val里
    """
    file_root = r'./VOCdevkit/images/val'  # 当前文件夹下的所有图片
    file_list = os.listdir(file_root)

    for i in file_list:
        if i.endswith('.jpg'):
            filename = r'./VOCdevkit/labels/train' + "\\" + i[:-4] + '.txt'
            # filename = os.path.join(r'E:\01_hjz\datas\facemask\mask10000_new\labels\train', i.strip() + '.txt')
            print(os.path.exists(filename))
            if os.path.exists(filename):
                shutil.copy(filename, r'./VOCdevkit/labels/val')
                # print(i + "处理成功！")

