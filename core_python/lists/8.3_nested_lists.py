#Nested list also known as 2D list is a list inside of another list.
#Basically here we are storing a list as an element of another list.

lst = [1, 2, 3, 4]
print(lst)  #printing the entire list.
print(lst[1]) #printing the second element of the list.

print('----------------------------')
print('----------------------------')

lst2 = [[1, 2], [3, 4], 5, 6]
print(lst2)  #prints the entire list.
print(lst2[0])  #prints the first element of the list. (lst2[0] is also a list.)
print(lst2[0][0]) #Since lst2[0] is a list, we can index on it.