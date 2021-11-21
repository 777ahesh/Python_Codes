# Pattern 4 :
# Odd Triangle 

# * 
# * * *
# * * * * *

# Code

n = int (input("Enter the number of rows : "))
k = 1
for i in range(0,n,1):
    for j in range(0,k,1):
        print("*",end=" ")
    k=k+2
    print()
