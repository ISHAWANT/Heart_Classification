from HeartClassification.entity.config_entity import * 
from HeartClassification.exception import HeartException 
from HeartClassification.logger import logging
from HeartClassification.constant import * 
import os,sys 
from HeartClassification.utils.utils import read_yaml_file

class Configuration:
    def __init__(self,config_file_path=CONFIG_FILE_PATH,current_time_stamp= CURRENT_TIME_STAMP)->None:
        try:
            self.config_info = read_yaml_file(file_path=config_file_path)
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.time_stamp = current_time_stamp
        except Exception as e:
            raise HeartException(e,sys) from e 
        
    #Data Ingestion 
    def get_data_ingestion_config(self)->DataIngestionConfig:
        
        logging.info('*'*15,'Data ingestion started','*'*15)
        try:
            data_ingestion_info = self.config_info[DATA_INGESTION_CONFIG_KEY] 
            artifact_dir = self.training_pipeline_config.artifact_dir 
            data_ingestion_artifact_dir = os.path.join(
                artifact_dir,
                DATA_INGESTION_ARTIFACT_DIR,
                self.time_stamp
            )
            
            dataset_download_url = data_ingestion_info[DATA_INGESTION_DOWNLOAD_URL_KEY]
            rar_download_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_RAR_DOWNLOAD_DIR_KEY]
            )
            raw_data_dir = os.path.join(
                data_ingestion_artifact_dir,data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY]
            )
            
            ingested_data_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_INGESTED_DIR_NAME_KEY]
            )
            
            ingested_train_dir = os.path.join(
                ingested_data_dir,
                data_ingestion_info[DATA_INGESTION_TRAIN_DIR_KEY]
            )
            
            ingested_test_dir = os.path.join(
                ingested_data_dir,
                data_ingestion_info[DATA_INGESTION_TEST_DIR_KEY]
            )
            
            data_ingestion_config = DataIngestionConfig(
                dataset_download_url=dataset_download_url,
                rar_download_dir=rar_download_dir,
                raw_data_dir=raw_data_dir,
                ingested_train_dir=ingested_train_dir,
                ingested_test_dir=ingested_test_dir
            )
            logging.info("*"*15,f"Data ingestion Config completed: {data_ingestion_config}","*"*15)
            return data_ingestion_config 
        except Exception as e:
            raise HeartException(e,sys) from e 
        
        
    def get_training_pipeline_config(self)->TrainingPipelineConfig:
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR,
                                        training_pipeline_config[ARTIFACT_BASE_FOLDER_NAME_KEY],
                                        training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
                                        )
            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir) 
            return training_pipeline_config
            
        except Exception as e:
            raise HeartException(e,sys) from e 