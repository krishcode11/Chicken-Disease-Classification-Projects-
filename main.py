from chicken_disease_detection.pipeline.stage_02_prepare_base_mode import PrepareBaseModelTrainingPipeline
from chicken_disease_detection import logger
from chicken_disease_detection.pipeline.stage_01_data_integration import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\n")
except Exception as e:
    logger.error(f"Error in stage {STAGE_NAME}: {e}")
    raise e



STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\n")
except Exception as e:
    logger.error(f"Error in stage {STAGE_NAME}: {e}")
    raise e