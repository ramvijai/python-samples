from functools import reduce
input = [1, 2, 3, 4, 5]

# Square the number
# Map the input to the lambda function
square_lambda = map(lambda num: num*num, input)
print(list(square_lambda))

# Get all the even numbers
# Use Filter built-in function
even_lambda=filter(lambda num: num % 2 == 0, input)
print(list(even_lambda))

# Get all the odd numbers
# Use Filter built-in function
odd_lambda=filter(lambda num: num % 2 !=0, input)
print(list(odd_lambda))

# Get the sum of all the numbers
# Use Reduce built-in function
# Remember to import the package
sum_lambda=reduce(lambda sum, num: sum+num, input, 0)
print(sum_lambda)