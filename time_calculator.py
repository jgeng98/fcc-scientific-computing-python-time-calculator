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


def format_time(time, days_passed, day_of_week):
    new_day = add_days(day_of_week, days_passed)

    if days_passed == 0:
        return "{time}, {new_day}".format(time=time, new_day=new_day.capitalize())
    elif days_passed == 1:
        return "{time}, {new_day} (next day)".format(
            time=time, new_day=new_day.capitalize()
        )
    else:
        return "{time}, {new_day} ({days_passed} days later)".format(
            time=time, new_day=new_day.capitalize(), days_passed=days_passed
        )


def add_time(start, duration, start_date=None):
    current_hour, current_mins = convert_to_24_hour_clock(start).split(":")
    hours_to_add, mins_to_add = duration.split(":")

    extra_hour, new_mins = divmod(int(current_mins) + int(mins_to_add), 60)

    days_passed, new_hour = divmod(
        int(current_hour) + int(hours_to_add) + extra_hour, 24
    )

    if new_mins < 10:
        new_mins = "0" + str(new_mins)

    new_time = convert_from_24_hour_clock(str(new_hour) + ":" + str(new_mins))

    if start_date == None:
        if days_passed == 0:
            return new_time
        elif days_passed == 1:
            return "{time} (next day)".format(time=new_time)
        else:
            return "{time} ({days} days later)".format(time=new_time, days=days_passed)
    else:
        return format_time(new_time, days_passed, start_date)
