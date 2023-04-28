import yaml 
from HeartClassification.exception import HeartException 
import os,sys 
# from HeartClassification.config.start_spark_session import spark_session 
import dill 

def read_yaml(file_path:str):
    """
    Reads a yaml file and returns the contents as dictionary.
    """
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HeartException(e,sys) from e 