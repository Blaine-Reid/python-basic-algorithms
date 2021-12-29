# Find the longest word in a string

def longestWord(str):
  longest = 0
  arr = str.split(' ')
  for word in arr:
    if len(word)>longest:
      longest = len(word)
  return longest

print(longestWord("The quick brown fox jumped over the lazy dog"))# should return 6.