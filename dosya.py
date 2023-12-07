file  = open("musteriler.txt","r") #+ defoult "r"
#print(file.read())

print("***********")
#print(file.readline())

for line in file:
    print(line)

file.close()

fileToAppend = open("ogrenciler.txt","w")
fileToAppend.write("\n")
fileToAppend.write("Ahmet")
fileToAppend.close()

import os
if os.path.exists("ogrenciler.txt"):
    os.remove("ogrenciler.txt")
    print("Dosya Silindi")
else:
    print("Dosya yok")

os.rmdir("Deneme")

#- Read "r" ---> Okuma 
#- Append "a" --> Ekleme
#- Write "w" --> Dosyanın üzerine yazar
#- Create "x" --> Dosya oluşturur,eğer varsa hata verir

