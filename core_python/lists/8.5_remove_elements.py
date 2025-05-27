#Task1: Remove the element 6 from the list.
#Task2: Try to remove the element 7 from the list and observe the error.

'''
Here, we created a list named lst and stored some intergers in it.
The "remove" method on a list removes the first occurence of the value in that list.
i.e., if you called lst.remove(1), it removes the first occurence of 1 from the list.

The len function returns the length of the list.
'''

lst = [1, 2, 3, 4, 5, 6]
print(lst) #[1, 2, 3, 4, 5, 6]
print(len(lst)) #6
print('-------------')

lst.remove(1)
print(lst) #[2, 3, 4, 5, 6]
print(len(lst)) #5
print('-------------')

lst.remove(2)
print(lst) #[3, 4, 5, 6]
print(len(lst)) #4
print('-------------')

#Task1
#remove the element and print the list

#Task2
#try to remove the element that does not exist in the list.