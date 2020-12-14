import matplotlib.pyplot as plt
import numpy as np
from functions import *

image0_list = []
image0 = np.ones((5, 10))
image0[:, 0] = 0
image0[:, -1] = 0
image0[0, :] = 0
image0[-1, :] = 0
image0_list = generate_noise(image0)

#drawing plus sign:  "+"
image1_list = []
image1 = np.ones((5, 10))
image1[:, 4] = 0
image1[2, :] = 0
image1_list = generate_noise(image1)

image2_list = []
image2 = np.ones((5, 10))
image2[:, 0] = 0
image2[0, :] = 0
image2_list = generate_noise(image2)


total_image_list = image0_list + image1_list + image1_list
x = []
x = image_list_to_array(total_image_list)


#1.ağırlık matrisi oluşturma (50'lik matris seçilmiştir)
weight_1 = np.random.uniform(-0.15,0.15,size=(50,13))
print(len(x[0]))
print(len(weight_1[0]))

#ağırlık matrisi ile giriş değerlerini çarpma
v1 = np.matmul(weight_1, x)
print(len(v1[0]))

#aktivasyon fonksiyonu ile çarpma
y1 = []
y1 = activation_function(v1)
print(y1)




#2.ağırlık matrisi oluşturma (20'lik matris seçilmiştir)
weight_2 = np.random.uniform(-0.15,0.15,size=(20,51))
print(len(y1[0]))
print(len(weight_2[0]))

#y matrisine bayes ekleme
one_list = [1 for i in range(50)]
y1.append(one_list)

#ağırlık matrisi ile birinci çıkış değerlerini çarpma
v2 = np.matmul(weight_2, y1)

#aktivasyon fonksiyonu ile çarpma
y2 = []
y2 = activation_function(v2)
print(len(y2[0]))



#3.ağırlık matrisi oluşturma (3'lük matris seçilmiştir)
weight_3 = np.random.uniform(-0.15,0.15,size=(3,21))

#y matrisine bayes ekleme
one_list = [1 for i in range(50)]
y2.append(one_list)

#ağırlık matrisi ile ikinci çıkış değerlerini çarpma
v3 = np.matmul(weight_3, y2)

#aktivasyon fonksiyonu ile çarpma
y3 = []
y3 = activation_function(v3)
print("y çıkış matrisinin boyutu: " + str(len(y3)) + "x" +str(len(y3[0])))







