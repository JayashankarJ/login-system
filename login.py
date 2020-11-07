import hashlib
import os
print("Hello all,this is my simple program of login system using python")
print("create your account")
name=input("give your name:")
user=input ("give your unique username:")
if us.islower():
     password=input("choose your strong password")
     if len(password) < 8:
         print("Make sure your password is at lest 8 letters")
    elif not password.isdigit():
        print("Make sure your password has a number")
    elif not password.isupper():
        print("Make sure your password has a capital letter")
    else:
        print("Your username and password inputted successfully")
else:
    print("username invalid!")
salt = os.urandom(32)
password= hashlib.pbkdf2_hmac( 'sha256', password.encode('utf-8'), salt,  100000 )
print("Account created successfully")
print ("Login to your account")
us= input("Username : ")
pa= input("password : ")
salt = os.urandom(32)
pa= hashlib.pbkdf2_hmac( 'sha256', password.encode('utf-8'), salt,  100000 )
if username == us :
    if password == pa:
        print("Conngratulations!Login successfully finished.")
    else :
        print("invalid password")
else :
    print("Invalid username")