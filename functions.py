sehir = "Ankara"
sehir = sehir.upper()
sehir = sehir.replace("A","E")
print(sehir)
print(sehir.endswith("E"))

def selamVer(name = "Ziyaretçi"):
    print("Merhaba " + name)

selamVer("Yaşar Can")
selamVer()


def selamVer2(surname , name = "Ziyaretçi"):
    print("Merhaba " + name + " " + surname)

selamVer2("Ali")
selamVer2("Ali","Topçu")

def dikUcgenAlanHesapla(taban,yukseklik):
    return (taban * yukseklik) / 2

print(dikUcgenAlanHesapla(4,5))

dikUcgenAlanHesapla2 = lambda a,b : (a*b)/2
print(dikUcgenAlanHesapla2(4,5))
print(type(dikUcgenAlanHesapla2))

x = dikUcgenAlanHesapla2 # x'e fonksiyon atadım "GARİP" !

print(x(4,5)) # şimdide kullandım x'i fonksiyon olarak

