student = {
    "name" : "John",
    "age" : 25,
    "courses" : ['Math', 'Computer Science']
}

print(student["courses"][0])
print(student.get('phone', 'Not Found'))

student['phone'] = 12345999

print(student)
print(student.get('phone', 'Not Found'))

student.update({'name' : 'Jane', 'age': '33', 'courses': ['Physics', 'Chemistry'], 'phone': '3330-3332'})

print(student)

age = student.pop('age')
print(student)
print(age)