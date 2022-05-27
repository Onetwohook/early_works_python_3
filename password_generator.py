#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


rand_letter = 0
pw_letters = str()
for letter in letters:
  if rand_letter < nr_letters:
    pw_letters += (" " +random.choice(letters))
    rand_letter += 1    
  else:
     break 

rand_sym = 0
pw_sym = str()
for symbol in symbols:
  if rand_sym < nr_symbols:
    pw_sym += (" " + random.choice(symbols))
    rand_sym += 1
  else:
    break

rand_number = 0
pw_num = str()
for num in numbers:
  if rand_number < nr_numbers:
    pw_num += (" " + random.choice(numbers))
    rand_number += 1
  else:
    break

# takes variables from for loops & make them into lists
letter_list = list(pw_letters.split())
num_list = list(pw_num.split())
sym_list = list(pw_sym.split())

#shuffles those lists
mixer = list(zip(letter_list + num_list + sym_list))
random.shuffle(mixer)

#joins lists back together by turning them from tuples into str for .join to work
print(''.join(''.join(elems) for elems in mixer))



