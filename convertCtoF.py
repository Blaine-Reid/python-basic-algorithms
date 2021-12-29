# create function that takes celsius and returns fahrenheit

def convertToF(celsius):
  fahrenheit = (int(celsius) * 9/5) + 32
  return fahrenheit

celsius = input("Enter Celsius to Convert to Fahrenheit: ")

print(convertToF(celsius))