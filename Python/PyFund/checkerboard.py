# Assignment: Checkerboard
# Write a program that prints a 'checkerboard' pattern to the console.
#
# Your program should require no input and produce console output that looks like so:
#
# * * * *
#  * * * *
# * * * *
#  * * * *
# * * * *
#  * * * *
# * * * *
#  * * * *

def checkerboard():
  for row in range(0,8):
    if row%2 == 0:
      print ("* * * * ")
    else:
      print (" * * * *")

checkerboard()
