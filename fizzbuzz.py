# Write a program that prints the numbers from 1 to 100. 
# But for multiples of three print “Fizz” instead of the number
# and for the multiples of five print “Buzz”. 
# For numbers which are multiples of both three and five print “FizzBuzz


numbers = list(range(1,101))
# fizzbuzz_3check5 = []
for i in numbers:
  if i % 3 == 0:
    if i % 5 == 0:
      print('Fizzbuzz',i)
      fizzbuzz_3check5.append(i)
    else:
      print('Fizz',i)
    
  elif i % 5 == 0:
    print('Buzz')
  else:
    print(i)


# print(fizzbuzz_3check5)
