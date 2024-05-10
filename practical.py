import pandas as pd
from pymongo import MongoClient



mongo_url = "mongodb://localhost:27017/"
client = MongoClient(mongo_url)
database_name = "practical_db"


db = client[database_name]
collection_name = "csv_data"

collection = db[collection_name]
csv_file_path = "organizations.csv"

df = pd.read_csv(csv_file_path)
records = df.to_dict(orient='records')

result = collection.insert_many(records)
print(f"{len(result.inserted_ids)} documents inserted into MongoDB ")


client.close()

