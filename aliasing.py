import cv2
import matplotlib.pyplot as plt

# Cargar la imagen
image = cv2.imread("test.jpg")

# Obtener las dimensiones de la imagen original
height, width = image.shape[:2]

# Calcular las nuevas dimensiones
new_height = height // 2
new_width = width // 2

# Redimensionar la imagen usando interpolación LANCZOS4 para reducir el aliasing
new_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4)

# Convertir la imagen de BGR a RGB para mostrarla con matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
new_image_rgb = cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB)

# Mostrar las imágenes usando matplotlib
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Imagen Original")
plt.imshow(image_rgb)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Imagen Antialiasing")
plt.imshow(new_image_rgb)
plt.axis("off")

plt.show()
