from sqlalchemy import create_engine
from sources.config.settings import settings

def get_engine():
    if not settings.SUPABASE_DB_URL:
        raise ValueError("SUPABASE_DB_URL is missing in environment variables")

    return create_engine(settings.SUPABASE_DB_URL)