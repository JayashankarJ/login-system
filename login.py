import hashlib
import os

salt = os.urandom(32)

print("\n")
print("Hello all,this is my simple program of login system using python")
print("Create your account")
name=input("Username : ")
user=input ("Password : ")
print("\n")

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
    print("invalid username!")

password= hashlib.pbkdf2_hmac( 'sha256', password.encode('utf-8'), salt,  100000 )

print("Account created successfully")
print ("Login to your account")
print("\n")
us= input("Username : ")
pa= input("password : ")
pa= hashlib.pbkdf2_hmac( 'sha256', password.encode('utf-8'), salt,  100000 )
print("\n")
if username == us :
	if password == pa:
		print("Conngratulations! Login successful.")
	else :
		print("invalid password")
else :
	print("Invalid username")