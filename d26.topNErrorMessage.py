import re
from collections import Counter

log_file = "d26.log.log"
top_n = 3

pattern = re.compile(r"ERROR\s+\S+\s+-\s+(?P<message>.+)")

error_messages = Counter()

with open(log_file, "r") as f:
    for line in f:
        match = pattern.search(line)
        if match:
            message = match.group("message").strip()
            error_messages[message] += 1

print(f"Top {top_n} error messages:")
for message, count in error_messages.most_common(top_n):
    print(f"{message} -> {count}")