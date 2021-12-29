# Basic Algorithm Scripting: Truncate a String
# Truncate a string (first argument) if it is longer than the given maximum string length (second argument). 
# Return the truncated string with a ... ending. Write your own code.

def truncateString(str,length):
  print(str) if (len(str)<=length) else print(str[:length] + '...')


truncateString("A-tisket a-tasket A green and yellow basket", 8) 
#should return "A-tisket...".
truncateString("Peter Piper picked a peck of pickled peppers", 11) 
#should return "Peter Piper...".
truncateString("A-tisket a-tasket A green and yellow basket", len("A-tisket a-tasket A green and yellow basket")) 
#should return "A-tisket a-tasket A green and yellow basket".
truncateString("A-tisket a-tasket A green and yellow basket", len("A-tisket a-tasket A green and yellow basket") + 2) 
#should return "A-tisket a-tasket A green and yellow basket".
truncateString("A-", 1) 
#should return "A...".
truncateString("Absolutely Longer", 2) 
#should return "Ab...".