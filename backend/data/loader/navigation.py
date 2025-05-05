import yaml
import os

# Define the path to the navigation.yml file
file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'navigation.yml')

def get_navigation_data():
    # Load the YAML file
    with open(file_path, 'r') as file:
        navigation_data = yaml.safe_load(file)
    return navigation_data
