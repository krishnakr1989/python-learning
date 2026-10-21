production_servers = [
    "web01",
    "web02",
    "web03"
]

#backup_servers = production_servers

#backup_servers = production_servers.copy()
backup_servers = production_servers[:]
backup_servers.append("web04")

print("Production:", production_servers)
print("Backup:", backup_servers)