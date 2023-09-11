import ruamel.yaml as yaml
from pathlib import Path
import requests
from rich import print

yaml = yaml.YAML()

root_dir = Path(__file__).parent.parent

data = yaml.load(root_dir / "_config.yml")

# with open("token.txt") as f:
#     token = f.read().strip()

# auth=("Remi-Gau", token)

# api_call = f"  https://api.github.com/repos/bids-apps/{}"
# r = requests.get(api_call)
# r.json()

for app in data["apps"]:

    print(app)

# rewrite config file
with open(root_dir / "_config.yml", "w") as f:
    yaml.dump(data, f)
