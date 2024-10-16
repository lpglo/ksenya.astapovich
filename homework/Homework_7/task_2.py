words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

print(*(word * count for word, count in words.items()), sep='\n')
