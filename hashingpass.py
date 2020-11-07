import hashlib
import os

users = ["jayashakar", "sam", "albin"];

print("Welcome to my Login System" + "\n")

username = input("Username : ")
password = input("Password : ")

currentPassword = "test"

salt = os.urandom(32)

inputKey = hashlib.pbkdf2_hmac( 'sha256', password.encode('utf-8'), salt,  100000 )
currentKey = hashlib.pbkdf2_hmac( 'sha256', currentPassword.encode('utf-8'), salt,  100000 )

exists = username in users

print("\n")
if exists :
	if inputKey == currentKey :
		print("success")
	else :
		print("invalid password")
else :
	print("Invalid username")