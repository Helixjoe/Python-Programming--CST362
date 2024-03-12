#program to calculate the square root of a number
import math
number=float(input("Enter a positive number: "))
x=number
z=1.0
sq_num=number
for i in range(1,number):
    z=(z+x/z)/2
    if(sq_num>z):
        sq_num=z
print("The program's estimate: ",sq_num)
print("Python's estimate is: ",math.sqrt(number))
