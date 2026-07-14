


import config

def is_external(ip: str) -> bool:
    return not ip.startswith(config.INTERNAL_IP_PREFIXES)

def is_sensitive_port(port:str) -> bool:
    return port in config.SENSITIVE_PORTS

def is_large_data(size: str) -> bool:
    return int(size) >= config.MAX_NORMAL_SIZE

def is_abnormal_hour(timestamp: str) -> bool:
    time_part = timestamp.split(" ")[1]
    hour = int(time_part.split(":")[0])
    return hour < config.START_WORK_HOUR or hour > config.END_WORK_HOUR









