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


