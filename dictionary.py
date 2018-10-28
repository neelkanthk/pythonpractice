# Dictionary are mutable
dictionary = {'red': 101, 'green': 102, 'yellow': 103, 'black': 104, 'white': 105}
print dictionary  # {'black': 104, 'white': 105, 'green': 102, 'yellow': 103, 'red': 101}
print dictionary['red']  # 101
print dictionary.keys()  # ['black', 'white', 'green', 'yellow', 'red']
print dictionary.values()  # [104, 105, 102, 103, 101]
dictionary.pop('red')  # remove red
for item in dictionary:
    print item.capitalize()