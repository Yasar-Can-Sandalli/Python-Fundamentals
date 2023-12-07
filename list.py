# ogrenci1 = "Yaşar Can"
# ogrenci2 = "Ali"
# ogrenci3 = "Ahmet"

# print(ogrenci1)
# print(ogrenci2)
# print(ogrenci3)

ogrenciler = ["Yaşar Can","Ali","Ahmet","Ayşe"]
ogrenciler.append("Aslı") # array e yeni eleman ekler

print(ogrenciler[1])
ogrenciler.remove("Yaşar Can") # array den elemanı siler
print(ogrenciler)



# List Constuctor

sehirler = list(("Ankara","Rize","Muğla","Manisa","Rize"))
print(sehirler)
print(len(sehirler))

#diğer fonksiyonlar

#print(sehirler.clear())
print("Rize sayısı " + str(sehirler.count("Rize"))) # array de Rizeden kaç tane var
print("Ankara Index i " + str(sehirler.index("Ankara")))#Ankara kaçıncı indexte --> birden fazla ise ilk bulduğunu söyler
sehirler.remove("Rize") # ilk bulduğunu sildi -- > sonda bir Rize daha var
sehirler.pop(1) # index numarasına göre sildi
print(sehirler)
sehirler.insert(1,"Rize") # birinci index e Rize ekledim(index e göre)
print(sehirler)
sehirler.reverse()
print(sehirler)

sehirler3 = sehirler.copy()
sehirler2  = sehirler
sehirler2[0] = "İzmir" # --> bunu yapınca sehirler[0] da İzmir oldu 
print(sehirler2) 
print(sehirler) #sehirler2[0]ı İzmir yaptım ama sehirler[0]da İzmir oldu

# ! Referans Tip ---> Nedir Araştır ? 
print(sehirler3)
sehirler.extend(sehirler3) # iki arrayi birleştirme
sehirler.sort() # küçükten büyüğe sıralar 
sehirler.reverse() #sort ettikten sonra reverse ettim -> büyükten küçüğe
print(sehirler)



