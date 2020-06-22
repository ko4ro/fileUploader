from sklearn import datasets,model_selection
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


data_path = os.getcwd()
mnist = datasets.fetch_mldata('MNIST original', data_home=data_path)
DATA_SIZE = len(mnist.data)
train_size = 60000
test_size = DATA_SIZE - train_size

x_train, x_test, y_train, y_test = model_selection.train_test_split(mnist.data, mnist.target,train_size=train_size, test_size=test_size)

print(x_train.shape)
print(x_test.shape)
print(y_train.dtype)
print(y_test.shape)

# PILを使って一枚の画像にMNIST手書き画像をまとめて表示


def ConvertToImg(img):
    return Image.fromarray(np.uint8(img))


width = 28
height = 28
num = 10


# pillow
# MNISTの文字をPILで１枚の画像に描画する
IMG = Image.new('RGB', (int(width * num), int(height * num)), (255, 255, 255))

# MNISTの文字を読み込んで描画
i = 0
for y in range(int(num)):
    for x in range(int(num)):
        chrImg = ConvertToImg(x_train[i].reshape(width, height))
        IMG.paste(chrImg, (width * x, height * y))
        i = i + 1

IMG.show()
# IMG.save('mnist.jpg', 'JPEG', quality=100, optimize=True)

# matplotlib
fig = plt.figure(figsize=(num,num))
for i in range(num * num):
    ax = fig.add_subplot(num, num, i + 1, xticks=[], yticks=[])
    ax.imshow(x_train[i].reshape((width,height)), cmap='gray')
plt.show()

# x_train = np.asarray(x_train).astype(np.float32)
# y_train = np.asarray(y_train).astype(np.int32)
# x_test = np.asarray(x_test).astype(np.float32)
# y_test = np.asarray(y_test).astype(np.int32)
