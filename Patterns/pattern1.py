# Pattern 1 :
#  Right Angle Triangle  

# * 
# * *
# * * *
# * * * *
# * * * * *

# Code

n = int (input("Enter the number of rows : "))
for i in range(0,n,1):
    for j in range(0,i+1,1):
        print("*",end=" ")
    print()
