# import matplotlib.pyplot as plt
# import numpy as np
# from image_data import rand_image, add_noise, generate_noise
# # image[:, 0] = 0
# # image[:, -1] = 0
# # image[0, :] = 0
# # image[-1, :] = 1
# # plt.imshow(image, cmap='gray')
# # plt.show()
#
# image0_list = []
# image0 = np.ones((5, 10))
# image0[:, 0] = 0
# image0[:, -1] = 0
# image0[0, :] = 0
# image0[-1, :] = 0
# image0_list = generate_noise(image0)
#
# #drawing plus sign:  "+"
# image1_list = []
# image1 = np.ones((5, 10))
# image1[:, 4] = 0
# image1[2, :] = 0
# image1_list = generate_noise(image1)
#
# image2_list = []
# image2 = np.ones((5, 10))
# image2[:, 0] = 0
# image2[0, :] = 0
# image2_list = generate_noise(image2)
#
# image3_list = []
# image3 = np.ones((5, 10))
# image3[:, 4] = 0
# image3[4, :] = 0
# image3_list = generate_noise(image3)
#
# image3l = []
# print(image3)
# for i in range(5):
#       for k in range(10):
#           image3l.append(image3[i][k])
#
# print(image3l)


import matplotlib.pyplot as plt
import numpy as np


def add_noise(img):
    noisy = img + 0.2 * np.random.rand(5, 10)
    noisy = noisy/noisy.max()
    plt.imshow(noisy, cmap='gray')
    plt.show()
    return noisy


def flip_rand(img):
    rand_index = np.random.randint(0, 50)
    rand_image = np.array(img)
    rand_image[int(rand_index % 5),
    int(rand_index / 5)] = np.where(rand_image[int(rand_index % 5), int(rand_index / 5)] == 1,
        0.0, 1.0)
    plt.imshow(rand_image, cmap='gray')
    plt.show()
    return rand_image

rectangle = np.ones((5, 10))
rectangle[:, 0] = 0
rectangle[:, -1] = 0
rectangle[0, :] = 0
rectangle[-1, :] = 0

cross = np.ones((5, 10))
cross[:, 5] = 0
cross[:, 4] = 0
cross[2 , : ] = 0

para_hor = np.ones((5, 10))
para_hor[1 , : ] = 0
para_hor[3 , : ] = 0

para_ver = np.ones((5, 10))
para_ver[:,2 ] = 0
para_ver[:,3 ] = 0
para_ver[:,6 ] = 0
para_ver[:,7 ] = 0


plt.imshow(rectangle, cmap='gray')
plt.show()
add_noise(rectangle)
flip_rand(rectangle)

plt.imshow(cross, cmap='gray')
plt.show()
add_noise(cross)
flip_rand(cross)

plt.imshow(para_hor, cmap='gray')
plt.show()
add_noise(para_hor)
flip_rand(para_hor)

plt.imshow(para_ver, cmap='gray')
plt.show()
add_noise(para_ver)
flip_rand(para_ver)







