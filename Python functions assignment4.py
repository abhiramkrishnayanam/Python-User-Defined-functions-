#1.What does the len() function do in Python? Write a code example using len() to find the length of a list.
#len() function gives the actual length of the datastructure or the number of elements in a datastructure.
l=[1,2,34,55]
print(len(l))

# #2.Write a Python function greet(name) that takes a person's name as input and prints "Hello, [name]!".
# def greet(name):
#     print(f"Hello {name}")
# name=input("Enter your name : ")
# greet(name)

# #3.Write a Python function find_maximum(numbers) that takes a list of integers and returns the maximum value without
# # using the built-in max() function. Use a loop to iterate through the list and compare values.
# def findmax(n):
#     max=0
#     for i in n:
#        if i>max:
#            max=i
#     return max
# list=[12,23,11,27,89,7]
# print (f"The maximum value in the list {list} is {findmax(list)}")

#4.Explain the difference between local and global variables in a Python function. Write a program
# where a global variable and a local variable have the same name and show how Python differentiates between them.
"""Ans : A local variable have its function and scope only inside the function statement(inside definition) but a
global variable have its scope in overall program.It have its own significance in the entire program.Thus we can
use a global variable anywhere in the program but the local variable is constrained inside the function."""

# base=10
# def area(height):
#     base = 5
#     print (f"the base inside the function = {base}")
#     area=base*height*0.5
#     print(f"The area of triangle having base {base} and height {height} is {area}")
# print(f"base outside the function ie; global variable= {base}")
# print(f"area of the triangle having height 6 and base as default given in the function is {area(6)}")
#concludes that the global variable (base) have'nt changed or it is different from the variable declared inside the
#function, that is local variable.


# #5.Create a function calculate_area(length, width=5) that calculates the area of a rectangle.
# # If only the length is provided, the function should assume the width is 5.
# # Show how the function behaves when called with and without the width argument.
# def calculate_area(length, width=5):
#     area = length*width
#     return area
# l=float(input("enter the length of the rectangle  : "))
# print(f"The area of the rectangle is {calculate_area(l)}") #it assumes width as 5 as default.
# length1=float(input("enter the length of the rectangle  : "))
# breadth1=float(input("enter the breadth of the rectangle  : "))
# print(f"The area of the rectangle with length {length1} and width {breadth1} is {calculate_area(length1,breadth1)}")
# #if we give value for breadth it will consider the value without assuming.
# print(f"The area of the rectangle with length 18 and width 20 is {calculate_area(18,20)}")
# #here the values are directly passed to function

