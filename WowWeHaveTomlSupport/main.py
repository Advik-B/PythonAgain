import tomllib

# With tomllib, you WILL HAVE TO USE Read-Binary mode
with open("sometoml.toml", "rb") as f:
    toml = tomllib.load(f)

print(toml)