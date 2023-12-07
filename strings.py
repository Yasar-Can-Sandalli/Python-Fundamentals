# SUBSTRİNG
mesaj = "Merhaba dünya" 

print(mesaj[2:5])

yeniMesaj = mesaj[2:5] # 2 dahil 5 dahil değil
print(yeniMesaj)

yeniMesaj2 = mesaj[2:] # 2 den sonra her şey
print(yeniMesaj2)

yeniMesaj3 = mesaj[:2] # 2 ye kadar 2 dahil değil veya 0:2
print(yeniMesaj3)

print(mesaj[len(mesaj) - 1])

#? Lower Upper
yeniMesaj4 = mesaj.lower() 
yeniMesaj5 = mesaj.upper()
print(yeniMesaj4 + " " +yeniMesaj5)

#? Replace
print(mesaj.replace("ü","u")) # Tüm ü leri u yaptı
print(mesaj.replace("a","e")) # Tüm a ları e yaptı

#? Split ---> Boşluğa göre ayırır "Ayraç"

bilgi = "Yaşar Can Sadallı İzmir 9Eylül  "
print(bilgi.split(" ")) 

bilgi2 = "Yaşar Can;Sandallı;Rize;Bilgisayar Bilimleri"

print(bilgi2.split(";"))
print("Adı: "+bilgi2.split(";")[0])

# Strip ---> Boşlukları atmaya yarar
bilgi3 = " Engin;Demiroğ;33;Ankara  ".strip()
print(bilgi3.split(" "))
print("Adı: " + bilgi3.split(";")[0])

# input
name = input("Adınız ? : ")
print("Merhaba" + name)
sayı1 = input("Sayı 1 ? = ")
sayı2 = input("Sayı 2 ? = ")
print(int(sayı1)+ int(sayı2))