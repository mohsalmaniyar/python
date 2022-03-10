'''str = "Mohammad Salman maniyar"
it = iter(str)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))'''



'''a = "Salman"

for x in a:
  print(x)'''


'''class A:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    x = self.a
    self.a += 1
    return x
myclass = A()
iterator = iter(myclass)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))'''


'''class B:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    if self.a <= 50:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
myclass = B()
iterator = iter(myclass)
for x in iterator:
  print(x)'''



