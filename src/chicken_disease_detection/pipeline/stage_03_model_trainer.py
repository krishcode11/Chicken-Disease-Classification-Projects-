from chicken_disease_detection.config.configuration import ConfigurationManager
# pyrefly: ignore [missing-import]
from chicken_disease_detection.components.model_trainer import Training
from chicken_disease_detection import logger




STAGE_NAME = "Training"



class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()
