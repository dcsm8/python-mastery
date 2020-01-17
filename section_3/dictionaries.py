# Dictionary

dictionary = {
    'a': [1, 2, 3],
    'b': 'Hello',
    'c': True
}

user = dict(name='David')

print(dictionary.get('d'))
print(user)


print('a' in dictionary)
print('hello' in dictionary.values())

user2 = user.copy()

print(user)
print(user2)

user2.clear()

print(user)
print(user2)

user.update({'name': 'Dave', 'age': 23})
print(user)
