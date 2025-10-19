import shutil
from pathlib import Path

def create_backup(source_dir: str | Path, dest_dir: str | Path) -> None:
    """
    Creates a clean backup of a source directory to a destination directory.

    If the destination directory exists, it is removed before copying.

    Args:
        source_dir (Union[str, Path]): The directory to back up.
        dest_dir (Union[str, Path]): The directory to create the backup in.
    """
    if not isinstance(source_dir,str) and not isinstance(dest_dir,Path):
        raise TypeError(f"'source_dir' must be type str or Path. current type: {source_dir}")
        
    if not isinstance(dest_dir,str) and not isinstance(dest_dir,Path):
        raise TypeError(f"'dest_dir' must be type str or Path. current type: {dest_dir}")
    
        
    path_source= source_dir if isinstance(source_dir,Path) else Path(source_dir)
    
    path_dest= dest_dir if isinstance(dest_dir,Path) else Path(dest_dir)
    
    if path_source.name == ".":
        raise ValueError("'source_dir' must be a non empty string")
    
    if path_dest.name == ".":
        raise ValueError("'dest_dir' must be a non empty string")
        
    if not path_source.exists():
        raise ValueError(f"couldn't find dir in 'source_dir' = {source_dir}")

    if path_dest.exists():
        shutil.rmtree(path_dest)



    shutil.copytree(path_source,path_dest)
        
        
        
        
    
    # TODO: Implement input validation.
    # TODO: Check if the destination exists; if yes, remove it.
    # TODO: Copy the source to the destination.
