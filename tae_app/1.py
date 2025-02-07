# views.py
import pandas as pd
import os
from .models import ItemView

def import_excel_to_db():
    # Excel файлын замыг тодорхойлох
    folder_path = 'files'  # Энд таны фолдерын замыг оруулна
    file_name = 'names.xlsx'   # Эксэл файлын нэрийг оруулна
    file_path = os.path.join(folder_path, file_name)

    # Excel файлыг уншина
    df = pd.read_excel(file_path)
    
    # Excel-ийн мөрүүдийг дамжуулж Django-ийн Model-д хадгалах
    for index, row in df.iterrows():
        ItemView.objects.create(
            name=row['Name'],
            box_number=row['Box Number'],
            size=row['Size'],
            country=row['Country'],
            image_url=row['Image URL']  # Зургийн линкийг оруулсан гэж төсөөлье
        )

print(import_excel_to_db())