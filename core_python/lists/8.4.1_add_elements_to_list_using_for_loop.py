#Task: Using range function generate a even numbers between 0 and 100. Create an empty list and append
#every element of that range function to the list using for loop.

'''
Here, we created an empty list named lst.
We used for loop on range(10), we know that range function generates a sequence of numbers.
In this case, it generates 0...9 numbers.
Using for loop, we iterate through the range function, i.e. 0 to 9.
We are appending(inserting at the end of the list.) every element in range(10) to the lst.
At last, we are printing the lst.(observe the output carefully)
'''

lst = []
for i in range(10):
    lst.append(i)

print(lst)