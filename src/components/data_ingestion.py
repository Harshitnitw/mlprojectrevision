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
        