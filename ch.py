# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv 
def Write_into_csv(info_t):
    With open('Student_inf.csv','a',newline='') as csv_file:
    Writer.WriteroW(["Name","Age","cntact number","emai ID"])
    Writer.WriteroW(info_t)
condition= True
while(condition):
    Student_inf= input("enter tudent inf fr Student #{} in the frmat {Name Age Contact_number Emai ID}:".format(s))
    Student_inf_t= Student_inf.split(' ')
    print ("\n the entered inf i -\n Name:{}\nAge:{}\nCn_num:{}\nEmaiID:{}"
           .format (Student_inf_t[0],Student_inf_t[1],Student_inf_t[2],Student_inf_t[3]))
    Choice_check = input("i the entered infrmatin crrect? (yeS/no):")
    if Choice_check=="yeS":
        Write_into_csv(Student_inf_t)
        condition_check= input("enter (yeS/no) if yu Want t enter inf fr anther Student: ")
        if  condition_check=="yeS":
            condition= true
        elif condition_check=="no":
            condition= false
    elif Choice_check=="no":
        print("/nplease re-enter vaue!")
            
            
            
        
           