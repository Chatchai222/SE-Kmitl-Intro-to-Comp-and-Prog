from abc import ABC, abstractmethod

class Transportation(ABC):
    def __init__(self, start_place, end_place, distance):
        self.start_place = start_place
        self.end_place = end_place
        self.distance = distance

    @abstractmethod
    def find_cost(self):
        pass

class Walk(Transportation):
    def __init__(self, start_place, end_place, distance):
        super().__init__(start_place, end_place, distance)

    def find_cost(self):
        return 0


class Taxi(Transportation):
    def __init__(self, start_place, end_place, distance):
        super().__init__(start_place, end_place, distance)

    def find_cost(self):
        return self.distance * 40


class Train(Transportation):
    def __init__(self, start_place, end_place, distance, station):
        super().__init__(start_place, end_place, distance)
        self.station = station

    def find_cost(self):
        return self.station * 5


walk1 = Walk("KMITL", "KMITL SCB Banj", 0.6)
taxi1 = Taxi("KMITL SCB Bank", "Ladkrabang Station", 5)
train1 = Train("Ladkrabang Station", "Payathai Station", 40, 6)
taxi2 = Taxi("Payathai Station", "The British Council", 3)

transport_list = [walk1, taxi1, train1, taxi2]
for each_transport in transport_list:
    print(each_transport.find_cost())