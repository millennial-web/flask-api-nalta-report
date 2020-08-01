#!/usr/bin/env python
import sys
import pandas as pd
import pymongo
import json
import os


engine_string = os.environ.get('MONGODB_URI', '')

def import_content(filepath):
    mng_client = pymongo.MongoClient(engine_string)
    mng_db = mng_client['accidents_mx']
    collection_name = 'accidents'
    
    db_cm = mng_db[collection_name]
    cdir = os.path.dirname(__file__)
    file_res = os.path.join(cdir, filepath)

    data = pd.read_json(file_res)

    data_json = json.loads(data.to_json(orient='records'))
    db_cm.remove()
    db_cm.insert_many(data_json)

if __name__ == "__main__":
  filepath = 'data/accidents_time_gender.json'
  import_content(filepath)