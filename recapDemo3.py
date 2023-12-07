num = int(input("Sayı giriniz : "))

asalMı = True

if(num <= 1):
    asalMı = False 
else:
    for x in range(2,num):
        if(num % x == 0):
            asalMı = False
            break

if(asalMı == True):
    print(str(num) + " sayısı asal")
else:
    print(str(num) + " sayısı asal değil")
