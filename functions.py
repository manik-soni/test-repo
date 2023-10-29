def calculateLength(str):
    length = 0
    for alpha in str:
        length += 1
    return length

print(len("Manik Soni"))
print(calculateLength("Manik Soni"))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info(['math', 'computer Science'], name='manik soni', age = 36)