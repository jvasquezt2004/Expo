import cv2
import matplotlib.pyplot as plt
import numpy as np


def apply_cubic_interpolation(image, new_width, new_height):
    result = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_CUBIC)

    plt.figure(figsize=(8, 4))

    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.imshow(image)
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.title("Interpolacion Cubic")
    plt.imshow(result)
    plt.axis("off")

    plt.show()
