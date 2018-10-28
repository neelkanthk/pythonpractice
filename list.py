# Lists are mutable
list = ['banana', 'orange', 'grapes', 'mango', 'kiwi']
print list  # ['banana', 'orange', 'grapes', 'mango', 'kiwi']
# iterate over the list
for item in list:
    # capitalize first letter of each item
    print item.capitalize()

list[2] = 'pineapple'  # change the item at index
print list  # ['banana', 'orange', 'pineapple', 'mango', 'kiwi']
list.append('papaya')  # add a item at the end
print list  # ['banana', 'orange', 'pineapple', 'mango', 'kiwi', 'papaya']
list.sort()  # sort the list
# list.sort sorts the list in place, i.e. it doesn't return a new list.
sorted_list = list  # store a sorted list
print sorted_list  # ['banana', 'kiwi', 'mango', 'orange', 'papaya', 'pineapple']
