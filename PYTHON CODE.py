#                       ----------Data types[Integer]---------
x = 10
print(type(x))
#                       ----------Data types[String]---------
x = "Salman"
print(type(x))
#                       ----------Data types[Float]---------
x = 2.86
print(type(x))
#                       ----------Data types[Complex]---------
x = 1j
print(type(x))
#                       ----------Data types[List]---------
x = ["Salman", "Maniyar", "Bijapur"]
print(type(x))
#                       ----------Data types[tuple]---------
x = ("Salman", "Maniyar", "Bijapur")
print(type(x))
#                       ----------Data types[dictionary]---------
x = {"name" :"Salman", "city" :"Bijapur"}
print(type(x))
#                       ----------Data types[range]---------
x = range(6)
print(type(x))
#                       ----------Data types[set]---------
x = {"name", "Salman", "city", "Bijapur"}
print(type(x))
#                       ----------Data types[frozenset]---------
x = frozenset({"name" :"Salman", "city" :"Bijapur"})
print(type(x))
#                       ----------Data types[boolean]---------
x = True
print(type(x))
#                       ----------Data types[bytes]---------
x = b"Hello"
print(type(x))
#                       ----------Data types[bytearray]---------
x = bytearray(4)
print(type(x))
#                       ----------Data types[memoryview]---------
x = memoryview(bytes(10))
print(type(x))
#               ----------Data types[Int,Float,Complex,String]---------
x = 10
y = 8.6
z= 1j
p = "Maniyar"
print(type(x))
print(type(y))
print(type(z))
print(type(p))
#                       ----------Data types[Float]---------
x = 44e33
y = 23E5
z = -7.2e400
print(type(x))
print(type(y))
print(type(z))
#                       ----------Data types[complex]---------
x = 4-3j
y = 6j
z = -7j
print(type(x))
print(type(y))
print(type(z))
#               ----------Data types[Int,Float,Complex,String]---------
x = 2
y = 4.7
z = 1j

a = float(x)
b = int(y)
c = complex(z)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))
#               ----------Data types[Random Number]---------
import random
print(random.randrange(51, 60))
#               ----------Specify a Variable Type---------
x = int(2)
y = int(6.5)
z = int("5")
print(x)
print(y)
print(z)
#                        ----------STRING---------
a = """My name is Mohammad Salman Maniyar,
Completed M.Tech from Secab Engineering,
college Vijayapura.Now I am doing,
FullStack DEvelopment Course at Innoovatum"""
print(a)

a = "Mohammad Salman Maniyar"
print(a[5])
print(a[0])
print(a[3])
print(a[13])

for x in "Mohammad Salman Maniyar":
    print(x)

a = "Mohammad Salman Maniyar"
print(len(a))

a = "I am Completed Post Graduation From SIET Bijapur"
print("Graduation" in a)

a = "I am Completed Post Graduation From SIET Bijapur"
print("Under" in a)

a = "Mohammad Salman"
print(a[3:8])

a = "Mohammad Salman"
print(a[:8])

a = "Mohammad Salman"
print(a[9:])

a = "Mohammad Salman"
print(a[-8:-3])

a = "Mohammad Salman"
print(a.upper())

a = "Mohammad Salman"
print(a.lower())

a = "Mohammad Salman   "
print(a.strip())

a = "Bijapur"
print(a.replace("B", "V"))

a = "Mohammad Salman"
print(a.split(","))

a = "Mohammad"
b = "Salman"
c = a+b
print(c)

a = "Mohammad"
b = "Salman"
c = a + " " + b
print(c)

standard = 10
a = "My name is shafeeq, now I am in {} class"
print(a.format(standard))

quantity = 4
bookno = 567
price = 4090
myorder = "I want {} numbers of book {} for {} rupees."
print(myorder.format(quantity, bookno, price))

x = "I am Salman, I completed \"M.tech\" from S.I.E.T."
print(x)

a = "My name is Salman \n and I am from Bijapur"
print(a)

a = "good morning,"
x = a.capitalize()
print (x)


a = "python is language used for Backend"
x = a.capitalize()
print (x)

a = "Good morning guys, And today I am Giving Presentation"
x = a.casefold()
print (x)

a = "python is language used for Backend"
x = a.center(100)
print(x)

a = "I am doing python course,python language used for Backend, python is very easy language for biginers to learn"
x = a.count("python")
print(x)

a = "python is language used for Backend."
x = a.endswith(".")
print(x)

a = "python is language used for Backend."
x = a.find("used")
print(x)

p = "My name is {fname}, I'm from {city}".format(fname = "Yasir", city = "Bijapur")
q = "My name is {0}, I'm from {1}".format("Salman","Bagalkot")
r = "My name is {}, I'm from {}".format("Sultan","Bangalore")
print(p)
print(q)
print(r)

a = "Salman333"
x = a.isalnum()
print(x)

a = "SalmanManiyar"
x = a.isalpha()
print(x)

a = "123456"
x = a.isdigit()
print(x)

a = ("Salman", "Yasir", "Suhaib")
x = "#".join(a)
print(x)

a = "banana"
b = "Mango"
c = "Orange"
x = a.ljust(20)
y = b.ljust(20)
z = c.ljust(20)
print(x, "is my favorite fruit.")
print(y, "is his favorite fruit.")
print(z, "is her favorite fruit.")


a = "Hello Kaleem!"
y = a.maketrans("K", "S")
print(a.translate(y))

a = "I can talk all Indian Languages Fluently"
x = a.partition("Indian Languages")
print(x)


a = "I can talk all Indian Languages Fluently"
x = a.swapcase()
print(x)


a = "My favourite city is mysore"
x = a.title()
print(x)



#               ----------BOOLEAN VALUES---------
print(54 < 68)
print(13 == 12)
print(23 > 9)

a = 20
b = 40

if b > a:
    print("b is greater than a")
else:
    print("b is not grater than a")


x = "Salman Maniyar"
y = 26
print(bool(x))
print(bool(y))


print(bool("Salman"))
print(bool(["brick", "cement", "sand"]))
print(bool(2004))


def myFunction():
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")



#                      ----------OPERATORS---------
a = 20
b = 32
print(a+b)


a = 40
b = 32
print(a-b)

a = 3
b = 8
print(a*b)

a = 12
b = 3
print(a/b)

a = 15
b = 4
print(a%b)

a = 15
b = 4
print(a**b)

a = 20
b = 6
print(a//b)

a = 15
print(a)

a += 15
print(a)

a = 15
a -= 3
print(a)

a = 15
a *= 3
print(a)

a = 40
a /= 4
print(a)

a = 18
a %= 4
print(a)

a = 15
a //= 3
print(a)

a = 15
a **= 3
print(a)

a = 15
a &= 3
print(a)

x = 15
x |= 3
print(x)

x = 5
x ^= 3
print(x)

x = 15
x >>= 3
print(x)

x = 15
x <<= 3
print(x)

a = 15
b = 3
print(a==b)

a = 15
b = 3
print(a!=b)

a = 20
b = 15
print(a>b)

a = 15
b = 3
print(a<b)

a = 15
b = 3
print(a>=b)

a = 15
b = 3
print(a<=b)

x = 10
print(x>5 and x<12)

x = 10
print(x>5 or x<8)

x = 15
print(not(x>12 and x<20))

a = ["Salman","Maniyar"]
b = ["Salman","Maniyar"]
c = b
print(a is b)
print(b is c)
print(a == b)


a = ["Salman", "Yasir"]
print("adnan" not in a)



#           ----------------------------LIST------------------------



a = ["Salman", "Aadil", "Maniyar"]
print(a)

#Duplicates Allowed
x = ["Bagalkot", "Bijapur", "Bangalore", "Belgaum", "Bagalkot"]
print(x)

#Length of LIST
a = ["1BHK", "2BHK", "3BHK", "4BHK", "5BHK"]
print(len(a))

#LIST Items: Data Types
a = ["HTML", "CSS", "JavaScript"]
b = [10.1, 2.4, 4.6, 9.8, 12]
c = [True, False, True]
print(a)
print(b)
print(c)

#All in one list
a = ["Salman", 26, True, 20, "male"]
print(a)

#Type() 
x = ["Salman", "Maniyar", "Bijapur"]
print(type(x))

#List() Constructor
a = list(("Salman", "Maniyar", "Bijapur"))
print(a)

#Access Items
a = ["orange", "banana", "grapes", "Mango"]
print(a[3])

#Negative Indexing
a = ["orange", "banana", "grapes", "Mango"]
print(a[-2])

#Range of Indexes
a = ["Salman", "Sultan", "Yasir", "Imtiyaz", "Niyaz", "Shakeel", "Suhaib"]
print(a[1:4])

a = ["Salman", "Sultan", "Yasir", "Imtiyaz", "Niyaz", "Shakeel", "Suhaib"]
print(a[:3])

a = ["Salman", "Sultan", "Yasir", "Imtiyaz", "Niyaz", "Shakeel", "Suhaib"]
print(a[3:])

#Range of Negative Indexes
a = ["Salman", "Sultan", "Yasir", "Imtiyaz", "Niyaz", "Shakeel", "Suhaib"]
print(a[-3:-1])

#Existence of item
x = ["Niyaz", "Shakeel", "Suhaib"]
if "Shakeel" in x:
  print("Yes, 'Shakeel' is in the names list")

#Change Item Value
a = ["orange", "banana", "grapes", "Mango"]
a[2] = "Watermelon"
print(a)

a = ["orange", "banana", "grapes", "Mango"]
a[1:3] = ["Watermelon","guava"]
print(a)

#Insert Item
a = ["orange", "banana", "grapes", "Mango"]
a.insert(3,"oneruit")
print(a)

#Append Items
a = ["Niyaz", "Shakeel", "Suhaib"]
a.append("Faisal")
print(a)

#Extend List
a = ["Niyaz", "Shakeel", "Suhaib"]
b = ["Salman", "Sultan", "Yasir"]
a.extend(b)
print(a)

#Remove Specified Item
a = ["Niyaz", "Shakeel", "Suhaib"]
a.remove("Niyaz")
print(a)

#Remove Specified Index
a = ["Niyaz", "Shakeel", "Suhaib"]
a.pop(2)
print(a)

#Delete item
a = ["Niyaz", "Shakeel", "Suhaib"]
del a[0]
print(a)

#Clear list
a = ["Niyaz", "Shakeel", "Suhaib"]
a.clear()
print(a)

#for loop
b = ["Salman", "Sultan", "Yasir"]
for x in b:
    print(x)

#Index Number
a = ["Niyaz", "Shakeel", "Suhaib"]
for i in range(len(a)):
    print(a[i])

#While loop
x = ["Salman", "Sultan", "Yasir","apple", "banana", "cherry","Niyaz", "Shakeel", "Suhaib"]
i = 0
while i < len(x):
  print(x[i])
  i = i + 1

#List Comprehension
p = ["Salman", "Sultan", "Maniyar", "Yasir", "Imtiyaz", "Faisal", "Farooq"]
q = []

for x in p:
  if "n" in x:
    q.append(x)

print(q)

#Sort List
a = ["Salman", "Sultan", "Maniyar", "Yasir", "Imtiyaz", "Faisal", "Farooq"]
a.sort()
print(a)

a = [26,20,18,12,57,43,87,72,4,6]
a.sort()
print(a)

#Sort Descending
a = ["Salman", "Sultan", "Maniyar", "Yasir", "Imtiyaz", "Faisal", "Farooq"]
a.sort(reverse = True)
print(a)

#Reverse Order
x = ["Salman", "Sultan", "Maniyar", "Yasir", "Imtiyaz", "Faisal", "Farooq"]
x.reverse()
print(x)

#Copy List
z = ["Salman", "Sultan", "Yasir"]
a = z.copy()
print(a)


z = ["Salman", "Sultan", "Yasir"]
a = list(z)
print(a)

#Join List
a = ["abc", "pqr", "xyz"]
b = [123, 231, 321]
z = a + b
print(z)

a = ["abc", "pqr", "xyz"]
b = [123, 231, 321]
for x in b:
  a.append(x)
print(a)

#List Method
#count
names = ["Salman", "Sultan", "Suhaib", "Yasir", "Suhaib"]
x = names.count("Suhaib")
print(x)




#           ----------------------------TUPLE------------------------



a = ("Salman", "Sultan", "Suhaib", "Yasir", "Suhaib")
print(a)

#Access Tuple Items
x = ("Salman", "Sultan", "Suhaib", "Yasir", "Suhaib")
print(x[3])

#Negative Indexing
a = ("Salman", "Sultan", "Suhaib", "Yasir")
print(a[-2])

#Range of Indexes
x = ("Salman", "Sultan", "Suhaib", "Yasir", "Suhaib")
print(x[2:4])

#Change Tuple Values
x = ("Salman", "Sultan", "Suhaib", "Yasir", "Suhaib")
y = list(x)
y[2] = "Saleem"
x = tuple(y)
print(x)

#Add item
x = ("Shuaib", "Yasir", "Suhaib")
y = list(x)
y.append("Faisal")
x = tuple(y)
print(x)

#Remove item
x = ("Salman", "Sultan", "Shuaib", "Yasir", "Suhaib")
y = list(x)
y.remove("Shuaib")
x = tuple(y)
print(x)

#Unpacking a Tuple
a = ("Salman", "Yasir", "Suhaib")
(CE, EE, ME) = a
print(CE)
print(EE)
print(ME)

#Using Asterisk*
fruits = ("Salman", "Yasir", "Sultan", "Adnan", "Zubair", "Suhaib")
(CE, EE, *ME) = fruits
print(CE)
print(EE)
print(ME)

#for loop
a = ("Salman", "Yasir", "Sultan")
for x in a:
  print(x)

#while loop
a = ("Salman", "Yasir", "Sultan")
i = 0
while i < len(a):
  print(a[i])
  i = i + 1

#join tuples
a = ("abc", "bde" , "cfg")
b = (11, 12, 13)
c = a + b
print(c)

#Multiply tuple
a = ("Salman", "Yasir", "Sultan")
b = a * 2
print(b)

#tuple count method
a = (10,20,30,40,50,60,70,80)
x = a.count(5)
print(x)



#           ----------------------------SETS------------------------




#Set
x = {"Adnan", "Zubair", "Suhaib"}
print(x)

#length of set
a = {"Adnan", "Zubair", "Suhaib"}
print(len(a))

#other way to write set
s = set(("banana", "guava", "mango"))
print(s)

#Acess items
s = {"banana", "guava", "mango"}
for x in s:
  print(x)


#Add sets
a = {"Salman", "Yasir", "Sultan"}
b = {"banana", "guava", "mango"}
a.update(b)
print(a)

#Remove items
a = {"banana", "guava", "mango"}
a.remove("mango")
print(a)

#Join sets
a = {"abc", "bca" , "cab"}
b = {123, 231, 312}
c = a.union(b)
print(c)










