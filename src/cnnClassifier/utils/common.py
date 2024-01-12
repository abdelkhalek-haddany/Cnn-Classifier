import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger 
import json 
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml( path_to_yaml: Path) -> ConfigBox:
    """ read_yaml file and return 
    Args:
    path_to_yaml (Path): path to yaml file
    
    Raises:
        ValueError: if yaml file is empty
        e: empty yaml file
        
    Returns:
        ConfigBox: configBox type  
    """
    try:
        with open(path_to_yaml, 'r') as f:
            config = yaml.safe_load(f)
        return ConfigBox(config)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def save_json( path: Path, data: dict):
    """
        save json data 
        Args:
            path (Path): path to json file
            data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at: {path}")
    

@ensure_annotations
def load_json( path: Path) -> ConfigBox:
    """
        load json data 
        Args:
            path (Path): path to json file
        
        Returns:
            ConfigBox: data as a class attributes instead of dict  
    """
    with open(path, "r") as f:
        data = json.load(f)
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(data)

@ensure_annotations
def save_bin( data: Any, path: Path):
    """
        save binary data
        Args:
            data (Any): data to be saved        
            path (Path): path to binary file
    """
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved at: {path}")
     
@ensure_annotations
def load_bin( path: Path) -> Any:
    """
        load binary data
        Args:
            path (Path): path to binary file
        
        Returns:
            Any: data as a class attributes instead of dict  
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded successfully from: {path}")
    return data

@ensure_annotations
def get_size(path: Path)->str:
    """
        get size of file
        Args:
            path (Path): path to file
        
        Returns:
            str: size of file
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"

def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()
        

def encodingImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, 'rb') as f:
        imgdata = f.read()
    return base64.b64encode(imgdata)