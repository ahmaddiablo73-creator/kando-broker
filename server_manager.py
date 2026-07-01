import psutil
def monitor_system():
    return psutil.cpu_percent(), psutil.virtual_memory().percent
