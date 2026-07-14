


import config

def is_external(ip: str) -> bool:
    return not ip.startswith(config.INTERNAL_IP_PREFIXES)

def is_sensitive_port(port:str) -> bool:
    return port in config.SENSITIVE_PORTS











