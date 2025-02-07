import os
import sys
import django
import csv
from django.conf import settings

# Django төслийн үндсэн замыг тохируулна
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)  # Төслийн үндсэн замыг Python замд нэмнэ
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taeproject.settings')  # Django төслийн тохиргоо
django.setup()

# Веб серверийн үндсэн URL
BASE_URL = "/static/images/"

# Static зургийн фолдерын зам
image_folder = os.path.join(BASE_DIR, 'static', 'images')
output_folder = os.path.join(BASE_DIR, 'output')
output_file = os.path.join(output_folder, 'image_urls.txt')

# Output фолдерыг үүсгэх
os.makedirs(output_folder, exist_ok=True)

# Зургийн файлуудын нэр болон URL-ийг бичих
with open(output_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # writer.writerow(['Image Name', 'Image URL'])  # Хийцийн нэрс

    # Зургийн фолдер дахь бүх зурагнуудыг шалгах
    for filename in os.listdir(image_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', 'webp')):
            image_url = f"{BASE_URL}{filename}"
            writer.writerow([image_url])  # Image name болон URL-ийг бичих

print(f"Image names and URLs written to {output_file}")
