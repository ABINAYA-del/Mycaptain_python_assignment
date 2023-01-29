# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# tak 1 fibbnaci number
num=13
m=0
n=1
print("fibb fr 13 number:")
for i in range (2,num):
    p=m+n
    m=n
    n=p
    print(p,end=" ")



#tak 2 print pittive number
m=[]
b=int (input("enter the vaue:"))
m.append(b)
n=[b for b in m if b>=0]    
print(n)