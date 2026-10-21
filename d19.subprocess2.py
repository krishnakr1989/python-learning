import subprocess

def run_command(command):
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode != 0:
            print("Non-zero return code:", result.returncode)
            print("stderr:", result.stderr)
            return

        print("stdout:", result.stdout)

    except FileNotFoundError:
        print("Command not found:", command[0])

    except subprocess.TimeoutExpired:
        print("Command timed out")

run_command(["git", "version1"])