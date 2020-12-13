import matplotlib.pyplot as plt
import numpy as np

def add_noise(image):
    noisy = image + 0.2 * np.random.rand(5, 10)
    noisy = noisy / noisy.max()
    return noisy

def rand_image(image):
    rand_index = np.random.randint(0, 50)
    rand_image = np.array(image)
    rand_image[int(rand_index % 5),
    int(rand_index / 5)] = np.where(rand_image[int(rand_index % 5), int(rand_index / 5)] == 1,0.0, 1.0)
    return rand_image

def show_image(image):
    plt.imshow(image, cmap='gray')
    plt.show()

def generate_noise(image):
    noise1 = rand_image(image)
    noise2 = rand_image(image)
    noise3 = add_noise(image)
    noise_list = []

    noise_list.append(image)
    noise_list.append(noise1)
    noise_list.append(noise2)
    noise_list.append(noise3)

    for image in noise_list:
        show_image(image)
    return noise_list

def image_list_to_array(image_list):
    t = 0
    w = 50
    h = 13
    # image array oluştururken bayes için ilk başta tüm vektör 1 olarak tanımlanmıştır ancak son satır değişmediği için sadece son satır 1 kalır.
    image_array = [[1 for x in range(w)] for y in range(h)]
    for image in image_list:
        image_array_temporary = []
        for i in range (5):
            for k in range(10):
                image_array_temporary.append(image[i][k])
        for i in range(len(image_array_temporary)):
            image_array[t][i] = image_array_temporary[i]

        t = t + 1
    return image_array





