def FizzBuzz(x = 0):

    if(x % 15 == 0):
        return "FizzBuzz"
    elif(x % 5 == 0):
        return "Buzz"
    elif(x % 3 == 0):
        return "Fizz"
    else:
        return "Normal Number"


fizzAdet = 0
buzzAdet = 0
fizzBuzzAdet = 0
normalNumberAdet = 0

num = int(input("Sayı Giriniz : "))

for i in range(1,num + 1):
    if(FizzBuzz(i) == "FizzBuzz"):
        fizzBuzzAdet = fizzBuzzAdet + 1
    elif(FizzBuzz(i) == "Fizz"):
        fizzAdet = fizzAdet + 1
    elif(FizzBuzz(i) == "Buzz"):
        buzzAdet = buzzAdet + 1
    else:
        normalNumberAdet = normalNumberAdet + 1


print(" Fizz Adet : " + str(fizzAdet))    
print(" Buzz Adet : " + str(buzzAdet))
print("FizzBuzz Adet : " + str(fizzBuzzAdet))
print("Normal Sayı Adet : " + str(normalNumberAdet))  


#?




#Sayı Giriniz : 15
# Fizz Adet : 4
# Buzz Adet : 2
#FizzBuzz Adet : 1
#Normal Sayı Adet : 8

