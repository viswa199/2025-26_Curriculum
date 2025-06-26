# 1. In this program, we are generating a sample nested list using nested for loops.
# 2. We created an empty list named lst.
# 3. we are using a nested for loop on a range function.
# 4. During every iteration of higher level for loop(i), we are creating an empty list named lst_2.
# 5. We are appending elements to the lst_2 on every (j) for loop iteration.
# 6. We are appending lst_2(list) to the lst(list) after (j) for loop completed it's iteration.

#Task: Read the instructions carefully and complete the program on line 18.


lst_1 = []

for i in range(5):
    lst_2 = []
    for j in range(5):
        lst_2.append(i*j+1)
    #insert your code here, Study the 6 steps above properly.


print(lst_1)
