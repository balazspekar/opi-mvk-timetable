# from lcd import LCD
from schedule import Schedule
import time


def prettify(schedule):
    result = ""
    schedule.update_remaining_seconds()
    departures = schedule.remaining_seconds

    counter = 0
    for departure in departures:
        if counter < 4:
            result += str(departure // 60) + " "
            counter += 1
        else:
            break

    if result == "":
        result = "N/A"

    return result

if __name__ == '__main__':
    # screen = LCD()
    schedule_downtown = Schedule("514")
    schedule_suburb = Schedule("513")

    while True:

        print("Belváros felé:")
        print(prettify(schedule_downtown))
        time.sleep(3)
        print("Diósgyőr felé:")
        print(prettify(schedule_suburb))
        time.sleep(3)