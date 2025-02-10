import pyodbc
import sys
from pathlib import Path

# Add the base directory to the sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from tae_app.db_config import server, database, username, password

def connect_to_database():
    try:
        conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
        conn = pyodbc.connect(conn_str)
        print("Successfully connected to the database!")
        return conn
    except Exception as e:
        print(f"Error: {e}")
        return None

