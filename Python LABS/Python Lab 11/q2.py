import math

class Calculator(object):
    def __init__(self, acc):
        self.acc = acc

    def set_accumulator(self,a):
        self.acc = a

    def get_accumulator(self):
        return self.acc

    def add(self, x):
        self.acc += x

    def subtract(self, x):
        self.acc -= x

    def multiply(self, x):
        self.acc *= x

    def divide(self, x):
        if x == 0:
            print("Error cannot divide by zero")
            return
        self.acc /= x

    def print_results(self):
        print(f"Result:{self.acc}")

class Sci_calc(Calculator):
    def __init__(self, acc=0.00):
        super().__init__(acc)

    def square(self):
        self.acc = self.acc ** 2

    def exp(self, x):
        self.acc = self.acc ** x

    def factorial(self):
        if self.acc < 0:
            print("Error cannot factorial a negative num")
            return
        if isinstance(self.acc, float):
            print("Error cannot factorial a decimal")
            return
        self.acc = math.factorial(self.acc)

    def print_results(self):
        print("{:e}".format(self.acc))

me = Sci_calc(1.1)
me.factorial()
me.print_results()