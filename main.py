from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTainingPipeline


if __name__ == "__main__":
    STAGE_NAME = "Data Ingestion Stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx===========x")
    except Exception as e:
        logger.exception(e)
        raise e


    STAGE_NAME = "Prepare Base Model"
    try:
        logger.info(f"*************************")
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        prepare_base_model = PrepareBaseModelTrainingPipeline()
        prepare_base_model.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx===================x")
    except Exception as e:
        logger.exception(e)
        raise e
    

    STAGE_NAME = "Training"
    try:
        logger.info(f"*************************")
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        model_trainer = ModelTainingPipeline()
        model_trainer.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx===================x")
    except Exception as e:
        logger.exception(e)
        raise e
