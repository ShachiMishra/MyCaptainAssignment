# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 15:21:35 2022

@author: Shachi Mishra
"""

# Python program to print positive Numbers in a List
  
# list of numbers
list1 = [12,-7,5,64,-14]
  
# iterating each number in list
for num in list1:
      
    # checking condition
    if num >= 0:
       print(num, end = " ")
       
       
       
       
# list of numbers
list2 = [12,14,-95,3] 

# iterating each number in list
for num in list2:
      
    # checking condition
    if num >= 0:
       print(num, end = " ")
  
# Function for nth Fibonacci number
def Fibonacci(n):
   
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 
# Driver Program
print(Fibonacci(9))
