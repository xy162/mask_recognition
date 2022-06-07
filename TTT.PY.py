# ------------      -------    --------    -----------    -----------
# @File       :TTT.PY.py    
# @Modify Time:2022/5/7 21:56
# @Author     :董海斌
# ------------      -------    --------    -----------    -----------
# import torch
# print(torch.cuda.is_available())

# import torch
# print(torch.cuda.is_available())
# print(torch.backends.cudnn.is_available())
# print(torch.cuda_version)
# print(torch.backends.cudnn.version())

import paddle
print(paddle.utils.run_check())

import numpy as np
import matplotlib.pyplot as plt

data = np.load('populations.npz', allow_pickle=True)
print(data.files)  # 查看文件中的数组
print(data['data'])
print(data['feature_names'])

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

name = data['feature_names']  # 提取其中的feature_names数组，视为数据的标签
values = data['data'][0:-2, :]  # 直方图数据 将年份逆序
for i in range(20):
    values[i, 0] = values[i, 0].replace("年", "")  # 去除年份中的汉字
print(values)

label1 = ['男性', '女性']  # 标签
label2 = ['城镇', '乡村']


def reverse_array(arr):
    n = len(arr)
    for i in range(int(n / 2)):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    return arr


reverse_array(values[:, 0])
reverse_array(values[:, 2])
reverse_array(values[:, 3])  # 调用逆序方法
reverse_array(values[:, 4])  # 调用逆序方法
reverse_array(values[:, 5])
print(values)

# 1.直方图
p1 = plt.figure(figsize=(12, 10))  # 设置画布大小
bar_width = 0.4  # 设置分组条形的宽度
# 子图1
a1 = p1.add_subplot(211)

plt.bar(np.arange(len(values[:, 0])), values[:, 2], width=bar_width,
        color='royalblue', label=label1[0], alpha=0.7)
plt.bar(np.arange(len(values[:, 0])) + bar_width, values[:, 3],
        color='pink', width=bar_width, label=label1[1], alpha=0.7)

plt.ylabel('人口（万人）')
plt.ylim(40000, 80000)  # 设置当前图形y轴的范围
plt.xlabel('时间（年）')

plt.xticks(np.arange(20) + bar_width / 2, values[:, 0], rotation=45)
# 添加图例
plt.legend()  # 添加标签
plt.title('1996~2015年男、女人口数直方图')

a11 = p1.add_subplot(212)

# 堆叠直方图
plt.bar(values[:, 0], values[:, 2], label=label1[0], width=bar_width, color='royalblue')
plt.bar(values[:, 0], values[:, 3], label=label1[1], bottom=values[:, 2],
        color='pink', alpha=1, width=bar_width)

plt.ylabel('人口（万人）')
plt.ylim(40000, 140000)  # 设置当前图形y轴的范围
plt.xlabel('时间（年）')

plt.xticks(np.arange(20) + bar_width / 2, values[:, 0], rotation=45)
# 添加图例
plt.title('1996~2015年男、女人口数直方图')
plt.legend()

plt.subplots_adjust(hspace=0.3, wspace=0)  # 控制子图距离


# 子图2
b1 = p1.add_subplot(231)

plt.bar(np.arange(len(values[:, 0])), values[:, 4], width=bar_width,
        color='orange', label=label2[0], alpha=0.7)
plt.bar(np.arange(len(values[:, 0])) + bar_width, values[:, 5],
        color='green', width=bar_width, label=label2[1], alpha=0.7)
plt.xlabel('时间（年）')
plt.ylabel('人口（万人）')
plt.ylim(10000, 100000)
plt.xticks(np.arange(20) + bar_width / 2, values[:, 0], rotation=45)
# 添加图例
plt.legend()
plt.title('1996~2015年城、乡人口数直方图')

# 2.饼图
ex = [0.01, 0.01]  # 饼图：设定各项距离圆心n个半径

p2 = plt.figure(figsize=(12, 12))
print(values)
# 子图1
a2 = p2.add_subplot(221)
plt.pie(values[0, 2:4], explode=ex, labels=label1,
        colors=['royalblue', 'pink'], autopct='%1.1f%%')
plt.title('1996年男、女人口数饼图')

# 子图2
b2 = p2.add_subplot(222)
plt.pie(values[19, 2:4], explode=ex, labels=label1,
        colors=['royalblue', 'pink'], autopct='%1.1f%%')
plt.title('2015年男、女人口数饼图')

# 子图3
c2 = p2.add_subplot(223)
plt.pie(values[0, 4:6], explode=ex, labels=label2,
        colors=['orange', 'green'], autopct='%1.1f%%')
plt.title('1996年城、乡人口数饼图')

# 子图4
d2 = p2.add_subplot(224)
plt.pie(values[19, 4:6], explode=ex, labels=label2,
        colors=['orange', 'green'], autopct='%1.1f%%')
plt.title('2015年城、乡人口数饼图')

# 显示
plt.show()

# 3.箱线图
p3 = plt.figure(figsize=(14, 14))
plt.boxplot(values[0:20, 1:6], notch=True,
            labels=['总人口', '男性', '女性', '城镇', '乡村'], meanline=True)
plt.xlabel('类别')
plt.ylabel('人口（万人）')
plt.title('1996~2015年各特征人口箱线图')
plt.show()

