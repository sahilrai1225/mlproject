import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts',"train.csv") ## artifact file and this is path where the output of dataIngestion will be stored 
    # will save all the file in this path
    ## our dataingestion will save the train.csv file in this particular path
    test_data_path:str=os.path.join('artifacts',"test.csv")
    raw_data_path: str =os.path.join('artifacts',"data.csv")
    
    
    ## These are inputs that we are giving to our dataingestion componets and now data ingestion know whr to save train,test,raw data
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        # this Data ingetion config consist the 3 values beacuse this is the input that we need intializze 
        # as soon we will call this the 3 class varicble will be created
    def initiate_data_ingestion(self):
        ## If our data is saved in any database we will write code here to get from database
        ## we can create a mongodb client/mysql clinet in utils and we can read it
        logging.info("Entered The dataingestion method or componets")
        
        # as a starter we are reading from csv then will move to database
        try:
            df=pd.read_csv('notebook/data/stud.csv')
            ## keep logging so any where exception happen you will know
            logging.info('Read the dataset as dataframe')
            
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)#creating folder
            
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True) # raw data path will be saved with help of this
            
            logging.info('Train test split initiated')
            
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True) ## we are saving test and test in artifact folder
            
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info("Ingestion of data completed")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                
            )
            
            # return beacuse this will required for data tranfromation
            # we will just grab this info  and start our process of data tranformation
        except Exception as e:
            raise CustomException(e,sys)
        
        
if __name__=="__main__": ## initiate
    obj=DataIngestion()
    obj.initiate_data_ingestion()# artifact folder will bw created once we execute this