import yaml
import os

callouts_file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'example_callouts.yml')
team_file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'my_sponsors.yml')

def get_callouts_data():
    with open(callouts_file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

def get_team_data():
    with open(team_file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data
