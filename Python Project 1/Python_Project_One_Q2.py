#Fizz Buzz Word Game for 3 and 5 

#Setting numbers as range from 1 to 100
numbers = range(1, 101)

#I will be iterating using the remainder theorem, if the remainder is 0 then it means that it is divisible
#Since a number divisible by a certain gives a remainder of 0, so I set the iteration to print FizzBuzz if both divisible by 5 and 3
#To print 'Fizz' if divisible by 3 only and To print 'Buzz' if divisible by 5 only
# Print the remaining values as numbers 
for i in numbers:
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
