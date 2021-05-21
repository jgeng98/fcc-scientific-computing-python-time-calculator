def add_days(day_of_week, days):
    weekdays = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]

    return weekdays[(weekdays.index(day_of_week.lower()) + days) % 7]


def convert_to_24_hour_clock(time):
    time, period = time.split()
    hour, minute = time.split(":")

    if period == "AM" and hour != "12":
        return time
    elif period == "AM" and hour == "12":
        return "00" + ":" + minute
    elif period == "PM" and hour == "12":
        return time
    else:
        return str(int(hour) + 12) + ":" + minute


def convert_from_24_hour_clock(time):
    hour, minute = time.split(":")

    if int(hour) == 0:
        return "12:" + minute + " AM"
    elif int(hour) <= 11:
        return time + " AM"
    elif int(hour) == 12:
        return time + " PM"
    else:
        return str(int(hour) - 12) + ":" + minute + " PM"


def add_time(start, duration, start_date=None):
    time, period = start.split()
    days = 0

    current_hour, current_mins = time.split(":")

    hours_to_add, mins_to_add = duration.split(":")

    extra_hour, new_mins = divmod(int(current_mins) + int(mins_to_add), 60)

    period_changes, new_hour = divmod(
        int(current_hour) + int(hours_to_add) + extra_hour, 12
    )

    if period == "PM" and (period_changes % 2) == 1:
        days += 1 + period_changes // 2
    else:
        days += period_changes // 2

    if (period_changes % 2) != 0:
        period = "PM" if period == "AM" else "AM"

    print(new_hour, new_mins, period)

    print(period_changes, days)

    new_time = ""

    return new_time


if __name__ == "__main__":
    print(add_time("12:00 PM", "12:00"))
