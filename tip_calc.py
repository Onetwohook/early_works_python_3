# a simple tip calculator that adds the tip, divides by number of people
# and gives what each person should pay

print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12 or 15? ")
people = input("How many people to split the bill? ")

# converts inputs to floats and ints. Probably should've used an f string here...

float_bill = float(bill)
int_tip = int(tip)
int_people = int(people)
# works out the %
tip_percent = float_bill / 100 * int_tip
# adds % to bill
sub_total = tip_percent + float_bill

final_amount = sub_total / int_people

bill_per_person = (round(final_amount, 2))

# Adds 2 decimal places even if total ends in 1 decimal place
bill_per_person = "{:.2f}".format(final_amount)

print(f"Each person needs to pay {bill_per_person}")
