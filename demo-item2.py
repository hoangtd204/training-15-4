
import json
from datetime import datetime

def log_event(event_name, *args, **kwargs):
    getlog = {
        "timestamp": datetime.now().isoformat(),
        "event": event_name,
        "args": args,
        "details": kwargs
    }
    return getlog

def save_user_to_file(filename, log):
    with open(filename, 'w') as f:
        json.dump(log, f, indent=4)

def main():
    filename = 'logevent.json'
    log = log_event("user_login", "UserID: 123", ip="192.168.1.5", success=True)
    save_user_to_file(filename, log)

main()
