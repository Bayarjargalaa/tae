import os
from .connect_db import connect_to_database

def fetch_and_save_views_to_file(conn, folder_path="output", filename="views_list.txt"):
    """
    VIEW хүснэгтүүдийн нэрсийг файлаар хадгалах функц.
    """
    try:
        # Фолдер байгаа эсэхийг шалгах, байхгүй бол үүсгэх
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        # Файл хадгалах бүрэн замыг үүсгэх
        full_path = os.path.join(folder_path, filename)
        
        # VIEW хүснэгтүүдийг татаж файлд бичих
        cursor = conn.cursor()
        cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.VIEWS")
        rows = cursor.fetchall()
        
        with open(full_path, 'w') as file:
            for row in rows:
                file.write(row[0] + "\n")
        print(f"Views saved to {full_path}")
    except Exception as e:
        print(f"Error while fetching and saving views: {e}")
    finally:
        cursor.close()

# Холболт үүсгэж функцыг дуудах
connection = connect_to_database()
if connection:
    fetch_and_save_views_to_file(connection, folder_path="output", filename="views_list.txt")
    connection.close()
