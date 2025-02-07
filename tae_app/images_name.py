import os
import sys
import django
from django.conf import settings

# Django төслийн үндсэн замыг тохируулна
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)  # Төслийн үндсэн замыг Python замд нэмнэ
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taeproject.settings')  # Django төслийн тохиргоо
django.setup()

# Static зургийн фолдерын зам
image_folder = os.path.join(BASE_DIR, 'static', 'images')
output_folder = os.path.join(BASE_DIR, 'output')
output_file = os.path.join(output_folder, 'image_names.txt')

# Output фолдерыг үүсгэх
os.makedirs(output_folder, exist_ok=True)

# Зургийн фолдер дахь файлуудыг бичих
with open(output_file, 'w') as file:
    for filename in os.listdir(image_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', 'WEBP')):
            file.write(filename + '\n')
            # print(f"Found: {filename}")

print(f"Image names written to {output_file}")
