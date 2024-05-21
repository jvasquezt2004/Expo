import cv2
import matplotlib.pyplot as plt
import numpy as np


def apply_rotation(image, rotation_type):
    if rotation_type == 1:
        result = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    elif rotation_type == 2:
        result = cv2.rotate(image, cv2.ROTATE_180)
    elif rotation_type == 3:
        result = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    else:
        raise ValueError("Invalid rotation")

    plt.figure(figsize=(8, 4))

    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.imshow(image)
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.title(
        "Rotacion"
        + (
            " 90 grados"
            if rotation_type == 1
            else " 180 grados" if rotation_type == 2 else " 270 grados"
        )
    )
    plt.imshow(result)
    plt.axis("off")

    plt.show()
