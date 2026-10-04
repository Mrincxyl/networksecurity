import os 
import sys
import json 
from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL =  os.getenv("MONGO_DB_URL")


import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo 

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


class NetworkDataExtract():
    
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def csv_to_json_converter(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records = data.to_dict(orient='records')
            return records  
            
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_mongodb(self,records,database_name,collection_name):
        try:
            self.database_name = database_name
            self.collection_name = collection_name
            self.records = records
            
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL,tlsCAFile=ca)
            
            db = self.mongo_client[self.database_name]
            collection = db[self.collection_name]
            result = collection.insert_many(self.records)
            return (len(self.records))
            
        except Exception as e:
            raise NetworkSecurityException(e,sys)
            

if __name__=="__main__":
    FILE_PATH =  "Network_Data/phisingData.csv"   
    Database = "Mrincxyl"
    Collection = "NetworkData" 
    try:
        networkobj = NetworkDataExtract()
        records = networkobj.csv_to_json_converter(FILE_PATH)
        print(f"Sample Record to Insert: {records[0] if records else 'No data extracted'}")
    
        len_records = networkobj.insert_data_mongodb(records,Database,Collection)
        print(f"Successfully inserted {len_records} records into MongoDB.")
    except Exception as e:
        print(f"Execution failed: {e}")    
            