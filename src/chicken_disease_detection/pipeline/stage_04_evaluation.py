from chicken_disease_detection.config.configuration import ConfigurationManager
from chicken_disease_detection.components.evaluation import Evaluation
from chicken_disease_detection import logger




STAGE_NAME = "Evaluation"



class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        evaluation_config = config.get_evaluation_config()
        evaluation = Evaluation(config=evaluation_config)
        evaluation.evaluation()
        evaluation.save_score()
