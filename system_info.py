import os
import platform
import shutil
import socket
import psutil
from datetime import datetime


def get_system_status():

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    battery = psutil.sensors_battery()

    if battery:
        battery_percent = f"{battery.percent}%"
    else:
        battery_percent = "Not Available"

    time_now = datetime.now().strftime("%I:%M %p")

    return (
        f"\n"
        f"💻 CPU Usage : {cpu}%\n"
        f"🧠 RAM Usage : {ram}%\n"
        f"🔋 Battery : {battery_percent}\n"
        f"🕒 Time : {time_now}\n"
    )


def health_check():

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent

    total, used, free = shutil.disk_usage("/")
    free_gb = round(free / (1024 ** 3), 2)

    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        internet = "Connected"
    except:
        internet = "Disconnected"

    return (
        f"\n"
        f"🤖 AJA HEALTH REPORT\n\n"
        f"💻 CPU Usage : {cpu}%\n"
        f"🧠 RAM Usage : {ram}%\n"
        f"💾 Free Disk : {free_gb} GB\n"
        f"🌐 Internet : {internet}\n"
    )


def get_system_info():

    system = platform.system()
    release = platform.release()
    version = platform.version()
    machine = platform.machine()
    processor = platform.processor()
    python_version = platform.python_version()
    hostname = socket.gethostname()

    try:
        username = os.getlogin()
    except Exception:
        username = "Unknown"

    total_ram = round(psutil.virtual_memory().total / (1024 ** 3), 2)

    total_disk, used_disk, free_disk = shutil.disk_usage("/")
    total_disk = round(total_disk / (1024 ** 3), 2)
    free_disk = round(free_disk / (1024 ** 3), 2)

    return f"""
==============================
🤖 AJA SYSTEM INFORMATION
==============================

💻 Computer Name : {hostname}
👤 User          : {username}

🖥 Operating System : {system} {release}
📦 Version          : {version}

⚙ Processor      : {processor}
🧩 Architecture   : {machine}

🧠 Total RAM      : {total_ram} GB
💾 Total Disk     : {total_disk} GB
📂 Free Disk      : {free_disk} GB

🐍 Python Version : {python_version}

==============================
"""