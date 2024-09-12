from PIL import Image

# Открытие уже загруженного изображения
image = Image.open('/Users/larisamosevica/Documents/GitHub/VD02/image.jpg')

# Уменьшение изображения до новых размеров (например, 800x600)
new_size = (600, 450)
resized_image = image.resize(new_size)

# Сохранение уменьшенного изображения
resized_image.save('resized_image.jpg')

print("Изображение уменьшено и сохранено.")
