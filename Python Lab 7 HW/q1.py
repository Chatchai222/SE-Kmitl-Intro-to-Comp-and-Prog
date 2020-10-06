class Clock:
    def __init__(self, hour, minute, second):
        hour = int(hour)
        minute = int(minute)
        second = int(second)
        if hour >= 24 or hour < 0:
            hour = 23
        if minute >= 60 or minute < 0:
            minute = 59
        if second >= 60 or second < 0:
            second = 59
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def set_time(self, hour, minute, second):
        hour = int(hour)
        minute = int(minute)
        second = int(second)

        if hour >= 24 or hour < 0:
            hour = 23
        if minute >= 60 or minute < 0:
            minute = 59
        if second >= 60 or second < 0:
            second = 59
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def get_time(self):
        return [self.__hour, self.__minute, self.__second]

    def tick(self):
        self.__second += 1
        if self.__second // 60 > 0:
            self.__second %= 60
            self.__minute += 1
        if self.__minute // 60 > 0:
            self.__minute %= 60
            self.__hour += 1
        if self.__hour // 24 > 0:
            self.__hour = 0

    def display_time(self):
        output = ":" + "{:02d}".format(self.__minute) + ":" + "{:02d}".format(self.__second)
        if self.__hour <= 12:
            output = "{:02d}".format(self.__hour) + output + " AM"
        else:
            output = "{:02d}".format(self.__hour - 12) + output + " PM"
        return output


