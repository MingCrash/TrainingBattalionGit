from PIL import Image
import tesserocr

#设置二值化阀值
def grad(threshold):
    grad = []
    threshold = 100
    for i in range(256):
        if i < threshold:
            grad.append(0)
        else:
            grad.append(1)
    return grad

image1=Image.open('test4.jpeg')
#做灰度处理
image1L = image1.convert('L')
#二值化
# image11 = image1L.convert('1')

#设置二值化阀值
grad = grad(100)
image11 = image1L.point(grad,'1')
print(tesserocr.image_to_text(image11))



print(tesserocr.file_to_text('test4.jpeg'))
print(tesserocr.file_to_text('test3.jpg'))
print(tesserocr.file_to_text('test2.jpg'))
print(tesserocr.file_to_text('test1_1.jpg'))