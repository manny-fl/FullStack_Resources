class Employee:
    def __init__(self, empID):
        self.empID = empID

    def getEmpID(self):
        return self.empID
    
    def setEmpID(self, empID):
        self.empID = empID

class Group:
    def __init__(self, *persons):
        self.persons = list(persons)
        
    def printPeopleInGroup(self):
        for person in self.persons:
            print(person)

    def __add__(self, person):
        self.persons.append(person)
        return self

    def __str__(self):
        allPeople = ''
        for person in self.persons:
            allPeople += str(person) + '\n'
        return allPeople

class Classroom(Group):

    numberOfClassrooms = 0

    def __init__(self, *persons):
        Group.__init__(self, *persons)
        self.roomNumber = 100 + self.numberOfClassrooms
        self.numberOfClassrooms += 1 

    def getRoomNumber(self):
        return self.roomNumber
    
    def setRoomNumber(self, roomNumber):
        self.roomNumber = roomNumber

class Person:
    def __init__(self, firstName='none', lastName='none'):
        self.firstName = firstName
        self.lastName = lastName
    
    def setFirstName(self, firstName):
        self.firstName = firstName
    
    def setLastName(self, lastName):
        self.lastName = lastName

    def getFirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName
    
    # Override a special method __str__
    def __str__(self):
        return '{} {}'.format(self.firstName, self.lastName)

    def __add__(self, other):
        return Group(self, other)

class Student(Person):
    def __init__(self, firstName, lastName, studentID):
        Person.__init__(self, firstName=firstName, lastName=lastName)
        self.studentID = studentID
    
    def getStudentID(self):
        return self.studentID
    
    def setStudentID(self, studentID):
        self.studentID = studentID

    def __str__(self):
        return '{} {}'.format(self.studentID, Person.__str__(self))
    
    def __add__(self, other):
        return Classroom(self, other)

class Professor(Person, Employee):
    def __init__(self, firstName, lastName, department, empID):
        Person.__init__(self, firstName=firstName, lastName=lastName)
        Employee.__init__(self, empID)
        self.department = department

    def getDepartment(self):
        return self.department
    
    def setDepartment(self, department):
        self.department = department

    def __str__(self):
        return '{} {}'.format(self.empID, Person.__str__(self))

    def __add__(self, other):
        return Classroom(self, other)


professor = Professor("Sohair", "Zaki", "Business", "E101")
student1 = Student("Eugene", "Mondkar", "S101")
student2 = Student("Oscar", "Ho", "S102")
student3 = Student("Sandy", "Sun", "S103")

pythonClass = professor + student1 + student2 + student3

listOfPeople = [professor , student1 , student2 , student3]

for person in listOfPeople:
    print('{} {}'.format(person.getFirstName(), person.getLastName()))

# print(pythonClass)
# print(type(pythonClass))