from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline

STAGE_NAME = "Data Ingestion"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started  <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} complete  <<<<<<\n\nx=====================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} complete <<<<<")
except Exception as e:
    logger.error(f"Error in {STAGE_NAME} : {e}")

STAGE_NAME = "Data Transformation"

try:
    logger.info(f">>>>> stage {STAGE_NAME} <<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.error(f"Exception occured in {STAGE_NAME}")
    raise e