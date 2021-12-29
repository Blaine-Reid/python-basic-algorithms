'''
to remove duplicates from a list
first, change to dictionary, as dictionaries can't have duplicates
then convert back to list
'''

arr = ['a','b','a','b','c','c']
clear = list(dict.fromkeys(arr))

print(clear)


