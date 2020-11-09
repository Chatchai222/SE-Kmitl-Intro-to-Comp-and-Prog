import math

class Name(object):
    def __init__(self, title, firstName, lastName):
        self.title = title
        self.firstName = firstName
        self.lastName = lastName

    def setName(self,t,f,l):
        self.title = t
        self.firstName = f
        self.lastName = l

    def getFullName(self):
        return f"{self.title}.{self.firstName} {self.lastName}"

class Date(object):
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def setDate(self,d,m,y):
        self.day = d
        self.month = m
        self.year = y

    def getDate(self):
        return f"{self.day}/{self.month}/{self.year}"

    def getDateBC(self):
        return f"{self.day}/{self.month}/{self.year + 543}"

class Address(object):
    def __init__(self, houseNo, street, district, city, country, postcode):
        self.houseNo = houseNo
        self.street = street
        self.district = district
        self.city = city
        self.country = country
        self.postcode = postcode

    def setAddress(self, houseNo, street, district, city, country, postcode):
        self.houseNo = houseNo
        self.street = street
        self.district = district
        self.city = city
        self.country = country
        self.postcode = postcode

    def getAddress(self):
        return f"HouseNo:{self.houseNo};Street:{self.street};District:{self.district};City:{self.city};Country:{self.country};Postcode:{self.postcode}"

class Department(object):
    def __init__(self, description, manager, employeeList=[]):
        self.description = description
        self.manager = manager
        self.employeeList = employeeList

    def addEmployee(self, e):
        self.employeeList.append(e)
        e.department = self

    def deleteEmployee(self, e):
        self.employeeList.remove(e)
        e.department = None

    def setManager(self, e):
        if (isinstance(e, PermEmployee) and (e in self.employeeList)):
            self.manager = e
        else:
            print("Sorry condition not fulfilled for manager")

    def printInfo(self):
        print(f"departmentdescription:{self.description}")
        if (self.manager != None):
            self.manager.printInfo()
        for employee in self.employeeList:
            employee.printInfo()

class Person(object):
    def __init__(self, name, birthday, address):
        self.name = name
        self.birthday = birthday
        self.address = address

    def printInfo(self):
        print(self.name.getFullName())
        print(self.birthday.getDate())
        print(self.address.getAddress())

class Employee(Person):
    def __init__(self, name, birthday, address, startDate, department):
        super().__init__(name, birthday, address)
        self.startDate = startDate
        self.department = department

    def printInfo(self):
        super().printInfo()
        self.department.printInfo()
        print("Startdate:"+self.startDate.getDate())


class TempEmployee(Employee):
    def __init__(self, name, birthday, address, startDate, department, wage):
        super().__init__(name, birthday, address, startDate, department)
        self.wage = wage

    def printInfo(self):
        super().printInfo()
        print(f"Wage:{self.wage}")

class PermEmployee(Employee):
    def __init__(self, name, birthday, address, startDate, department, salary):
        super().__init__(name, birthday, address, startDate, department)
        self.salary = salary

    def printInfo(self):
        super().printInfo()
        print(f"Salary:{self.salary}")


name1 = Name("Mr", "Chatchai", "Paisalpanich")
bday1 = Date("5", "6", "2001")
address1 = Address("123", "lion", "pravet", "bangkok", "thailand", "12345")
startdate1 = Date("1", "1", "2020")
department1 = Department("UNIVERISTYKMITL", None, [])

me = TempEmployee(name1,bday1,address1,startdate1,department1, "100")
me.printInfo()

