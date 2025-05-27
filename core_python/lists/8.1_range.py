#Task: Create odd numbers between 0 and 100.

'''
range will generate a sequence of numbers in the given range.
range can have three arguments: start(optional), stop, step(optional)
If you only provided one argument to the range function, it is stop. start has default value of 0 and step has default value of 1.
range is exclusive of stop, it does not include stop value.
'''

#We only provided one argument to the range, 10 is the value of stop. start & step have default values.
numbers = list(range(10))
print(numbers)

#We provided two arguments to the range, 1 and 10 are the values of start and stop respectively. step has the default value.
numbers = list(range(1, 10))
print(numbers)

#We provided three arguments to the range, 0, 10, 2 are the values of start, stop and step respectively.
even_numbers = list(range(0, 10, 2))
print(even_numbers)