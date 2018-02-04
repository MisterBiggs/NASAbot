import json



with open('trainastronaut.json', 'r') as f:
    distros_dict = json.load(f)

for distro in distros_dict:
    print(distro['retweeted'])
