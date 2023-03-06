"""
Write a single Python statement to generate the following pattern.
*
* *
* * *
* * * * 
"""

rows = int(input("Enter the number of rows: "))
for i in range(rows):
    for j in range(i):
        print('*', end=" ")
    print('')
    