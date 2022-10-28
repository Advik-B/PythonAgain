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

def print_kv(dictobj: Union[dict, list], indent: int = 0):
    if isinstance(dictobj, dict):
        for key, value in dictobj.items():
            if isinstance(value, dict):
                print(" " * indent, key+":")
                try:
                    print_kv(value, indent + 4)
                except RecursionError:
                    print(" " * (indent + 4), "...")
            else:
                print(" " * indent, key+":", value)
    elif isinstance(dictobj, list):
        for value in dictobj:
            print()
            print_kv(value, indent)


# print_kv(toml)
print_kv(jayson)