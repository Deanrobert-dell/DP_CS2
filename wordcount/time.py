

def record_time(doc_id, duration):
    """record timestamp when doc is updated"""
    # implement time recording logic here
    return True
    
# ...existing code...
from datetime import datetime

def record_time(doc_id, duration):
    """record timestamp when doc is updated"""
    current = get_current_time()
    # implement time recording logic here (e.g., write to a log or DB)
    print(f"Recording time for doc {doc_id}: {current} (duration: {duration})")
    return True

def get_current_time():
    """Return the current time as an ISO-formatted string (seconds precision)."""
    return datetime.now().isoformat(timespec='seconds')

def print_current_time():
    """Print the current time to stdout."""
    print(get_current_time())
# ...existing code...