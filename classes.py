class A:
  x = 5
print(A)



class P:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = P("Salman", 26)
print(p1.name)
print(p1.age)



class p:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = p("Sultan", 27)
p1.myfunc()


class Name:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Name("Riyaz", 36)
p1.age = 48
print(p1.age)


class Name:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Name("Salman", 26)
del p1.age
print(p1.age)
