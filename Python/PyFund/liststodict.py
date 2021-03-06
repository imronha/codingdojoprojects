# Assignment: Making Dictionaries
# Create a function that takes in two lists and creates a single dictionary where the first list contains keys and the second values. Assume the lists will be of equal length.
#
# Your first function will take in two lists containing some strings. Here are two example lists:
#
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

# Here's some help starting your function.
#
def make_dict(arr1, arr2):
  new_dict = {}
  for i in range(0,len(arr1)):
      new_dict[arr1[i]] = arr2[i]
  return new_dict
