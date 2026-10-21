def analyze_log(file_path):
    error_count = 0
    warning_count = 0
    timeout_count = 0
    http_500_count = 0

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if "ERROR" in line:
                error_count += 1
            elif "WARN" in line:
                warning_count += 1
            elif "TIMEOUT" in line:
                timeout_count += 1
            elif "HTTP 500" in line:
                http_500_count += 1

    print(f"ERROR       : {error_count}")
    print(f"WARN      : {warning_count}")
    print(f"TIMEOUT     : {timeout_count}")
    print(f"HTTP 500    : {http_500_count}")


analyze_log("d25.application.log")


# RETURN:
# ERROR       : 120
# WARN        : 430
# TIMEOUT     : 31
# HTTP 500    : 14