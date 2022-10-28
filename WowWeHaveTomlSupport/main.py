import tomllib
import json
import yaml

# With tomllib, you WILL HAVE TO USE Read-Binary mode
with open("sometoml.toml", "rb") as f:
    toml = tomllib.load(f)

with open("somejson.json", "r") as f:
    jayson = json.load(f)

with open("someyaml.yaml", "r") as f:
    yam = yaml.load(f, Loader=yaml.SafeLoader)


