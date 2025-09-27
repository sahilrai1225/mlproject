from flask import Flask,request,render_template
import numpy as pd
import pandas as pd


from sklearn.preprocessing import StandardScaler # beacuse we need to use pkl file 
# we also have to use training pipleine # we have diffenret pipeline
from src.pipeline.predict_pipeline import CustomData,PredictPipeline


application=Flask(__name__)# will give entry point whre we need to executed

app=application

## Route for home page 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html') # in this home html there will be simple data field that will be provided to user for prediction
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score')))
        
        pred_df=data.get_data_as_data_frame() #this function is present in predict_pipelien which will convert data in df
        print(pred_df)

        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df) # asson a well cal predict_pipeline it will go to predict function inpredict_pipelie
        return render_template('home.html',results=results
                               
        )
        # get to get all info
        
    # it will connect to predict pipleine .py
    # in post part we have to capture the data and to standard scaling then prediction
if __name__=="__main__":      
    app.run(host="0.0.0.0",debug=True,port=5000)