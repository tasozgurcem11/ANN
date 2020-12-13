import matplotlib.pyplot as plt
import numpy as np
from image_data import rand_image, add_noise, generate_noise, image_list_to_array

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


#ağırlık matrisi oluşturma
weight_1 = np.random.uniform(-0.15,0.15,size=(50,13))
print(x)
print(weight_1)

d = np.matmul(x, weight_1)
print(d)









