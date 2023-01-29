# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from typing import Dict
c_dict={}
def moSt_frequent(String:Str)-> dict:
    n_String= String.lower()
    for c in n_String:
        if c in c_dict :
            c_dict[c] = c_dict+1
        else:
            c_dict[c]=1
    return c_dict
if __name__ == "__main__":
    u_String= input("enter input:")
    moStfrequent=moSt_frequent(u_String)
    print("char cunt:",moStfrequent)
    
   