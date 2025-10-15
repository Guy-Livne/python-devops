from pathlib import Path
from typing import Union
import re

def archive_log_files(log_directory: Union[str, Path], archive_date: str) -> list[Path]:
    """
    Finds and renames all .log files in a directory with a date stamp.

    Args:
        log_directory (Union[str, Path]): The directory to scan.
        archive_date (str): The date stamp to use for renaming (YYYY-MM-DD).

    Returns:
        list[Path]: A list of the new Path objects for the renamed files.
    
    Raises:
        TypeError: If an argument has an invalid type.
        ValueError: If an argument has an invalid value or format.
        
    """
    
    if not isinstance(log_directory,str) and not isinstance(log_directory,Path):
        raise TypeError("'log_directory' must be str or a Path object")
        
    if not isinstance(archive_date,str):
        raise TypeError("'archive_date' must be str")
        
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", archive_date):
        raise ValueError("'archive_date' is not in a date format (YYYY-MM-DD)")
        
    
    used_dir= log_directory if isinstance(log_directory,Path) else Path(log_directory)
    
    if not used_dir.is_dir():
        raise ValueError("'log_directory' is not a directory")  
        
    path_list=[]
    for file in used_dir.iterdir():
        if file.suffix =='.log':
            new_name= f"{file.stem}-{archive_date}{file.suffix}"
            new_path= file.with_name(new_name)
            file.rename(new_path)
            path_list.append(new_path)

    return path_list
    
    
                    
    # TODO: Implement input validation first.
    # TODO: Rename .log files following instructions.
    # TODO: Return a list of renamed files.