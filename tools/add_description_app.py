import ruamel.yaml as yaml
from pathlib import Path
import requests
from rich import print

yaml = yaml.YAML()

root_dir = Path(__file__).parent.parent

data = yaml.load(root_dir / "_config.yml")

with open("/home/remi/Documents/tokens/gh_user.txt") as f:
    token = f.read().strip()

auth=("Remi-Gau", token)

for idx, app in enumerate(data["apps"]):

    api_call = f"https://api.github.com/repos/{app['gh']}"
    r = requests.get(api_call, auth=auth)
    content = r.json()
    print(content["description"])
    app["description"] = content["description"]

    data["apps"][idx] = app


# rewrite config file
with open(root_dir / "_config.yml", "w") as f:
    yaml.dump(data, f)
