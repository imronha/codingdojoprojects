# Assignment: Coin Tosses
# Write a function that simulates tossing a coin 5,000 times.
# Your function should print how many times the head/tail appears.
#
# Sample output should be like the following:
#
# Starting the program...
# Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
# Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
# Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
# Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
# ...
# Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far
# Ending the program, thank you!
# Hint: Use the python built-in round function to convert that floating point number into an integer

import random
def cointoss():
  heads = 0
  tails = 0
  for i in range(1,5001):
    x = random.random()
    y = random.random()
    x_rounded = round(x)
    y_rounded = round(y)
    if x_rounded == 0:
      print ("Attempt #", i, "Throwing a coin... its a head! ... Got", heads, "head(s) so far and", tails, "tail(s) so far.")
      heads +=1
    else:
        print ("Attempt #", i, "Throwing a coin... its a tail! ... Got", heads, "head(s) so far and", tails, "tail(s) so far.")
        tails +=1

cointoss()
