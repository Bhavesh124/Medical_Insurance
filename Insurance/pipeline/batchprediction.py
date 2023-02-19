from Insurance.logger import logging
from Insurance.exception import InsuranceException
from typing import Optional
import numpy as np 
import pandas as pd
import os,sys
from datetime import datetime
from Insurance.utils import load_object
from Insurance.predictor import ModelResolver

PREDICTION_DIR = "prediction"

def start_batch_prediction(input_file_path):
    try:
        os.makedirs(PREDICTION_DIR, exist_ok=True)
        model_resolver = ModelResolver(model_registry="saves_models")
        #data loading
        df = pd.read_csv(input_file_path)
        df.replace({"na":np.NAN},inplace=True)

        #data vaildation
        transformer = load_object(file_path=model_resolver.get_latest_transformer_path())

        target_encoder = load_object(file_path=model_resolver.get_latest_target_encoder_path())

        input_feature_names = list(transformer.feature_names_in_)
        for i in input_feature_names:
            if df[i].dtypes =='object':
                df[i] = target_encoder.fit_transform(df[i])

        input_arr = transformer.transform(df[input_feature_names])

        model = load_object(file_path=model_resolver.get_latest_model_path())
        prediction = model.predict(input_arr)

        prediction_file_name = os.path.basename(input_file_path).replace(".csv",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.csv")
        prediction_file_path = os.path.join(PREDICTION_DIR,prediction_file_name)
        df.to_csv(prediction_file_path,index=False,header=True)

    except Exception as e:
        raise InsuranceException(error_message=e, error_detail=sys)