from sklearn import datasets,model_selection
import os
import numpy as np
import matplotlib.pyplot as plt
import urllib.request
from PIL import Image
import wget


data_dir = os.path.join(os.path.dirname(__file__),"mldata")
os.makedirs(data_dir,exist_ok=True)
data_path = os.path.join(data_dir,"mnist-original.mat")
if not os.path.isfile(data_path):
    url = 'https://github.com/amplab/datascience-sp14/raw/master/lab7/mldata/mnist-original.mat'
    filename = wget.download(url, out=data_dir)
mnist = datasets.fetch_mldata('MNIST original', data_home=os.getcwd())
DATA_SIZE = len(mnist.data)
train_size = 60000
test_size = DATA_SIZE - train_size

x_train, x_test, y_train, y_test = model_selection.train_test_split(mnist.data, mnist.target,train_size=train_size, test_size=test_size)

# print(x_train.shape)
# print(x_test.shape)
# print(y_train.dtype)
# print(y_test.shape)

# PILを使って一枚の画像にMNIST手書き画像をまとめて表示


# def ConvertToImg(img):
#     return Image.fromarray(np.uint8(img))


width = 28
height = 28
num = 10


# pillow
# MNISTの文字をPILで１枚の画像に描画する
# IMG = Image.new('RGB', (int(width * num), int(height * num)), (255, 255, 255))

# MNISTの文字を読み込んで描画
# i = 0
# for y in range(int(num)):
#     for x in range(int(num)):
#         chrImg = ConvertToImg(x_train[i].reshape(width, height))
#         IMG.paste(chrImg, (width * x, height * y))
#         i = i + 1

# IMG.show()
# IMG.save('mnist.jpg', 'JPEG', quality=100, optimize=True)

# matplotlib
fig = plt.figure(figsize=(num,num))
for i in range(num * num):
    ax = fig.add_subplot(num, num, i + 1, xticks=[], yticks=[])
    ax.imshow(x_train[i].reshape((width,height)), cmap='gray')
plt.show()
