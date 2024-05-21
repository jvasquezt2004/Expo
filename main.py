import cv2
import matplotlib.pyplot as plt
import numpy as np

from cubic_interpolation import apply_cubic_interpolation
from nearest_neighbor import apply_nearest_neighbor_interpolation
from reflection import apply_reflection
from rotation import apply_rotation


def main():
    image_path = "test.jpg"
    image = cv2.imread(image_path)
    if image is None:
        print(f"No se pudo cargar la imagen {image_path}")
        exit(1)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    print("Que operacion desea realizar?")
    print("1. Reflejo")
    print("2. Rotacion")
    print("3. Interpolacion por vecino mas proximo")

    choice = input("Introduce el numero de la operacion que decea realizar ")

    if choice == "1":
        print("Que tipo de reflejo desea hacer?")
        print("1. Horizontal")
        print("2. Vertical")
        reflection_type = int(
            input("Introduce el numero de la operacion que decea realizar ")
        )
        apply_reflection(image, reflection_type)
    if choice == "2":
        print("Que tipo de rotacion desea hacer?")
        print("1. 90 grados")
        print("2. 180 grados")
        print("3. 270 grados")
        rotation_type = int(
            input("Introduce el numero de la operacion que decea realizar ")
        )
        apply_rotation(image, rotation_type)
    if choice == "3":
        print("Que tipo de interpolacion desea hacer?")
        print("1. Nearest Neighbor")
        print("2. Cubica")
        interpolation_type = int(
            input("Introduce el numero de la operacion que decea realizar ")
        )
        new_width = int(input("Introduce el nuevo ancho de la imagen"))
        new_height = int(input("Introduce el nuevo alto de la imagen"))
        if interpolation_type == 1:
            apply_nearest_neighbor_interpolation(image, new_width, new_height)
        elif interpolation_type == 2:
            apply_cubic_interpolation(image, new_width, new_height)


main()
