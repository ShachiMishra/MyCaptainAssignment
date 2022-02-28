# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 16:10:12 2022

@author: Shachi Mishra
"""

       
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
 