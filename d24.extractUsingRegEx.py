import re

pattern = re.compile(
    r'^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) '
    r'(?P<level>[A-Z]+) '
    r'(?P<application>\S+) '
    r'transaction=(?P<transaction_id>\d+)'
)

with open("d24.data.log", "r") as f:
    for line in f:
        line = line.strip()
        match = pattern.match(line)
        if match:
            d = match.groupdict()
            print(f"timestamp: {d['timestamp']}")
            print(f"level: {d['level']}")
            print(f"application: {d['application']}")
            print(f"transaction ID: {d['transaction_id']}")