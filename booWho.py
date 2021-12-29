# Basic Algorithm Scripting: Boo who
# Check if a value is classified as a boolean primitive. Return true or false. Boolean primitives are true and false. 
# Write your own code.

def booWho(val):
  return print(bool(val))



booWho(True) 
#should return true.

booWho(False) 
#should return false.

#any list,set,tuple, and dicionary not empty are true
booWho([1, 2, 3]) 
#should return false.
booWho({ "a": 1 }) 
#should return false.

#numbers execpt 0 are true in python
booWho(1) 
#should return true.

#strings are true in python
booWho("a") 
#should return true. 
booWho("true") 
#should return true.
booWho("false") 
#should return true.