import yaml

with open("d20.env.yaml", "r") as f:
    data = yaml.safe_load(f)

for item in data:
    for key, value in item.items():
        print(key, "=", value)