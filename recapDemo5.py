import sys
list = [6,7,"Yaşar Can","8","9"]

for x in list:
    try:
        print("Sayı : " +  str(x))
        result = 1 / int(x)
        print("Sonuc : "  + str(result))
    except(ValueError): 
        print(str(x) + " ınterger değil")
    except(ZeroDivisionError):
        print("Payda 0 olamaz")
    except:
        print("Hesaplanamayan değer " + str(x))
        print("Sistem Diyorki",sys.exc_info())
    finally:
        print("İşlem Bitti")

# import sys
# list = [7,'Engin',0,3,"6"]

# for x in list:
#     try:
#         print("Sayı : ",str(x))
#         sonuc = 1 / int(x)
#         print("sonuc : " + str(sonuc))
#     except (ValueError):
#         print(str(x) + " integer değil")
#     except ZeroDivisionError:
#         print("Payda",x,"olmazzz !!!")
#     except:
#         print("Hesaplanamayan Değer : ",x)
#         print("Sistem Diyor ki : ",sys.exc_info()[0])
#     finally:
#         print("işlem Bitti")