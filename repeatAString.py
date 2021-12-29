# Basic Algorithm Scripting: Repeat a String Repeat a String
# Repeat a given string str (first argument) for num times (second argument). Return an empty string if num is not 
# a positive number. Write your own code. 

def repeatStringNumTimes(str,num):
  if (num<=0): return print('') # return empty string if neg num
  multiStr = '' 
  for x in range(num): multiStr = multiStr + str  # must use range to loop a set amount of  times
  print(multiStr)


repeatStringNumTimes("*", 3) #should return "***".
repeatStringNumTimes("abc", 3) #should return "abcabcabc".
repeatStringNumTimes("abc", 4) #should return "abcabcabcabc".
repeatStringNumTimes("abc", 1) #should return "abc".
repeatStringNumTimes("*", 8) #should return "********".
repeatStringNumTimes("abc", -2) #should return "".
repeatStringNumTimes("abc", 0) #should return "".