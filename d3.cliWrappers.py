import subprocess
from shlex import quote

def run_cmd(cmd, *args, capture_output=False, check=True, timeout=None, **flags):
    """
    cmd: base command (e.g. "kubectl")
    *args: extra positional args (e.g. "get", "pods")
    **flags: keyword flags will be converted to CLI options:
        namespace="default"  -> --namespace default
        output="json"        -> --output json
        all=True             -> --all
        dry_run=False        -> (omitted)
    """
    parts = [cmd]
    parts.extend(map(str, args))

    for k, v in flags.items():
        flag = f"--{k.replace('_', '-')}"
        if isinstance(v, bool):
            if v:
                parts.append(flag)
        elif v is None:
            parts.append(flag)
        else:
            parts.extend([flag, str(v)])

    # For logging / debugging
    print("Running:", " ".join(quote(p) for p in parts))

    return subprocess.run(parts, capture_output=capture_output, check=check, timeout=timeout)

if __name__ == "__main__":
    # build args/flags dynamically
    extra_args = ("get", "pods")
    extra_flags = {"namespace": "default", "output": "json", "all": False}

    # unpack with * and **
    run_cmd("kubectl", *extra_args, **extra_flags)