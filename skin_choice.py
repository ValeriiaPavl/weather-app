from datetime import time


def choose_time_skin(local_datetime: str):
    local_time = local_datetime.split(' ')[1]
    time_hours, time_minutes = [int(n) for n in local_time.split(':')]
    local_time_for_comparing = time(time_hours, time_minutes)

    start_day = time(hour=10, minute=0)
    end_day = time(hour=18, minute=0)
    start_night = time(hour=22, minute=0)
    end_night = time(hour=6, minute=0)

    if start_day < local_time_for_comparing < end_day:
        return "card day"
    if local_time_for_comparing > start_night or local_time_for_comparing < end_night:
        return "card night"
    else:
        return "card dusk"
