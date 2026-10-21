class Server:

    def __init__(self, name, ip):
        self.name = name
        self.ip = ip

    def health_check(self):
        print(f"Checking {self.name}")

server = Server(
    "web01",
    "10.0.0.10"
)

server.health_check()