from Insurance.entity import config_entity,artifact_entity
from Insurance.logger import logging
from Insurance.exception import InsuranceException
import os,sys
import pandas as pd
from sklearn.pipeline import Pipeline
from Insurance import utils
from typing import Optional
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from Insurance.config import TARGET_COLUMN
from Insurance.predictor import ModelResolver
from Insurance.utils import load_object


class ModelEvaluation:
    def __init__(self,model_eval_config:config_entity.ModelEvaluationConfig,
                      data_ingestion_artifact:artifact_entity.DataIngestionArtifact,
                      data_transformation_artifact:artifact_entity.DataTransformationArtifact,
                      model_trainer_artifact:artifact_entity.ModelTrainerArtifact):

        try:
            self.model_eval_config = model_eval_config
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_transformation_artifact = data_transformation_artifact
            self.model_trainer_artifact = model_trainer_artifact
            self.model_resolver = ModelResolver()

        except Exception as e:
            raise InsuranceException(e, sys)

    def initiate_model_evaluation(self,)->artifact_entity.ModelEvaluationArtifact:
        try:
            latest_dir_path = self.model_resolver.get_latest_dir_path()
            
            if latest_dir_path == None:
                model_eval_artifact = artifact_entity.ModelEvaluationArtifact(is_model_expected=True,improved_accuracy=None)
            
            logging.info(f"Model evaluation artifact: {model_eval_artifact}")
            return model_eval_artifact

            # Find location previous model
            #transformer_path = self.model_resolver.get_latest_dir_path()
            #model_path = self.model_resolver.get_latest_model_path()
            #target_encoder_path = self.model_resolver.target_encoder_path()

            # Previous model
            #transformer = load_object(file_path = transformer_path)
            #model = load_object(file_path = model_path)
            #target_encoder = load_object(file_path = target_encoder_path)

            #New Model
            #current_transformer = load_object(file_path = self.data_transformation_artifact.transform_object_path)
            #current_model = load_object(file_path = self.data_transformation_artifact.model_path)
            #current_target_encoder = load_object(file_path = self.data_transformation_artifact.target_encoder_path)
        
        except Exception as e:
            raise InsuranceException(e, error_detail=sys)