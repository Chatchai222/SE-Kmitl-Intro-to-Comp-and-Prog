import math
import time


class Clock(object):
    def __init__(self, hh=0, mm=0, ss=0):
        self.hh = hh
        self.mm = mm
        self.ss = ss

    def tick(self):
        self.ss += 1
        if self.ss > 59:
            self.ss = 0
            self.mm += 1
        if self.mm > 59:
            self.mm = 0
            self.hh += 1
        if self.hh > 23:
            self.hh = 0

    def run(self):
        while True:
            self.tick()
            time.sleep(1)
            output = "%02d:%02d:%02d" % (self.hh, self.mm, self.ss)
            print(output)


class AlarmClock(Clock):
    def __init__(self, hh, mm, ss, alarm_hh, alarm_mm, alarm_ss, alarm_on_off):
        super().__init__(hh, mm, ss)
        self.alarm_hh = alarm_hh
        self.alarm_mm = alarm_mm
        self.alarm_ss = alarm_ss
        self.alarm_on_off = alarm_on_off

    def timeSameAsAlarmTime(self):
        if (self.alarm_hh == self.hh) and (self.alarm_mm == self.mm) and (self.alarm_ss == self.ss):
            return True
        else:
            return False

    def setAlarmTime(self, h, m, s):
        self.alarm_hh = h
        self.alarm_mm = m
        self.alarm_ss = s

    def alarm_on(self):
        self.alarm_on_off = "On"

    def alarm_off(self):
        self.alarm_on_off = "Off"

    def run(self):
        while True:
            self.tick()
            if self.timeSameAsAlarmTime() and (self.alarm_on_off == "On"):
                print("BEEP! BEEP!")
                break
            print("%02d:%02d:%02d" % (self.hh, self.mm, self.ss))

me = AlarmClock(5, 59, 56, 6, 0, 0, "On")
me.run()