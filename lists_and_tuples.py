courses = ['History', 'Mathematics', 'Physics', 'Chemistry', 'Biology', 'Computer Science']
courses.append('Arts')
courses.insert(2, 'Economics')
print(courses)

courses_2 = ['Geography', 'Civics', 'Accounting']
courses.extend(courses_2)
print(courses)

courses.remove('Arts')
print(courses)

courses.pop()
print(courses)

nums = [1, 5, 0, 55, -22, 44, 4, 55, 2, 4]
nums.sort()
print(nums)

nums.reverse()
print(nums)

print(sorted(courses))

for index, cor in enumerate(courses):
    print("{} - {}".format(index, cor))

new_course = ' - '.join(courses)
print(new_course)