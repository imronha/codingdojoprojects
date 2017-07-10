# Make Change
# You'll probably remember this one from your morning algorithm sessions,
# but I'll explain it just in case you haven't done it yet.
#
# Write a function that takes an amount of money in cents and returns the
# fewest number of coins possible for the number of cents. Here's an example,
# given the input 387. Now that you have a few tools at your disposal, the output
# should be a dictionary, as shown below:
#
# Solving this problem may seem relatively simple, and it is, as long as we
# use only one type of currency. Here we are assuming American currency:
#
# Dollar: 1
# Half-Dollar: 0.5 (optional)
# Quarter: 0.25
# Dime: 0.1
# Nickel: 0.05
# Penny: 0.01
#   {'dollars': 3, 'quarters': 3, 'dimes': 1, 'nickels': 0, 'pennies': 2}

def change(cents):
  coins= {'dollars': 0, 'quarters': 0, 'dimes': 0, 'nickels': 0, 'pennies': 0}
  while cents > 0:
    if cents >= 100:
      coins['dollars'] = cents/100
      cents -= (cents/100)*100
    if cents >= 25:
      coins['quarters'] = cents/25
      cents -= (cents/25)*25
    if cents >= 10:
      coins['dimes'] = cents/10
      cents -= (cents/10)*10
    if cents >= 5:
      coins['nickels'] = cents/5
      cents -= (cents/5)*5
    else:
      coins['pennies'] = cents
      cents -= cents
  print coins


change(987)
