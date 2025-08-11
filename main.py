"""
Lists in Python
"""
# Defining an empty list
my_list = []

print("Empty list: ", my_list) #[]
print(type(my_list)) # <class 'list'>
print("Length of empty string: ", len(my_list)) # 0

# Adding elements to a list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print("List after adding elements: ", my_list)
print("Length of string: ", len(my_list))

# Adding an element at a specific position
my_list.insert(1, 15)

print("List after inserting 15 at second position", my_list)
print("Length of list after inserting 15 at second position: ", len(my_list))

# Extending a List
my_list.extend([50, 60, 70])

print("List after extension: ", my_list)
print("Length of list after extension: ", len(my_list))

# Removing last element from list
my_list.pop(-1)

print("List after removing element: ", my_list)
print("Length of string: ", len(my_list))

# Sorting elements in ascending order
my_list.sort()

print("List sorted in ascending order: ", my_list)

# Accessing a value in a list and displaying its index

index = my_list.index(30)

print("List: ", my_list)
print("30 is at index: ", index)
