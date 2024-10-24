# Question 1(i)
# Write a Python program to find the distance between two coordinate points (x1, y1) and (x2, y2).

#1(i)
import math
x1 = int(input("Enter the value of x1: "))
x2 = int(input("Enter the value of x2: "))
y1 = int(input("Enter the value of y1: "))
y2 = int(input("Enter the value of y2: "))
distance = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
print(f"The distance between two coordinate points is {distance}.")


# Question 1(ii)
# Write a Python program to find maximum between three numbers.
number_one = int(input("Enter first number: "))
number_two = int(input("Enter the second number: "))
number_three = int(input("Enter the third number: "))
max(number_one, number_two, number_three)



