import logging
import logging.handlers

def configure_rotating_logger(logger_name, log_filepath,max_size_bytes,backup_count):
    
    if not isinstance(logger_name,str) or not isinstance(log_filepath,str):
        raise TypeError(f"must be type 'str' \n logger_name = {type(logger_name)}"
        +"\n log_filepath = {type(log_filepath)} ")
    
    if logger_name == "" or log_filepath == "":
        raise ValueError(f"must be non empty strings \n logger_name = {logger_name}"
        +"\n log_filepath = {log_filepath} ")
        
    if not isinstance(max_size_bytes,int) or not isinstance(backup_count,int):
        raise TypeError(f"must be type 'int' \n logger_name = {type(logger_name)}"
        +"\n log_filepath = {type(log_filepath)} ")
        
    if max_size_bytes <=0 or backup_count <=0:
        raise ValueError(f"must be greater then zero \n logger_name = {logger_name}"
        +"\n log_filepath = {log_filepath} ")    
        
    
    new_logger=logging.getLogger(logger_name)
    new_logger.setLevel(logging.DEBUG)
    
    rotating_fh= logging.handlers.RotatingFileHandler(log_filepath
    ,maxBytes= max_size_bytes
    ,backupCount=backup_count
    )
    new_logger.addHandler(rotating_fh)
    
    return new_logger
    