# Assignment: Names
# Write the following function.
#
# Part I
# Given the following list:
#
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def names(arr):
  for i in range(0,len(arr)):
    print (students[i]["first_name"], students[i]["last_name"])

names(students)

# Part II
# Now, given the following dictionary:
#
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
# Copy
# Create a program that prints the following format (including number of characters in each combined name):
#
# Students
# 1 - MICHAEL JORDAN - 13
# 2 - JOHN ROSALES - 11
# 3 - MARK GUILLEN - 11
# 4 - KB TONEL - 7
# Instructors
# 1 - MICHAEL CHOI - 11
# 2 - MARTIN PURYEAR - 13

def all_users(arr):
  for role in arr:
    i = 0
    print (role)
    for person in arr[role]:
      i += 1
      print (i, person['first_name'], person['last_name'], len(person['first_name'])+len(person['last_name']))

all_users(users)
