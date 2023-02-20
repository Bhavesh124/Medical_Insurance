from Insurance.pipeline.batchprediction import start_batch_prediction
from Insurance.pipeline.trainingpipeline import start_training_pipeline

file_path=r"/config/workspace/insurance.csv"
print(__name__)
if __name__=="__main__":
    try:
        output_file = start_training_pipeline()
        output_file = start_batch_prediction(input_file_path=file_path)
        print(output_file)

    except Exception as e:
        print(e)