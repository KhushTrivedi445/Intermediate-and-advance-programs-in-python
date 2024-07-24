"""
This python script asks for a password as string
checks for suitable criterea for a strong password and suggests with the required missing elements
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

print()                                                  # print() statement without arguement is generally used to print new line in python

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
