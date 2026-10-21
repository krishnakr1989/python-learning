from pathlib import Path   

def error_lines(filename,kk):
    with open(filename) as file:
        for line in file:
            if any(keyword in line for keyword in kk):
                yield line

path=Path(__file__).parent.parent / "response.py"
for error in error_lines(path,["error","Error","timedout"]):
    print(error)