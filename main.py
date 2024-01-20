from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline

##################################====DATA INGESTION STAGE====##################################
STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\n x===============================x")
except Exception as e:
        logger.exception(e)
        
        
###############################====PREPARE BASE MODEL STAGE====###################################
STAGE_NAME = 'Prepare Base Model Stage'
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    data_ingestion = PrepareBaseModelTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\n x===============================x")
except Exception as e:
        logger.exception(e)
        
        
        
###############################====TRAINING STAGE====###################################
STAGE_NAME = 'Training Stage'
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    data_ingestion = ModelTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\n x===============================x")
except Exception as e:
        logger.exception(e)
     
     
     
###############################====EVALUATION STAGE====###################################
STAGE_NAME = 'Evaluation Stage'
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    data_ingestion = EvaluationPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\n x===============================x")
except Exception as e:
        logger.exception(e)
     