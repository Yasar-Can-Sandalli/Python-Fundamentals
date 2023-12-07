sehirler = ["Ankara","İstanbul","İzmir","Bursa"]

# print(sehirler[0])
# print(sehirler[len(sehirler) - 1])


for sehir in sehirler:
    if(sehir == "İstanbul"):
        continue
    print(sehir[0:3]) 
    print("--------")  

# For range
for x in range(0,100,2):
    print(x)

