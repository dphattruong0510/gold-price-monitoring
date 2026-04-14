import os 
from dotenv import load_dotenv 

load_dotenv()

class Settings:
    SOURCE_URL= os.getenv("SOURCE_URL","https://www.24h.com.vn/gia-vang-hom-nay-c425.html")
    MONGO_URI= os.getenv("MONGO_URI")
    SUPABASE_DB_URL = os.getenv("SUPABASE_DB_URL")
    SUPABASE_DB_HOST = os.getenv("SUPABASE_DB_HOST")
    SUPABASE_DB_PORT = os.getenv("SUPABASE_DB_PORT")
    SUPABASE_DB_USER = os.getenv("SUPABASE_DB_USER")
    SUPABASE_DB_PASSWORD = os.getenv("SUPABASE_DB_PASSWORD")

settings = Settings()
