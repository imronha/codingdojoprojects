# Push Front
# This algorithm might be familiar. Write a function that takes in a list and a
# value, and adds the value to the front of that list, outputting the changed list.
# This should be done in place> This means you should not create a new list, but
# change the existing one. Try using your newly discovered Python swap! Here's what
# your function should look like:
#
#   def push_front(arr, val):
#     ...
#     return arr
# 
# To get the most out of this exercise, limit your use of built-in functions to
# only the most basic, doing the harder stuff manually. Use only the built-in
# list.append(value) method to solve this problem.


def push_front(arr, val):
  i = len(arr)
  arr.append(i)
  while i >=0:
    arr[i],arr[i-1] = arr[i-1],arr[i]
    i -= 1
  arr[0] = val
  print arr

push_front([1,2,3,4],8)
