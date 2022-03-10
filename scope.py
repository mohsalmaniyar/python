def number():
  x = 250
  def newnumber():
    print(x)
  newnumber()
number()


x = 275
def oddnumber():
  x = 233
  print(x)
oddnumber()
print(x)


x = 500
def number():
  global x
  x = 300
number()
print(x)
