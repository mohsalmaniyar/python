'''class Student:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
x = Student("Salman", "Maniyar")
x.printname()


class Student:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student1(Student):
  pass
x = Student("Yasir", "Maniyar")
x.printname()


class Student:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student1(Student):
  def __init__(self, fname, lname):
    Student.__init__(self, fname, lname)
x = Student1("Sultan", "Maniyar")
x.printname()


class Student:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student1(Student):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
x = Student1("Riyaz", "Maniyar")
x.printname()


class Student:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student1(Student):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2000
x = Student1("Ashfaq", "Maniyar")
print(x.graduationyear)'''




