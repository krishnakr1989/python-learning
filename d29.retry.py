def retry_operation(operation, attempts=3):
    ...

# RETURN:

# Attempt 1 → FAILED
# Attempt 2 → FAILED
# Attempt 3 → SUCCESS
#
# Use exponential backoff.