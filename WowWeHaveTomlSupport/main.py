import tomllib
import sys

sys.setrecursionlimit(10000)

# With tomllib, you WILL HAVE TO USE Read-Binary mode
with open("sometoml.toml", "rb") as f:
    toml = tomllib.load(f)

def print_kv(dictobj: dict, indent: int = 0):
    for key, value in dictobj.items():
        if isinstance(value, dict):
            print(" " * indent, key+":")
            try:
                print_kv(value, indent + 4)
            except RecursionError:
                print(" " * (indent + 4), "...")
        else:
            print(" " * indent, key+":", value)


print_kv(toml)