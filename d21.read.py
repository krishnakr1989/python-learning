import json

with open("d21.info.json", "r") as f:
    data = json.load(f)

for key, value in data.items():
    label=key.title()
    print(f"{label} : {value}")