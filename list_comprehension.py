nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in nums:
    print(num)

num_print = [x for x in nums if x%2 == 0]
print(num_print)

num_sqrd = [num**2 for num in nums]
print(num_sqrd)

#Generate a letter number pair

result_lst = []
for letter in 'abcd':
    for num in range(4):
        result_lst.append((letter, num))
print (result_lst)

# Same result with list comprehension
let_pair = [(l,n) for l in 'abcd' for n in range(4)]
print(let_pair)

#Dictionary comprehension

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Supernam', 'Spiderman', 'Wolverine', 'Deadpool']

my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero

print(my_dict)

comp_dict = { name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print(comp_dict)