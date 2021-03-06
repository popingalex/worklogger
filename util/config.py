import yaml
import os

PATH_PROFILE = 'profile.yaml'
PROFILE_EMPTY = {'username': 'EMPTY', 'password': 'EMPTY', 'ie_driver': 'Locate your IE Driver'}

if not os.path.exists(PATH_PROFILE):
    with open(PATH_PROFILE, 'w+', encoding='utf-8') as file:
        yaml.dump(PROFILE_EMPTY, file, allow_unicode=True, default_flow_style=False)
    print("complete configuration file please.")
    exit(1)

with open(PATH_PROFILE, 'r+', encoding='utf-8') as file:
    profile = yaml.load(file)
    if profile['username'] == 'EMPTY' or profile['password'] == 'EMPTY':
        print("complete configuration file please.")
        exit(1)
