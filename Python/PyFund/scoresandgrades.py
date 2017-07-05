# Assignment: Scores and Grades
# Write a function that generates ten scores between 60 and 100.
# Each time a score is generated, your function should display what the grade is for a particular score.
# Here is the grade table:
#
# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A

import random
def grades():
  print ("Scores and Grades")
  for i in range(1,11):
    grade = random.randint(60,100)
    # print (grade)
    if grade>=60 and grade<=69:
      print ("Score:", grade, "Your grade is a D.")
    elif grade >=70 and grade<=79:
      print ("Score:", grade, "Your grade is a C.")
    elif grade >=80 and grade<=89:
      print ("Score:", grade, "Your grade is a B.")
    elif grade >=90 and grade<=100:
      print ("Score:", grade, "Your grade is an A.")


grades()
