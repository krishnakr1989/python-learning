import yaml

with open("d22.data.yaml", "r") as f:
    data = yaml.safe_load(f)

required_fields = ["application", "environment", "replicas", "image"]
for field in required_fields:
    if field not in data:
        raise ValueError(f"Missing required field: {field}")

if not data["application"]:
    raise ValueError("application must exist")

if not data["image"]:
    raise ValueError("image must exist")

if data["replicas"] <= 0:
    raise ValueError("replicas must be greater than 0")

valid_environments = {"dev", "qa", "prod", "staging"}
if data["environment"] not in valid_environments:
    raise ValueError(f"environment must be one of {sorted(valid_environments)}")

print(data)
print(type(data))
print(data["application"])
print(data["replicas"])