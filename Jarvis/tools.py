import datetime
import os
import webbrowser
import psutil

def get_system_status() -> str:
    """Returns live hardware metrics including CPU utilization, RAM usage, and battery state."""
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    battery = psutil.sensors_battery()
    
    battery_status = "No battery detected (Desktop)"
    if battery:
        plugged = "Plugged in" if battery.power_plugged else "Discharging"
        battery_status = f"{battery.percent}% ({plugged})"
        
    return (
        f"System Metrics -> CPU Usage: {cpu_usage}%, "
        f"RAM Usage: {ram_usage}%, "
        f"Battery: {battery_status}."
    )

def open_website(url: str) -> str:
    """Opens any specified website URL in the default web browser.

    Args:
        url: Web address to open (e.g., 'youtube.com', 'https://github.com').
    """
    if not url.startswith("http"):
        url = f"https://{url}"
    webbrowser.open(url)
    return f"Successfully opened {url} in your default browser."

def launch_app(app_name: str) -> str:
    """Launches a Windows desktop application.

    Args:
        app_name: Command name of the application (e.g., 'notepad', 'calc', 'cmd', 'mspaint').
    """
    try:
        os.system(f"start {app_name}")
        return f"Successfully launched application: {app_name}."
    except Exception as e:
        return f"Failed to launch application {app_name}: {str(e)}"

def get_current_time() -> str:
    """Returns the current system date and time."""
    now = datetime.datetime.now()
    return f"The current time is {now.strftime('%I:%M %p')} on {now.strftime('%A, %B %d, %Y')}."

AVAILABLE_TOOLS = [get_system_status, open_website, launch_app, get_current_time]