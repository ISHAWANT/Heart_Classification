from HeartClassification.entity.config_entity import * 
from HeartClassification.exception import HeartException 
from HeartClassification.logger import logging 
from HeartClassification.constant import * 
import os,sys 

class Configuration:
    def __init__(self,config_file_path=CONFIG_FILE_PATH,current_time_stamp= CURRENT_TIME_STAMP)->None:
        try:
            self.config_info = read_yaml