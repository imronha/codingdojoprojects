# Assignment: Stars
# Write the following functions.
#
# Part I
# Create a function called draw_stars() that takes a list of numbers and prints out *.
#
# For example:
#
# x = [4, 6, 1, 3, 5, 7, 25]
# Copy
# draw_stars(x)should print the following in when invoked:
#
# ****
# ******
# *
# ***
# *****
# *******
# *************************
x = [4, 6, 1, 3, 5, 7, 25]
def draw_stars(arr):
  for i in arr:
    stars = ""
    for j in range(0,i):
      stars += "*"
    print (stars)

draw_stars(x)

# Part II
# Modify the function above. Allow a list containing integers and strings to be
# passed to the draw_stars() function. When a string is passed, instead of
# displaying *, display the first letter of the string according to the example
# below. You may use the .lower() string method for this part.
#
# For example:
#
# x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
# Copy
# draw_stars(x) should print the following in the terminal:
#
# ****
# ttt
# *
# mmmmmmm
# *****
# *******
# jjjjjjjjjjj
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars(arr):
  for i in arr:
    if isinstance(i, int):
      stars = ""
      for j in range(0,i):
        stars += "*"
      print (stars)
    elif isinstance(i, str):
      letters =""
      for k in range(0, len(i)):
        letters += (i[0]).lower()
      print(letters)

draw_stars(x)
