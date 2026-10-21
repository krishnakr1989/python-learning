from pathlib import Path

log_directory = Path("days").parent.parent

for file in log_directory.glob("*.py"):
    print(file)