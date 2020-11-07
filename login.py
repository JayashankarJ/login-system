import hashlib
import os

salt = os.urandom(32)

print("Hello all,this is my simple program of login system using python")
print("\n")
print("create your account")
print("\n")

name=input("Username : ")
user=input ("Password : ")

if us.islower():
	password=input("Choose a strong Password")
	if len(password) < 8:
		print("Make sure your password is at lest 8 letters")
	elif not password.isdigit():
		print("Make sure your password has a number")
	elif not password.isupper():
		print("Make sure your password has a capital letter")
	else:
		print("Your username and password generated successfully")
else:
    print("Username Invalid!")

password= hashlib.pbkdf2_hmac( 'sha256', password.encode('utf-8'), salt,  100000 )

print("Account created successfully")
print("\n")
print ("Login to your account")
print("\n")
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