#a = lambda a: a + 110
#print(a(105))


#x = lambda a, b: a-b
#print(x(20, 15))

#x = lambda a, b, c: a + b + c
#print(x(15, 26, 32))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(30)
mytripler = myfunc(45)

print(mydoubler(3)) 
print(mytripler(5))
