from abc import ABC, abstractmethod

class StationeryGood(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def findCost(self):
        pass

class Magazine(StationeryGood):
    def __init__(self, name, price):
        super().__init__(name)
        self.price = price

    def findCost(self):
        return self.price

class Book(StationeryGood):
    def __init__(self, name, price):
        super().__init__(name)
        self.price = price

    def findCost(self):
        return self.price * 0.9

class Ribbon(StationeryGood):
    def __init__(self, name, length):
        super().__init__(name)
        self.length = length

    def findCost(self):
        return (self.length * 5)

def getTotalCost(basket):
    output = 0
    for each_good in basket:
        output += each_good.findCost()
    return output

mybasket = [Magazine("Computer World", 70),Magazine("Computer World", 70),Magazine("Computer World", 70),
            Book("Windows 7 for Beginners", 200),Book("Windows 7 for Beginners", 200),Ribbon("Blue ribbon", 10)]

print(getTotalCost(mybasket))