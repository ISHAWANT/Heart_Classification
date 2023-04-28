from HeartClassification.entity.artifact_entity import DataIngestionArtifact
from HeartClassification.entity.config_entity import DataIngestionConfig 
import os,sys 
from HeartClassification.logger import logging 
from HeartClassification.exception import HeartException 
import tarfile 
from six.moves import urllib  
import pandas as pd 
import numpy as np 
from zipfile import ZipFile 

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'*'*20}Data Ingestion log started{'*'*20}") 
            self.data_ingestion_config=data_ingestion_config 
        except Exception as e:
            raise HeartException(e,sys) from e 
        
    def download_heart_data(self)->str:
        try:
            download_url = self.data_ingestion_config.dataset_download_url 
            rar_download_dir = self.data_ingestion_config.rar_download_dir
            
            if os.path.exists(rar_download_dir):
                os.remove(rar_download_dir) 
            os.makedirs(rar_download_dir,exist_ok=True) 
            
            rar_file_name = os.path.basename(download_url) 
            
            rar_file_path = os.path.join(rar_download_dir,rar_file_name) 
            logging.info(f"Downloding file from : [{download_url}] into [{rar_file_path}]") 
            
            #Downloading data 
            urllib.request.urlretrieve(download_url,rar_file_path) 
            
            logging.info(f"File [{rar_file_path}] has download succesfully")
            return rar_file_path 
        except Exception as e:
            raise HeartException(e,sys) from e 
    def extract_rar_file(self,rar_file_path:str):
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir 
            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir) 
            os.makedirs(raw_data_dir,exist_ok=True) 
            logging.info(f"Extracting rar file:[{rar_file_path}] into dir [{raw_data_dir}]")
            
            with ZipFile(rar_file_path) as rar_file_obj:
                rar_file_obj.extractall(path=raw_data_dir) 
            logging.info(f"Extraction completed") 
        except Exception as e:
            raise HeartException(e,sys) from e 
        
    def split_data_as_train_test(self)-> DataIngestionArtifact:
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir 
            csv_file_name = os.listdir(raw_data_dir)[0] 
            
            csv_file_path = os.path.join(raw_data_dir,csv_file_name) 
            logging.info(f"reading csv file: [{csv_file_path}]") 
            path = csv_file_path 
            heart_data_frame = pd.read_csv(path=path,header=True) 
            
            #Spliting file into training and testing 
            logging.info(f"Spliting file into training and testing") 
            train_dataset = None 
            test_dataset = None 
            (train_dataset,test_dataset) = heart_data_frame.randomSplit([0.8,0.2]) 
            
            train_dir = os.path.join(self.data_ingestion_config.ingested_train_dir,csv_file_name) 
            test_dir = os.path.join(self.data_ingestion_config.ingested_test_dir,csv_file_name) 
            
            if train_dataset is not None:
                os.makedirs(train_dir,exist_ok=True)
                logging.info(f"Dumping train data into [{train_dir}]") 
                train_dataset.write.csv(path=train_dir)
                
            if test_dataset is not None:
                os.makedirs(train_dir,exist_ok=True) 
                logging.info(f"Dumping data into [{test_dir}]")
                test_dataset.write.csv(path=test_dir)
                
            data_ingestion_artifact = DataIngestionArtifact(train_file_path=train_dir,
                                                            test_file_path=test_dir,
                                                            message=f"Data ingestion completed",
                                                            is_ingested=True)
            logging.info(f"DataIngestionArtifact:[{DataIngestionArtifact}]") 
            return data_ingestion_artifact
        
        except Exception as e:
            raise HeartException(e,sys) from e 
    def initiate_data_ingestion(self)->DataIngestionArtifact:
        try:
            rar_file_path = self.download_heart_data() 
            self.extract_rar_file(rar_file_path)
            return self.split_data_as_train_test()
        except Exception as e:
            raise HeartException(e,sys) from e 
    def __del__(self):
        logging.info(f"{'*'*20} Data Ingestion log completed {'*'*20}")