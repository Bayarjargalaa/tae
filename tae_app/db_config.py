from dotenv import load_dotenv
import os
from pathlib import Path
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# .env файлыг унших
# .env файлын байршлыг тодорхойлох
dotenv_path = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path)

# load_dotenv()

server = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
