#creates the 'board'
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
#turns input into a list
position = list(position)

# if loops with nested if to assign x to board in right position
if position[0] == "1":
 if position[1] == "1":
  row1[0] = "x"
 elif position[1] == "2":
   row1[1] = "x"
 else: 
   row1[2] = "x"

if position[0] == "2":
  if position[1] == "1":
    row2[0] = "x"
  elif position[1] == "2":
    row2[1] = "x"
  else:
    row2[2] = "x"

if position[0] == "3":
  if position[1] == "1":
    row3[0] = "x"
  elif position[1] == "2":
    row3[1] = "x"
  else:
    row3[2] = "x"
# prints new board with x in place
print(f"{row1}\n{row2}\n{row3}")
