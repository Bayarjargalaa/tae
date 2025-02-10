import pyodbc
import os
from django.db import models
from dotenv import load_dotenv

# .env файлыг ачааллах
load_dotenv()

# MSSQL холболтын тохиргоо
server = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")



conn = pyodbc.connect(
    f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
)
cursor = conn.cursor()

# View-үүдийн нэрийг авах функц
def get_views():
    cursor.execute("SELECT table_name FROM information_schema.views")
    return [row[0] for row in cursor.fetchall()]

# View бүрийн баганы мэдээллийг авах функц
def get_columns(view_name):
    cursor.execute(f"""
        SELECT COLUMN_NAME, DATA_TYPE 
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_NAME = '{view_name}'
    """)
    return cursor.fetchall()

# Django Model үүсгэх функц
def generate_django_models():
    models_code = "from django.db import models\n\n"
    
    for view_name in get_views():
        models_code += f"class {view_name.capitalize()}(models.Model):\n"
        
        columns = get_columns(view_name)
        if not columns:
            models_code += "    pass\n\n"
            continue

        for column in columns:
            column_name = column.COLUMN_NAME.lower()
            data_type = column.DATA_TYPE.lower()

            # MSSQL төрлийг Django төрлүүдэд хөрвүүлэх
            field_type = {
                "int": "models.IntegerField()",
                "varchar": "models.CharField(max_length=255)",
                "nvarchar": "models.CharField(max_length=255)",
                "datetime": "models.DateTimeField()",
                "decimal": "models.DecimalField(max_digits=10, decimal_places=2)",
                "float": "models.FloatField()",
                "bit": "models.BooleanField()",
            }.get(data_type, "models.TextField()")  # Хэрэв тодорхойгүй төрөл байвал TextField()

            models_code += f"    {column_name} = {field_type}\n"
        
        models_code += "    class Meta:\n"
        models_code += f"        managed = False  # View учраас Django удирдахгүй\n"
        models_code += f"        db_table = '{view_name}'  # MSSQL дахь нэртэй тааруулж өгнө\n\n"

    return models_code

# Үүсгэсэн model кодыг models.py файлд хадгалах
models_file_path = "tae_app/models.py"  # Та өөрийн app-ийн models.py замыг оруулна уу
with open(models_file_path, "w", encoding="utf-8") as file:
    file.write(generate_django_models())

print(f"✅ Model файлыг амжилттай үүсгэлээ: {models_file_path}")

# Холболтыг хаах
conn.close()
