# Find and Replace
# In this string: words = "It's thanksgiving day. It's my birthday,too!" print the position of the first instance of the word "day". Then create a new string where the word "day" is replaced with the word "month".
words = "It's thanksgiving day. It's my birthday,too!"
end = len(words)
index = words.find("day", 0, end)
replaced = words.replace("day", "month")
print (replaced, "First instance replaced at index", index,".")

# Min and Max
# Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.
x = [2,54,-2,7,12,98]
x.sort()
print ("Min:",x[0],"Max:",x[-1])

# First and Last
# Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only the first and last values in the original list. Your code should work for any list.
x = ["hello",2,54,-2,7,12,98,"world"]
newlist =[]
newlist.append(x[0])
newlist.append(x[-1])

print ("First:",x[0],"Last:",x[-1])
print (newlist)

# New List
# Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
first =x[:int(len(x)/2)]
second = x[int(len(x)/2):]
print (first)
print (second)

second.insert(0,first)
print (second)
