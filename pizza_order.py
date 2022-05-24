print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# assigns size to variable
if size == "S":
  pizza = 15
elif size == "M":
  pizza = 20
else:
  pizza = 25

# gives two variables depending on size of pizza
if add_pepperoni == "Y" and size == "S":
  pizza += 2
if size == "M" or size == "L":
  pizza += 3 
  
#final variable
if extra_cheese == "Y":
  pizza += 1

# combines all variables for final price
print(f"Your final bill is £{pizza}")
