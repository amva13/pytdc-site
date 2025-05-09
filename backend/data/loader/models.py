import yaml
import os

# Define the path to the navigation.yml file
file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'models.yml')

def get_models_data():
    # Load the YAML file
    with open(file_path, 'r') as file:
        models = yaml.safe_load(file)
    return models
