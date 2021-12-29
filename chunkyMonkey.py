# Basic Algorithm Scripting: Chunky Monkey
# Write a function that splits an array (first argument) into groups the length of size (second argument) 
# and returns them as a two-dimensional array. Write your own code.

def chunkArrayInGroups(arr,size):
  newArr = []
  x = 0 
  while x<len(arr):
    clip= [x for x in arr[x:x+size]]    #List Conprehesion a clipping
    newArr.append(clip)                 # append to newArr
    x+=size                             #increment x
  
  return print(newArr)                  #return newArr


chunkArrayInGroups(["a", "b", "c", "d"], 2) #should return [["a", "b"], ["c", "d"]].
chunkArrayInGroups([0, 1, 2, 3, 4, 5], 3) #should return [[0, 1, 2], [3, 4, 5]].
chunkArrayInGroups([0, 1, 2, 3, 4, 5], 2) #should return [[0, 1], [2, 3], [4, 5]].
chunkArrayInGroups([0, 1, 2, 3, 4, 5], 4) #should return [[0, 1, 2, 3], [4, 5]].
chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6], 3) #should return [[0, 1, 2], [3, 4, 5], [6]].
chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6, 7, 8], 4) #should return [[0, 1, 2, 3], [4, 5, 6, 7], [8]].
chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6, 7, 8], 2) #should return [[0, 1], [2, 3], [4, 5], [6, 7], [8]].