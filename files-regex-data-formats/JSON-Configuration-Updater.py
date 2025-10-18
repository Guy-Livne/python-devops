import json
from pathlib import Path


def update_image_tag(config_path: str | Path, service_name: str, new_tag: str) -> None:
    """
    Reads a JSON config file, updates a service's image tag, and writes it back.
    """
    if not isinstance(config_path,str) and not isinstance(config_path,Path):
        raise TypeError(f"'config_path' must be type str or type Path. currnet type {type(config_path)}")
        
    if not isinstance(service_name,str):
        raise TypeError(f"'service_name' must be type str. currnet type {type(service_name)}")

    if not isinstance(new_tag,str):
        raise TypeError(f"'new_tag' must be type str. currnet type {type(new_tag)}")
        
    if service_name=="":
        raise ValueError("'service_name' must be a non empty string")
    
    if new_tag=="":
        raise ValueError("'new_tag' must be a non empty string")
        
    config_path = Path(config_path) if not isinstance(config_path,Path) else config_path
    
    if config_path.name=='.':
        raise ValueError("'config_path' must point to a json file, entering empty string will cuase it to point the cwd")
    
    if not config_path.exists():
        raise FileNotFoundError("file in 'config_path' doesn't exists...")
    
    with open(config_path,'r') as file:
        json_file=json.load(file)
        try:
            json_file["services"][service_name]["image_tag"]=new_tag
               
        except KeyError:
            if not 'services' in json_file.keys():
                raise KeyError("key 'services' doesn't exist in this json file...")
                
            elif not service_name in json_file["services"].keys():
                raise KeyError(f"key '{service_name}' doesn't exist in this json file...")
                
            elif not "image_tag" in json_file["services"][service_name].keys():
                raise KeyError("key 'image_tag' doesn't exist in this json file...")
                
            
        except Exception as e:
            raise e(f"somting went worng,excption type: {e}")
            
        try:
            with open(config_path, 'w') as f:
                json.dump(json_file, f, indent=4)
        except IOError as e:
            raise IOError(f"Could not write updated data to file '{config_path}': {e}")
    
    # TODO: Implement input validation.
    # TODO: Read, update, and save updated JSON object.
    # Remember to use an indent of 4 for human-readable output.
    