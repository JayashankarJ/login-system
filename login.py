import hashlib
import os

# Generate salt
salt = os.urandom(32)

#Registration Section
print("\n")
print("Hello all,this is my simple program of login system using python")
print("Create your account")
name=input("Username : ")
username=input ("Password : ")
print("\n")

# Validate Data
if username.islower():
	password=input("Choose a strong Password : ")
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

#Encrypt Password
passwd = hashlib.pbkdf2_hmac( 'sha256', password.encode('utf-8'), salt,  100000 )

print("Account created successfully")
print("\n")

# Login Module
print ("Login to your account")
print("\n")
us= input("Username : ")
pa= input("Password : ")
pa= hashlib.pbkdf2_hmac( 'sha256', password.encode('utf-8'), salt,  100000 )
print("\n")

# User Authentication
if username == us :
	if passwd == pa:
		print("Conngratulations! Login successful.")
	else :
		print("invalid password")
else :
	print("Invalid username")