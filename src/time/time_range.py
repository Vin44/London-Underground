from datetime import datetime

def get_value_by_time():
    now = datetime.now().time()

    am_peak_start = datetime.strptime("07:00", "%H:%M").time()
    am_peak_end = datetime.strptime("09:00", "%H:%M").time()

    inter_peak_start = datetime.strptime("09:30", "%H:%M").time()
    inter_peak_end = datetime.strptime("15:30", "%H:%M").time()

    if am_peak_start <= now <= am_peak_end:
        return 1
    elif inter_peak_start <= now <= inter_peak_end: 
        return 2
    else:
        return 3
    
