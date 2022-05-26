# list nos 1-100, if divis by 3 print Fizz, if divis by 5 print Buzz
# if divis by 3 and 5, write FizzBuzz
number_set = range(1, 101)

for numbers in number_set:
  if numbers % 3 == 0 and numbers % 5 == 0:
    print("FizzBuzz!")
  elif numbers % 3 == 0:
    print("Fizz")
  elif numbers % 5 == 0:
    print("Buzz")
  else:
    print(numbers)
