x = ["1BHK", "2BHK", "3BHK"]
y = ["G+1", "G+2", "G+3"]
x.append(y)
print(x)

rooms = ["1BHK", "2BHK", "3BHK"]
rooms.clear()
print(rooms)

names = ["Sultan", "Salman", "Yasir"]
x = names.count("Salman")
print(x)

names = ["Sultan", "Salman", "Yasir"]
age = (27, 26, 26)
names.extend(age)
print(names)

names = ["Sultan", "Salman", "Yasir"]
names.insert(2, "Suhaib")
print(names)


names = ["Sultan", "Salman", "Yasir"]
x = names.pop(2)
print(x)

rooms = ["1BHK", "2BHK", "3BHK"]
rooms.remove("2BHK")
print(rooms)

rooms = ["1BHK", "2BHK", "3BHK"]
rooms.reverse()
print(rooms)

def myFunc(n):
  return n['DOY']
students = [
  {'S1': 'Sultan', 'DOY': 1994},
  {'S2': 'Salman', 'DOY': 1995},
  {'S3': 'Yasir', 'DOY': 1995},
  {'S4': 'Adnan', 'DOY': 1996}
]
students.sort(key=myFunc)

print(students)

