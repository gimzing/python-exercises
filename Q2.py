#----------------------------------------#
# Question 2
# Level 1
#
# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

def factorial(number):
    result = number
    for i in range(number - 1,0,-1):
        result *= i
    print(result)

input = input()
factorial(int(input))
