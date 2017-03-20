from lcd import LCD
from schedule import Schedule
import time
import datetime


def prettify(schedule, destination):
    result = destination + ":"
    schedule.update_remaining_seconds()
    departures = schedule.remaining_seconds
    counter = 0
    for departure in departures:
        print(departure)
        if counter < 5:
            in_minute = departure // 60
            if in_minute < 10 and in_minute >= 0:
                    result += "0"
            result += str(in_minute) + " "
            counter += 1
        else:
            break

    if result == "":
        result = "N/A"

    return result


def add_zero(digit):
    stringified = str(digit)
    if len(stringified) > 1:
        return digit
    else:
        return "0" + stringified


if __name__ == '__main__':
    screen = LCD()
    schedule_downtown = Schedule("514")
    schedule_suburb = Schedule("513")
    requests = 0
    try:
        while True:
            prettified_1 = prettify(schedule_downtown, "B")
            prettified_2 = prettify(schedule_suburb, "D")
            requests += 1
            screen.lcd_string(prettified_1, 1)
            screen.lcd_string(prettified_2, 2)
            time.sleep(5)
            current_dt = datetime.datetime.now()
            screen.lcd_string(str(current_dt.year) + "/" + add_zero(current_dt.month) + "/" + add_zero(current_dt.day), 1)
            screen.lcd_string(add_zero(current_dt.hour) + ":" + add_zero(current_dt.minute) + " [" + str(requests) + "]", 2)
            time.sleep(2)
    finally:
        screen.lcd_string("Exited", 1)
        screen.lcd_string("", 2)
