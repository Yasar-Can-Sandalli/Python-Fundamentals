sozluk = {
    "book":"kitap",
    "table":"masa",
    "scholl" : "okul"
}

sozluk2 = dict(masa = "table" , kitap = "book")

sozluk["book"] = "kitap1" #* değer değiştirme
sozluk["pencil"] = "kalem" #* yeni değer

del(sozluk["book"]) #* değer silme
print(len(sozluk))

