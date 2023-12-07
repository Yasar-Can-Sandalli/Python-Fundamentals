x = int(input("Sayı 1 :"))
y = int(input("Sayı 2 :"))
z = int(input("Sayı 3 :"))


if((x>=y) and (x>=z)):
    print(x)
elif((y>=z) & (y>=x)):
    print(y)
else:
    print(z)