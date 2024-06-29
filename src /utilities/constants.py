"""
Constants
"""
import yaml

RESOLUTION = (640, 480)
DESIRED_POSITION = (320, 240)
SCALING_FACTOR = 0.01
MODE = "MILITARY"

def load_yaml(path = 'src /utilities/config.yaml'):
    """
    Load yaml config
    """
    with open(path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    return data

def set_variables(data):
    """
    Change constants
    """
    global RESOLUTION, DESIRED_POSITION, SCALING_FACTOR, MODE
    for config in ['RESOLUTION', 'DESIRED_POSITION', 'SCALING_FACTOR', 'MODE']:
        if config not in data:
            print(f"-- Missing {config} variable in config file. Using default values")
    if 'RESOLUTION' in data:
        RESOLUTION = tuple(data['RESOLUTION'])
    if 'DESIRED_POSITION' in data:
        DESIRED_POSITION = tuple(data['DESIRED_POSITION'])
    if 'SCALING_FACTOR' in data:
        SCALING_FACTOR = data['SCALING_FACTOR']
    if 'MODE' in data:
        MODE = data['MODE']
