# in this pipleine we will create a prediction pipeline
import sys
import pandas as pd

from src.exception import CustomException
from src.logger import logging 
from src.utils import load_object # to load pkl file


class PredictPipeline:
    def __init__(self):
        pass # bydefault empty const
    
    def predict(self,features):#this predict is just like model prediction it will do prediction
        try:
            model_path='artifacts/model.pkl'
            preprocessor_path= 'artifacts/preprocessor.pkl' # this is responsible for handling categorical features ,feature scaling etc
            model=load_object(file_path=model_path) # this load_object is nothing but just to imoort pkl file # this function should be created  in utils
            preprocessor=load_object(file_path=preprocessor_path) 
        
            # after loading data awe need to sclaer
        
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e,sys)
    
    
class CustomData: # help to map all the input to the backends
    def __init__(self,
                 gender: str,
                 race_ethnicity: str,
                 parental_level_of_education,
                 lunch:str,
                 test_preparation_course: str,
                 reading_score:int,
                 writing_score:int):
        # now we will create a varible using self
        
        self.gender=gender
        self.race_ethnicity=race_ethnicity
        self.parental_level_of_education=parental_level_of_education
        self.lunch=lunch
        self.test_preparation_course=test_preparation_course
        self.reading_score=reading_score
        self.writing_score=writing_score
        
        
    def get_data_as_data_frame(self): # this function will return all input as a dataframe beacuse we trained our model as a df
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
                