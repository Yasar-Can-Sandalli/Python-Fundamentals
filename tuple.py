tupleListe = (2,4,6,"Ankara",(2,3,4),[])
liste = [2,4,6,"Ankara",[3,4,5],()]
liste[0] = 6

# tupleListe[0] = 6 #! Tuple değiştirilemez

print(tupleListe[1:2]) #* 1 dahil 2 dahil değil
print(liste[1:2]) #* 1 dahil 2 dahil değil

tupleDeger = ("Engin",) #- Tek elemanda tuple çalışmaz str anlar.Tek elemanda tuple çalıştırmak için sonuna , koyarız

print(tupleDeger) 
print(type(tupleDeger))

print(tupleListe[-2])
print(liste[-2])



print(type(liste))
print(type(tupleListe))
print(liste)
print(len(tupleListe))
print(len(liste))


