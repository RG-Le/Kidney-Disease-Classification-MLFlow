from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_training import Training
from cnnClassifier import logger

STAGE_NAME = "Training"


class ModelTainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_genarator()
        training.train()
        

if __name__ == '__main__':
    try:
        logger.info(f"*************************")
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = ModelTainingPipeline()
        obj.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx===================x")
    except Exception as e:
        raise e