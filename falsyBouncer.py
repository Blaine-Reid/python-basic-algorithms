# Basic Algorithm Scripting: Falsy Bouncer
# Remove all falsy values from an array. 
# Falsy values in Python are empty values, such as (), [], {}, "", 
# the number 0, and the value None. And of course the value False evaluates to False.
# Hint: Try converting each value to a Boolean. Write your own code.

def bouncer(arr):
  newList = [x for x in arr if bool(x)]
  print(newList)


bouncer([7, "ate", "", False, 9]) #should return [7, "ate", 9].
bouncer(["a", "b", "c"]) #should return ["a", "b", "c"].
bouncer([False, (), 0, {}, [], ""]) #should return [].
bouncer([1, 0, (), 2, '']) #should return [1, 2].