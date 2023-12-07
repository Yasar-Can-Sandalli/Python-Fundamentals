ogrenciler = ["Engin","Derin","Salih","Ali","Ayse"]

fileToAppend = open("ogrenciler.txt","w")

for ogrenci in ogrenciler:
    fileToAppend.write(ogrenci)
    fileToAppend.write("\n")

fileToAppend.close()