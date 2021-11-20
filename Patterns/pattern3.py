# Pattern 1 :
# empty Sqauare

# * * * * *
# *       *
# *       *
# *       *
# * * * * *

# Code

n = int (input("Enter the number of rows : "))
for i in range(0,n,1):
    for j in range(0,n,1):
        if(i==0 or i == n-1 or j==0 or j==n-1):
            print("*",end=" ")
        else:
            print(end="  ")
    print()