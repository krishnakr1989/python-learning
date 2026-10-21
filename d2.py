from copy import copy, deepcopy

deployment = {
    "application": "payment",
    "replicas": 3,
    "environment": "prod"
}

def scale_application(config, replicas):
    config = deepcopy(config)
    config["replicas"] = replicas
    return config

updated = scale_application(deployment, 5)
print(f"Original replicas : {deployment['replicas']}")
print(f"New replicas      : {updated['replicas']}")

print("Original deployment:", deployment)
print("Updated deployment:", updated)