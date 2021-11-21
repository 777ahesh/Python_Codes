# Pattern 5 :
# Triangular Pyramid 

    #       1 
    #      1 1
    #     1 2 1
    #    1 3 3 1
    #   1 4 6 4 1

# Code

from math import factorial

input = int(input("Enter the number of rows : "))
for i in range(input):
    # inner loop To print spaces
   for j in range(input-i+1):

      print(end=" ")

   for j in range(i+1):
      print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

    
   print()