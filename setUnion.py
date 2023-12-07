setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}
#? Sanki A ve B kümeleri var Birleşimleri alınıyor

#-Birleşim (union)
print(setA | setB)
print(setA.union(setB))
print(setB.union(setA))

#-Kesişim (intersection)
print(setA & setB)
print(setA.intersection(setB))
print(setB.intersection(setA))

#-Ayrım -> Farklılık veya A-B(a fark b)
print(setA-setB)
#print(setB-setA) #! farklı sonuç verir b de olup a da olmayan demek
print(setA.difference(setB)) 

#+ veya
print(setB-setA)
print(setB.difference(setA))


#! Simetrik fark
print("--------")

print((setA | setB) - (setA & setB))
print((setA-setB) | (setB-setA) )
print((setA | setB) - (setA & setB))
print(setA ^ setB)
print(setB.symmetric_difference(setA))
