import pymongo
import json
import pandas as pd

client = pymongo.MongoClient("mongodb+srv://mongodb:mongodb@cluster0.4ajckbg.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = "/config/workspace/insurance.csv"
DATABASE_NAME = "INSURANCE"
COLLECTION_NAME = "INSURANCE_PROJECT"

if __name__=="__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns:",df.head())

    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)