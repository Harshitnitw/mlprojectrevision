import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import  dataclass


class DataIngestionConfig:
    def __init__(self):
        self.train_data_path:str=os.path.join("artifacts","train.csv")
        self.test_data_path:str=os.path.join("artifacts","test.csv")
        self.raw_data_path=str.os.path.join("artifacts","data.csv")

    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered data ingestion method or component")
        try:
            df=pd.read_csv('notebook/data/stud.csv')
            logging.info('Read dataset as df')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiating")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("ingestion of data completed")

            return(
                self.ingestion_config.train_data_path,self.ingestion_config.test_data_path
            )
        except:
            pass