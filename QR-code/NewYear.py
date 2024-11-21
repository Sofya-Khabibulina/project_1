"""Модуль создания рамки под тематику Новый год"""
from PIL import Image
import requests
from io import BytesIO


def new_year(qrcode_path, image_url, output_path):
  """Декорирует QR-код под тематику "Новый год", вставляет изображение вокруг указанного QR-кода и сохраняет результат."""

  # Загружаем изображение рамки из URL
  response = requests.get(image_url)
  border_image = Image.open(BytesIO(response.content))

  qr_code = Image.open(qrcode_path)

  # Получаем размеры
  qr_width, qr_height = qr_code.size
  border_width, border_height = border_image.size

  # Создаем новое изображение с размерами QR-кода + размеры рамки
  new_image = Image.new("RGBA", (qr_width + border_width, qr_height + border_height))

  # Cовмещаем рамку и QR-код
  new_image.paste(border_image, (100, 150))
  new_image.paste(qr_code, (border_width // 4, border_height // 3))

  # Сохраняем итоговое изображение
  new_image.save(output_path)
  print(f"QR-код с рамкой сохранен как {output_path}")