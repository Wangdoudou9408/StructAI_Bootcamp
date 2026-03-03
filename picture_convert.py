# numpy的使用练习
from PIL import Image
import numpy as np
#图像改变
a=np.array(Image.open("/Users/wangdoudou/PycharmProjects/StructAI_Bootcamp/1.jpg"))
print(a.shape, a.dtype)
b=[255,255,255]-a
im2=Image.fromarray(b.astype(np.uint8))
im2.save("2.jpg")

#图像手绘风格
a=np.asarray(Image.open("1.jpg").convert('L')).astype('float')#先转为二维的灰度值
depth=10. #预设深度为10 取值范围为0-100
grad = np.gradient(a)
grad_x, grad_y = grad #提取x和y方向的梯度值
grad_x=grad_x*depth/100  #根据深度调整x和y方向的梯度值
grad_y=grad_y*depth/100
vec_el = np.pi/2.2
vec_az = np.pi/4.0
dx = np.cos(vec_el)*np.cos(vec_az)
dy = np.cos(vec_el)*np.sin(vec_az)
dz = np.sin(vec_el)
A=np.sqrt(grad_x**2+grad_y**2+1.0) #开平方根，避免除以 0 / 数值下溢，保证计算稳定；平滑梯度突变，适配 AI 模型学习；方便后续梯度方向归一化；
uni_x=grad_x/A
uni_y=grad_y/A
uni_z=1.0/A
b=255*(dx*uni_x+dy*uni_y+dz*uni_z)
b=b.clip(0,255)#为避免图像溢出，将生成的灰度值裁剪至0-255
im3= Image.fromarray(b.astype(np.uint8))
im3.save("3.jpg")








