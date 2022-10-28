import tomllib
import sys
import json
from typing import Union
sys.setrecursionlimit(10000)

# With tomllib, you WILL HAVE TO USE Read-Binary mode
with open("sometoml.toml", "rb") as f:
    toml = tomllib.load(f)

with open("somejson.json", "r") as f:
    jayson = json.load(f)

def print_kv(dataobj: Union[dict, list], indent: int = 0):
    if isinstance(dataobj, dict):
        for key, value in dataobj.items():
            if isinstance(value, dict):
                print(" " * indent, key+":")
                try:
                    print_kv(value, indent + 4)
                except RecursionError:
                    print(" " * (indent + 4), "...")
            else:
                print(" " * indent, key+":", value)
    elif isinstance(dataobj, list):
        for value in dataobj:
            print()
            print_kv(value, indent)


# print_kv(toml)
print_kv(jayson)