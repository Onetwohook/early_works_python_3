year = int(input("Which year do you want to check? "))

# using equation: on every year that is evenly divisible by 4 
# **except** every year that is evenly divisible by 100 
# **unless** the year is also evenly divisible by 400

if (year % 4) != 0:
  print("Not leap")
elif (year % 100) != 0:
  print("Leap")
elif (year % 400) == 0:
  print("Leap")
else:
  print("Not leap")

