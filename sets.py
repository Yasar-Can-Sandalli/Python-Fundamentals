studentsSet = {"Engin","Ayla","Salih","Ahmet"}
print(studentsSet)

for student in studentsSet:
    print(student)

print("Ayla" in studentsSet)

if("Ahmet" in studentsSet):
    print("listede var")

studentsSet.add("Ali")
print(studentsSet)

studentsSet.update(["Merve","Mert","Ayşe"])
print(studentsSet)
print(len(studentsSet))

studentsSet.remove("Ahmet") #* bulamazsa hata verir
print(len(studentsSet))

studentsSet.discard("Ahmet") #* bulamazsa hata çıkarmaz
print(len(studentsSet))

# x = studentsSet.pop() #* Random eleman siliyor
# print(len(studentsSet))
# print(studentsSet)

studentsSet.clear() #! clear diyince içindeki elemanlar temizlenir sadece set() kalır
print(len(studentsSet))
del studentsSet #! seti tamamen siler
#print(studentsSet)




#+ NOT:
#- tuplelar() = indexlidir sonradan değiştiremezler
#- setler{} = indexsizdir sonradan değiştirilebirler veri tekrarı olamaz
#- listeler[] = indexlidir sonradan değiştirebilir


