
""" 

# Write your code here

"""### Q2:- Write a program that will convert celsius value to fahrenheit."""

celsius= float(input("Enter temperature in celsius:"))
fahrenheit= (celsius*9/5) + 32
print("Temperature in Fahrenheit:")

"""### Q3:- Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax."""

a= int(input("Enter the first number:"))
b= int(input("Enter the second number:"))
temp=a
a=b
b=temp
print("After swapping:")
print("First number:",a)
print("Second number:",b)

"""### Q4:- Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input."""

import math
x1= float(input("enter x1:"))
x2= float(input("enter x2:"))
y1= float(input("enter y1:"))
y2= float(input("enter y2:"))

distance=math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(" the euclidean distance:f",distance)

"""### Q5:- Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.

"""

p= int(input("enter the principal amount"))
r= int(input("enter the rate of intrest"))
t= int(input("enter the time"))
a=(p*r*t)/100
print(a)


"""### Q6:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.

For example:
Input:
heads -> 4
legs -> 12
<br>
Output:
dogs -> 2
chicken -> 2
.....

"""
heads = int(input("heads"))
legs = int(input("legs"))
dogs = (legs - 2*heads)//2
chicken = heads - dogs
print("dogs", dogs)
print("chicken", chicken)


"""### Q7:- Write a program to find the sum of squares of first n natural numbers where n will be provided by the user."""

n= int(input("Enter a integer:"))
sum_of_squares= 0
for i in range(1, n+1):
    sum_of_squares += i**2
print(f"The sum of squares of first {n} natural numbers is: {sum_of_squares}")  



"""### Q8:- Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user."""

x= float(input("Enter the first term x:"))
y= float(input("Enter the second term y:"))
n= int(input("Enter the term number n:"))
d= y-x
n= x+(n-1)*d
print(f"The {n} of arithemetic series is:{n}") 


"""### Q9:- Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user."""

a= int(input("Enter first numerator value:"))
b= int(input("Enter first denominator value:"))
c= int(input("Enter first numerator value:"))
d= int(input("Enter first denominator value:"))
n_sum= a*d+b*c
d_sum= b*d
print(f"The sum of fractions is:{n_sum}/{d_sum}")


"""### Q10:- Given the height, width and breadth of a milk tank, you have to find out how many glasses of milk can be obtained? Assume all the inputs are provided by the user.



Input:<br>
Dimensions of the milk tank<br>
H = 20cm, L = 20cm, B = 20cm
<br><br>
Dimensions of the glass<br>
h = 3cm, r = 1cm
"""

import math
H = int(input("Enter height of tank"))
L = int(input("Enter length of tank"))
B = int(input("Enter breadth of tank"))

h = int(input("Enter height of glass"))
r = int(input("Enter radius of glass"))

tank_volume = H * L * B
glass_volume = math.pi * r * r * h

num_glasses = tank_volume // glass_volume 

print("Number of glasses of milk:", int(num_glasses))