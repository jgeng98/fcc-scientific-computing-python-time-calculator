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
