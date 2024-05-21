import cv2
import matplotlib.pyplot as plt
import numpy as np


def apply_reflection(image, reflection_type):
    if reflection_type == 1:
        result = cv2.flip(image, 1)
    elif reflection_type == 2:
        result = cv2.flip(image, 0)
    else:
        raise ValueError("Invalid reflection")

    plt.figure(figsize=(8, 4))

    # Original Image
    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.imshow(image)
    plt.axis("off")

    # Reflected Image
    plt.subplot(1, 2, 2)
    plt.title("Reflejo" + (" Horizontal" if reflection_type == 1 else " Vertical"))
    plt.imshow(result)
    plt.axis("off")

    plt.show()
