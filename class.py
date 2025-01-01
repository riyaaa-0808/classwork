'''#write a program to add two numbers
a=int(input("enter the first number:")) #taking input from the user
b=int(input("enter the second number:"))
c=a+b
print(f"added number is :{c} ")
#write a program to print areas of rectangle
l=int(input("enter the length:"))
b=int(input("enter the breadth"))
r=l*b
print(f"area of rectangle is {r}")
#write a program to print area of cricle
import math #To use math.pi for the value of pi
radius=float(input("enter the radius"))
circle_area = math.pi * radius * radius
print(f"area of circle is :{circle_area :.2f}")
#write a program to check if the given number is odd or even
num=int(input("enter the number:"))
if num % 2 ==0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")
#Input score from the user
score = float(input("Enter your score: "))
#check the grade
if score >= 90:
    print("Grade A")
elif score >= 70:
    print("Grade B")
elif score >= 60:
    print("Grade C")
elif score >= 50:
    print("Grade D")
else:
    print("Grade K")
#Input temperature from the user
temp_celsius = float(input("Enter the temperature in celsius: "))
  
#Convert to Fahrenheit
temp_fahrenheit = (temp_celsius * 9/5) + 32

#Print the result
print(f"{temp_celsius}degree celsius is equal to {temp-fahrenheit}degree fahrenheit.")'''
#write a program to find the greatest among three numbers.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 > num2 and num1 > num3:
     print(f"The greatest number is {num1}.")
elif num2 > num1 and num2 > num3:
    print(f"The greatest number is : {num2}.")
elif num3 > num1 and num3 > num2:
    print(f"The greatest is : {num3}.")
else:
    print("Two or more numbers are equal and the greatest.")
    