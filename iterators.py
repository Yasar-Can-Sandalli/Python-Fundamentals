sehirler = ["Ankara","İstanbul","İzmrir","Van"]

iteratorum = iter(sehirler)

print(next(iteratorum))
print(next(iteratorum))
print(next(iteratorum))
print(next(iteratorum))

for sehir in sehirler:
    print(sehir)