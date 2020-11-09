# Question 4
import math

class QuadraticEquation:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def getDiscriminant(self):
        return (self.__b ** 2) - (4 * self.__a * self.__c)

    def getRoot1(self):
        if self.getDiscriminant() < 0:
            return 0
        else:
            return (-self.__b + math.sqrt(self.getDiscriminant())) / (2 * self.__a)

    def getRoot2(self):
        if self.getDiscriminant() < 0:
            return 0
        else:
            return (-self.__b - math.sqrt(self.getDiscriminant())) / (2 * self.__a)


my_quad = QuadraticEquation(1, -7, 10)
print(my_quad.get_a())
print(my_quad.get_b())
print(my_quad.get_c())
print(my_quad.getDiscriminant())
print(my_quad.getRoot1())
print(my_quad.getRoot2())
