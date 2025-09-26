import sys
from dataclasses import dataclass
import os


import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object # this is just used for saving pkl file
@dataclass
class DataTranformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl")
    # if we wnat to create any modle and want ro seve that in pkl path so we need path 
    # if we creating any pipleine pickle file its name is  preprocessor.pkl file /model.pkl file
    # in Data Tranformation Config we bascially just want to give input to data tranformation input
# wrt to Datatranformation class this is input we will probably be giving over here
class DataTransformation:
    def __init__(self):
        self.data_tranformation_config=DataTranformationConfig()
        # short in data_trannformation_config we will have preprocessor_obj_file_path variable
        
        
    def get_data_transformer_object(self):
            '''
            This function is reponsible for data tranformation based on diifernt types of data
            
            '''
            # this func is just to create a pkl file which will be resp for categ feature to num feature
            try:
                numerical_columns=['writing_score','reading_score']
                categorical_columns=['gender',
                                     'race_ethnicity',
                                     'parental_level_of_education',
                                     'lunch',
                                     'test_preparation_course']
                
                # now we will create a pipeline
                # steps are most important thing wrt this
                num_pipeline=Pipeline(
                    steps=[
                        ("imputer",SimpleImputer(strategy="median")),# for handling missing value # here we are using median beacuse their are somme oultiers
                        ("scaler",StandardScaler())
                    # we have created a pipeline which is doing 2 imp thing handle missing value and standardizing
                    # and this pipeline has to work on training data set Fit_trafor
                    ]
                )
                cat_pipeline=Pipeline(
                    steps=[
                        ("imputer",SimpleImputer(strategy="most_frequent")),
                        ("one_hot_encoder",OneHotEncoder()),
                        ("scaler",StandardScaler(with_mean=False))
                    ]
                    # in eda we have seen there were very less category wrt to categorical features
                ) 
                logging.info(f"categorical columns:{categorical_columns}")
                logging.info(f"numerical coulumns:{numerical_columns}")
                
                # now we have to combine numerical pipeline with categorical pipleine for that we will use column trandformer
                preprocessor=ColumnTransformer([
                    ("num_pipeline",num_pipeline,numerical_columns),
                    ("cat_pipeline",cat_pipeline,categorical_columns)
                ])

                return preprocessor # returning preprocessor means we are returning every thing
                
            except Exception as e:
                raise CustomException(e,sys)
            
            
            # lets start our data tranformation technique
            
    def initiate_data_tranformation(self,train_path,test_path):
        
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            
            logging.info("Read train and test data completed")
            
            logging.info("obtaining preprocessing object")
            
            preprocessing_obj=self.get_data_transformer_object()

            
            target_column_name="math_score"
            numerical_columns=["writing_score","reading_score"]
            
            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]
            
            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]
            
            logging.info(
                f"Applying Preprocessing object on training dataframe and testing dataframe"
            )
            # input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            # input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)   
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            
            train_arr=np.c_[
                input_feature_train_arr,np.array(target_feature_train_df)
            ]
            
            
            test_arr=np.c_[
                input_feature_test_arr,np.array(target_feature_test_df)
            ]
            # np.c_ is a shortcut for column-wise concatenation
            
            
            logging.info(f"Saved Preprocessing Object")
            #preprocessing_obk need to be converted in pkl file but yet we havn,t done,but we have taken a path and given in dataTranformationCofig like preprocessor pkl
            #now we will save pkl file in same locatiion
            
            save_object(
                file_path=self.data_tranformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj # we are giving this because this is a model wrt to data tranformation 
            )# utils is one place indie src where we will write this /call this save_object
            # beacuse utils will have all the common things which we will import//use // entire functionalities which entire project cqna use
            return(
                train_arr,
                test_arr,
                self.data_tranformation_config.preprocessor_obj_file_path,
                #preprocessor_obj_file_path is our pickle file
            )
        except Exception as e:
            raise CustomException(e,sys)