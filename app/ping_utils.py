import subprocess

def ping_host(host: str, timeout_seconds: int = 1) -> bool:
    try:
        completed = subprocess.run(
            ["ping", "-c", "1", "-W", str(timeout_seconds), host],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        return completed.returncode == 0
    except Exception:
        return False
