#Fizz Buzz Word Game for 3 and 5 

numbers = range(1, 100)

#I will be iterating using the remainder theorem, if the remainder is 0 then it means that it is divisible

for i in numbers:
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
