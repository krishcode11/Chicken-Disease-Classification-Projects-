from chicken_disease_detection.config.configuration import ConfigurationManager
from chicken_disease_detection.components.prepare_base_model import PrepareBaseModel
from chicken_disease_detection import logger


STAGE_NAME = "Prepare base model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__ == "__main__":
    try:
        logger.info(f"\n{'='*10} STAGE: {STAGE_NAME} STARTED {'='*10}")
        pipeline = PrepareBaseModelTrainingPipeline()
        pipeline.main()
        logger.info(f"\n{'='*10} STAGE: {STAGE_NAME} COMPLETED {'='*10}")
    except Exception as e:
        logger.error(f"{'='*10} STAGE: {STAGE_NAME} FAILED {'='*10}")
        logger.error(f"Error: {e}")
        raise e