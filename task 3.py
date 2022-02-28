# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 15:38:01 2022

@author: Shachi Mishra
"""

# initializing string 
test_str = "Mississippi"
  
# using dict.get() to get count 
# of each element in string 
res = {}
  
for keys in test_str:
    res[keys] = res.get(keys, 0) + 1
  
# printing result 
print ("Count of all characters in Mississippi is : \n"
                                             +  str(res))
