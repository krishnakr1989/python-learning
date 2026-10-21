servers = [
    {"name": "web01", "cpu": 45, "memory": 16},
    {"name": "web02", "cpu": 91, "memory": 32},
    {"name": "web03", "cpu": 76, "memory": 16},
    {"name": "web04", "cpu": 88, "memory": 38}
]

# def cpuGT80(servers):
#     Filtered_server=[]
#     for server in servers:
#         if server["cpu"] >80:
#             Filtered_server.append(server["name"])
#     return Filtered_server
# filtered_servers = cpuGT80(servers)
# print(filtered_servers)


# cpuGT80 = lambda servers: [server["name"] for server in servers if server["cpu"] > 80]
# filtered_servers = cpuGT80(servers)
# print(filtered_servers)


# cpuGT80 = list(
#     filter(lambda server: server["cpu"] > 80, servers)
# )
# print(cpuGT80)

# generator expression
# cpuGT80=list(
#     {"xx": server["name"],"yy": server["memory"]}
#     for server in servers if server["cpu"] > 80
# )
# print(cpuGT80)

cpuGT80=[]
for server in servers:
    if server["cpu"] > 80:
        cpuGT80.append({"xx": server["name"],"yy": server["memory"]})
print(cpuGT80)