import os
from datetime import datetime

ROOT_DIR = os.getcwd()

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
    
CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"
FEATURE_COLUMN = "features"
TARGET_COLUMN = "target"
CONFIG_FILE_PATH = os.path.join(CONFIG_DIR,CONFIG_FILE_NAME)
MODEL_CHECK = "saved_models.yaml"
MODEL_TRAINER_INDICATOR = "is_training started"
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

# Training pipeline related variable
TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = "artifact_dir"
ARTIFACT_BASE_FOLDER_NAME_KEY = "artifact_folder_name" 


# Data Ingestion related variable
DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"
DATA_INGESTION_DOWNLOAD_URL_KEY = "dataset_download_url"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_RAR_DOWNLOAD_DIR_KEY = "rar_download_dir"
DATA_INGESTION_INGESTED_DIR_NAME_KEY = "ingested_dir"
DATA_INGESTION_TRAIN_DIR_KEY = "ingested_train_dir"
DATA_INGESTION_TEST_DIR_KEY = "ingested_test_dir"