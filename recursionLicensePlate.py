# Recursion: License Plate
# Published by Deep Xavier in
# logic recursion regex strings
# Traveling through Europe one needs to pay attention to how the
# license plate in the given country is displayed. When crossing
# the border you need to park on the shoulder, unscrew the plate,
# re-group the characters according to the local regulations,
# attach it back and proceed with the journey.
# Create a solution that can format the dmv number into a plate
# number with correct grouping. The function input consists of
# string s and group length n . The output has to be upper case
# characters and digits. The new groups are made from right to
# left and connected by - . The original order of the dmv number is
# preserved.

def licensePlate(str, num):
  str = str.upper().replace('-','') #convert to uppercase
  if len(str)<=num:
    return str
  else:
    clip = str[len(str)-num:]
    return licensePlate(str[:len(str)-num] ,num) + "-" + clip



print(licensePlate("5F3Z-2e-9-w", 4)) #➞ "5F3Z-2E9W"
print(licensePlate("2-5g-3-J", 2)) #➞ "2-5G-3J"
print(licensePlate("2-4A0r7-4k", 3)) #➞ "24-A0R-74K"
print(licensePlate("nlj-206-fv", 3)) #➞ "NL-J20-6FV"
