#!/usr/bin/env python
# coding: utf-8

# In[7]:


'''
Given three real numbers aa, bb, cc. Write a program that finds the real roots of a quadratic equation
ax ^ 2 + bx + c = 0.
Output data format
The program should print the real roots of the equation if they exist, or the text "Нет корней" otherwise.

Note. If the equation has two roots, then you should derive them in ascending order.
'''

from math import *
a=float(input())
b=float(input())
c=float(input())
z=(b**2)-(4*a*c)
if z>0:
    a1=(-b-sqrt(z))/(2*a)
    a2=(-b+sqrt(z))/(2*a)
    if a1>a2:
        print(a2, a1, sep="\n")
    else:
        print(a1, a2, sep="\n")
elif z==0:
    print(-b/(2*a))
else:
    print("Нет корней")


# In[ ]:




