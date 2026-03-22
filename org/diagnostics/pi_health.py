"""Pi health diagnostics — temperature, voltage, throttling."""
import subprocess
from dataclasses import dataclass

@dataclass
class PiHealth:
    node: str
    temp_c: float
    voltage: float
    throttled: bool
    clock_mhz: int
    memory_mb: int

def read_local_health() -> dict:
    """Read health metrics from local Pi."""
    try:
        temp = float(open("/sys/class/thermal/thermal_zone0/temp").read()) / 1000
    except Exception:
        temp = 0.0
    try:
        throttled = subprocess.check_output(["vcgencmd", "get_throttled"]).decode().strip()
    except Exception:
        throttled = "unknown"
    return {
        "temperature_c": round(temp, 1),
        "throttled": throttled,
    }
