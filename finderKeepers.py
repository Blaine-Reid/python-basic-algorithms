# Basic Algorithm Scripting: Finders Keepers
# Create a function that looks through an array (first argument) and returns the first element in the 
# array that passes a truth test (second argument). If no element passes the test, return undefined.
#  Write your own code.

def findElement(array,func):
  for elem in array:                     # loop through array
    if (func(elem)): return print(elem)  # return first elem that passes func
  return print("undefined")              # print undefined if no matches


findElement([1, 3, 5, 8, 9, 10], lambda num: num % 2 == 0 ) 
#should return 8.
findElement([1, 3, 5, 9], lambda num: num % 2 == 0 ) 
#should return undefined.