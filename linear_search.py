def linear_search(alist, key):
    for i in range(len(alist)):
        if alist[i] == key:
            return i
    return -1 
alist = input('Enter the list of numbers: ')
alist = alist.split()
alist = [int(x) for x in alist]
key = int(input('The number to search for: '))
index = linear_search(alist, key)
if index < 0:
    print('{} was not found at.'.format(key))
else:
    print('{} was found at index of the {}.'.format(key, index))
