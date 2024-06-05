
my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [6, 7, 8, 9, 10],
    'dict': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
    'set': {11, 12, 13, 14, 15}
}

print("Last element of the tuple:", my_dict['tuple'][-1])

my_dict['list'].append(11)
del my_dict['list'][1]

my_dict['dict'][('i am a tuple',)] = 'new value'
del my_dict['dict']['a']

my_dict['set'].add(16)
my_dict['set'].discard(11)

print("\nUpdated dictionary:", my_dict)
