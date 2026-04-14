from sources.config.settings import settings 

def main():
    print("SOURCE_URL =", settings.SOURCE_URL)
    print("MONGO_URI =", settings.MONGO_URI)
    print("SUPABASE_DB_URL =", settings.SUPABASE_DB_URL)

if __name__ == "__main__":
    main()