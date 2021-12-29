# Basic Algorithm Scripting: Title Case a Sentence
# Return the provided string with the first letter of each word capitalized. Make sure the rest of the word is in 
# lower case. For the purpose of this exercise, you should also capitalize connecting words like "the" and "of". 
# Write your own code.


# def titleCase(string):
#   sentence = []
#   for word in string.lower().split(): 
#     sentence.append(str(word.capitalize()))
#   return print(' '.join(sentence))


def titleCase(string):

    print(" ".join(x.capitalize() for x in string.lower().split()))

    

titleCase("I'm a little tea pot") 
#should return a string.
titleCase("I'm a little tea pot") 
#should return I'm A Little Tea Pot.
titleCase("sHoRt AnD sToUt") 
#should return Short And Stout.
titleCase("HERE IS MY HANDLE HERE IS MY SPOUT") 
#should return Here Is My Handle Here Is My Spout.