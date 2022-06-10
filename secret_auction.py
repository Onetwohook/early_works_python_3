keep_auction_going = True
buyers = {}

while keep_auction_going == True:
  name = input("What is your name? \n")
  bid = int(input("What is your bid? \n£"))

  buyers[name] = bid

  another_round = input("Are there any more bidders? Type Yes or No: \n")
  if another_round == "Yes":
    clear()
    keep_auction_going = True
  else: 
    keep_auction_going = False

winner = max(buyers, key=buyers.get)

print(f"The winner is {winner} with a bid of £{buyers[winner]}")
