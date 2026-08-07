import os


def shutdown():
    os.system("shutdown /s /t 5")
    return "PC will shut down in 5 seconds."


def restart():
    os.system("shutdown /r /t 5")
    return "PC will restart in 5 seconds."


def lock():
    os.system("rundll32.exe user32.dll,LockWorkStation")
    return "PC locked."


def cancel_shutdown():
    os.system("shutdown /a")
    return "Shutdown cancelled."