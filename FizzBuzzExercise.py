# Fizz Buzz
# Write a function to print all numbers 1 to n, but there are some constraints
# If the number is divisible by 3, print 'Fizz' instead of the number
# If the number is divisible 5, print 'Buzz' instead of the number
# If the number is divisible by both 3 and 5, print 'FizzBuzz' instead of the number
# Otherwise, simply print the number
def fizzbuzz(number):
    for num in range(1,number+1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3== 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
fizzbuzz(40)
