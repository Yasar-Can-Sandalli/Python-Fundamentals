# Yazılım Nedir 
# Programlama
# Yazılım Bilgisayar Mühendisliği nedir ? 
# Vs Code Nedir
# IDE Editor Nedir
# Python Java C# JavaScript HTML CSS 
# PascalCase CamelCase
# Fonksiyon = İşlev Operatör işleç

names = ["Ali","Veli","Ahmet","Hasan","Ayşe","Hüseyin"]
print(names)
print(names[0])
print(len(names)) #lenght
names[0] = "Ercan"
print(names[0])
print(names)
print(names[5])

krediler = ["Hızlı Kredi","Maaşını Halkbank'tan alanlara özel","Mutlu emekli ihtiyaç kredisi","Konut Kredisi"]


for kredi in krediler: #for in loop
    print(kredi)

for i in range(len(krediler)):
    print(krediler[i])

for i in range(0,11,2):
    print(i)




def krediList():
    krediler = ["Hızlı Kredi","Maaşını Halkbank'tan Alanlara Özel","Mutlu Emekli İhtiyaç Kredisi","Konut Kredisi"]
    for kredi in krediler:
        print("<option>" + kredi + "</option>")

krediList()



    





