import os
import platform

def get_system_info():
    info = {
        "OS Name": os.name,
        "Platform": platform.system(),
        "Platform Release": platform.release(),
        "Platform Version": platform.version(),
        "Architecture": platform.machine(),
        "Processor": platform.processor(),
        "Python Version": platform.python_version()
    }
    return info

def print_system_info(info):
    for key, value in info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    system_info = get_system_info()
    print_system_info(system_info)