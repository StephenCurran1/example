class example:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, age, occupation, salary):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.salary = salary
        example.empCount += 1

    def displayCount(self):
        print("Total people %d" % example.empCount)

    def displayExample(self):
        print("Name : ", self.name,  ", age: ", self.age, ", occupation: ", self.occupation, ", Salary", self.salary)

name = input('Enter your name: ')
age = input('Enter your age: ')
occupation = input('Enter your occupation: ')
salary = input('Enter your salary: ')
examp = example(name, age, occupation, salary)
examp.displayExample()
examp.displayCount()

