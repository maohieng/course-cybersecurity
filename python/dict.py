students = {"Alice": 25, "Bob": 27, "Claire": 17, "Dan": 21, "Emma": 22}
print(students)

# values
vals = students.values()
print('Values:', vals)

# keys
itms = students.items()
print('Items:', itms)

# for k, v in students.items():
#     print(k, v)

# copy
students_copy = students.copy()
print('student copy:', students_copy)

# alias
students_alias = students

students["Alice"] = 26

print('student copy again:', students_copy)
print('students alias:', students_alias)

# delete
del students["Claire"]
print('after delete students:', students)

# difference keys type
strange_students = {"Alice": 25, 2: 27, "Claire": 17, 3: 21, "Emma": 22}
print('strange students:', strange_students)
strange_students['2'] = 30
print('strange students2:', strange_students)
print(len(strange_students))

print('Does Alice is in strange_students:', 'Alice' in strange_students)

# compare 2 dicts
print('Compare 2 dicts:', students == strange_students)

# tuple of dicts keys
print('Tuple of students keys:', tuple(students.keys()))

# tuple of dicts values
print('Tuple of students values:', tuple(students.values()))

# tuple of dicts items
print('Tuple of students items:', tuple(students.items()))

# get value by key
print('Get value by key using get():', students.get('Alice'))
print('Get value by key:', students["Alice"])

# get value by key with default value
print('Get value by key with default value:', students.get('X', 0))

# concat 2 dicts
students.update(strange_students)
print('Concat 2 dicts:', students)

# clear strage_students
strange_students.clear()
print('Clear strange_students:', strange_students)

# pop
print('Pop Alice:', students.pop('Alice'))
print('After pop:', students)