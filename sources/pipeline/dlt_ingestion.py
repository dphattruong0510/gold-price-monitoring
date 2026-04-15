import dlt
from pymongo import MongoClient

from sources.config.settings import settings


@dlt.resource(name="prices", write_disposition="replace")
def mongo_prices():
    if not settings.MONGO_URI:
        raise ValueError("MONGO_URI is missing in environment variables")

    client = MongoClient(settings.MONGO_URI)
    db = client["gold_db"]
    collection = db["prices"]

    try:
        for doc in collection.find():
            doc["_id"] = str(doc["_id"])
            yield doc
    finally:
        client.close()


def load_mongodb_to_supabase() -> None:
    if not settings.SUPABASE_DB_URL:
        raise ValueError("SUPABASE_DB_URL is missing in environment variables")

    pipeline = dlt.pipeline(
        pipeline_name="gold_price_pipeline",
        destination="postgres",
        dataset_name="gold_raw",
    )

    load_info = pipeline.run(
        mongo_prices(),
        credentials=settings.SUPABASE_DB_URL,
    )

    print(load_info)


if __name__ == "__main__":
    load_mongodb_to_supabase()