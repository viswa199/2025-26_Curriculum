# range will generate a sequence of numbers in the given range on line 8.
# range can have three arguments: start(optional), stop, step(optional) on line 16.

#Task: Create odd numbers between 0 and 100 using range on line 21 and print it.

#We only provided one argument to the range, 10 is the value of stop.
# start & step have default values.
numbers = list(range(10))
print(numbers)

#We provided two arguments to the range,
# 1 and 10 are the values of start and stop respectively. step has the default value.
numbers = list(range(1, 10))
print(numbers)

#We provided three arguments to the range, 0, 10, 2 are the values of start,
# stop and step respectively.
even_numbers = list(range(0, 10, 2))
print(even_numbers)

