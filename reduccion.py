import cv2
import matplotlib.pyplot as plt

# Cargar la imagen
image = cv2.imread("test.jpg")

# Obtener las dimensiones de la imagen original
height, width = image.shape[:2]

# Calcular las nuevas dimensiones (20% de las dimensiones originales)
scale_factor = 0.2  # Reducir la imagen a un 20%
new_height = int(height * scale_factor)
new_width = int(width * scale_factor)

# Redimensionar la imagen usando interpolación LANCZOS4 para mantener la calidad
resized_image = cv2.resize(
    image, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4
)

# Guardar la imagen redimensionada
cv2.imwrite("resized_image.jpg", resized_image)

# Convertir la imagen de BGR a RGB para mostrarla con matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
resized_image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

# Mostrar las imágenes usando matplotlib
plt.figure(figsize=(12, 6))

# Imagen Original
plt.subplot(1, 2, 1)
plt.title("Imagen Original\nDimensiones: {}x{}".format(width, height))
plt.imshow(image_rgb)
plt.axis("off")

# Imagen Redimensionada
plt.subplot(1, 2, 2)
plt.title(
    "Imagen Redimensionada (20%)\nDimensiones: {}x{}".format(new_width, new_height)
)
plt.imshow(resized_image_rgb)
plt.axis("off")

plt.show()

print("La imagen redimensionada se ha guardado como 'resized_image.jpg'.")
