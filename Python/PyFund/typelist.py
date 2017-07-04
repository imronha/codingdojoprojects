# Assignment: Type List
# Write a program that takes a list and prints a message for each element in the list,
# based on that element's data type.

# Your program input will always be a list. For each item in the list, test its data type.
# If the item is a string, concatenate it onto a new string.
# If it is a number, add it to a running sum. At the end of your program print the string,
# the number and an analysis of what the array contains. If it contains only one type,
# print that type, otherwise, print 'mixed'.

l = ['magical unicorns',19,'hello',98.98,'world']
l2 = [2,3,1,7,4,12]
l3 = ['magical', 'unicorns']

def typelist(lst):
    string = ''
    currentsum = 0
    for i in lst:
        if isinstance(i, int):
            currentsum += i
        elif isinstance(i, float):
            currentsum += i
        elif isinstance(i, str):
            string += (" "+i)
    if string != '' and currentsum !=0:
      print ("The array you entered is of mixed type.")
      print ("String:", string)
      print ("Sum: ", currentsum)
    elif string != '' and currentsum == 0:
      print ("The array you entered is of string type")
      print ("String:", string)
    elif string == '' and currentsum != 0:
      print ("The array you entered is of integer type")
      print ("Sum: ", currentsum)




typelist(l3)
typelist(l2)
typelist(l)
