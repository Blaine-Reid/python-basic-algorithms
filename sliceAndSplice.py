# Basic Algorithm Scripting: Slice and Splice
# You are given two arrays and an index. Begin inserting elements at index n of the second array. 
# Return the resulting array. The input arrays should remain the same after the function runs. Write your own code.

def frankenSplice(arr1,arr2,index):
  for x in range(len(arr1)): arr2.insert( index+x, arr1[x])
  return print(arr2)



frankenSplice([1, 2, 3], [4, 5], 1) 
#should return [4, 1, 2, 3, 5].
frankenSplice([1, 2], ["a", "b"], 1) 
#should return ["a", 1, 2, "b"].
frankenSplice(["claw", "tentacle"], ["head", "shoulders", "knees", "toes"], 2) 
#should return ["head", "shoulders", "claw", "tentacle", "knees", "toes"].
