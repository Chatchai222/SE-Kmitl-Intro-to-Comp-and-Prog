# Question 1
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print(self):
        new_hour = "{:02d}".format(self.hour)
        new_minute = "{:02d}".format(self.minute)
        new_second = "{:02d}".format(self.second)

        print(new_hour + ":" + new_minute + ":" + new_second + " Hrs.")


time1 = Time(9, 30, 0)
time1.print()


