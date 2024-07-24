# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 22:47:34 2024

@author: DELL
"""

password = input("enter new password : ")
up = low = sp = space = dig = length = 0


for i in password :
    length += 1
    if i.isupper():
        up += 1
    elif i.islower():
        low += 1
    elif i.isdigit() :
        dig += 1
    elif i.isspace() :
        space += 1
    else :
        sp += 1
l = [up , low ,  dig , sp ]
ls = ["Upper " , "Lowwer " ,  "digit " ,  "Special " ]

print()

if length >= 6 :

    if 0 in l :
        print("password not strong")
        for i in range(len(l)) :
            if l[i] == 0 :
                print(ls[i], end = " ")
        print("character missing")
    else:
        print("strong is password")

else:
    print("password length is less than 6 characters") 


    

