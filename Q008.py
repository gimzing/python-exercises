#----------------------------------------#
# Question 8
# Level 2
#
# Question:
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

input = "without,hello,bag,world"
# input = input().split(",")
input = input.split(",")
input.sort()
input = ",".join(input)
print(input)
