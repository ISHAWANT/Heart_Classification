from collections import namedtuple 

DataIngestionArtifact = namedtuple("DataIngestionArtifact",
                                   ['train_file_path','test_file_path','message','is_ingested']) 
